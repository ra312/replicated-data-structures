import time
from threading import RLock

from time import time

import pprint
pp = pprint.PrettyPrinter(indent=4)


class Set:
	'''
		A Last-Write-Wins Set CRDT implementation
	'''
	def __init__(self):
		# a lock to add elements
		self.added = dict() # {element: timestamp_when_added}
		self.removed = dict()
		self.lock_when_adding = RLock()
		self.lock_when_removing = RLock()
	def __print__(self):
		added = self.added
		print("\n")
		pp.pprint(added)

	def __update__(self, el, elements):
		# we create a timestamp at the time of adding element
		timestamp = time()
		if el in elements:
			 # if element is in added, then 
			# we do not update timestamp
			current_timestamp = elements[el]
			if current_timestamp < timestamp:
				# adding same element later 
				elements[el] = timestamp
		else:
			elements[el] = timestamp
			

	def add(self, element):
		# we create a timestamp at the time of adding element
		elements = self.added
		op_state = True
		self.lock_when_adding.acquire()
		try:
			self.__update__(el=element, elements=elements)
		except Exception as e:
			print(f"An exception {str(e)} occured")
			op_state = False
		finally:
			self.lock_when_adding.release()
		return op_state

	def remove(self, element):
		# we create a timestamp at the time of adding element
		elements = self.removed
		op_state = True
		self.lock_when_adding.acquire()
		try:
			self.__update__(el=element, elements=elements)
		except Exception as e:
			print(f"An exception {str(e)} occured")
			op_state = False
		finally:
			self.lock_when_adding.release()
		return op_state

	def exists(self, element):
		'''
			Return: False if element does not exist
		'''
		added  = self.added
		removed = self.removed

		try:
			if element not in added:
				return False
			elif element not in removed:
				# if element exists and it has not yet been removed
				# then we return True
				return True
			elif self.added[element] >= self.removed[element]:
				# if the element has been added after the removal
				# we still consider it in the added set
				return True
			else:
				# we added and then removed it (chron order)
				# then it's been removed
				return False
		except:
			raise RuntimeError(f"An internal error when checking if {element} exists")

	def merge(self, other):
		'''
		merge one LWW-Set with other LWW-Set
		:param other:
		:return: Lww
		'''

		merged_set = Set()

		with self.lock_when_adding, self.lock_when_removing, other.lock_when_adding, other.lock_when_removing:

			# Merge add_set
			merged_set.added = {**self.added, **other.added}

			# Merge remove_set
			merged_set.removed = {**self.removed, **other.removed}

			# Update lww with latest timestamp in add_set
			for element, timestamp in self.added.items():
				merged_set.added[element] = max(merged_set.added[element], timestamp)

			# Update lww with latest timestamp in remove_set
			for element, timestamp in self.removed.items():
				merged_set.remove[element] = max(merged_set.remove[element], timestamp)


		return merged_set



		
		
