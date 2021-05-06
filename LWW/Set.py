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
		
	def add(self, element):
		# we create a timestamp at the time of adding element
		timestamp = time()

		added = self.added
		if element in added:
			 # if element is in added, then 
			# we do not update timestamp
			current_timestamp = added[element]
			if current_timestamp < timestamp:
				# adding same element later 
				added[element] = timestamp
		else:
			self.lock_when_adding.acquire()
			added[element] = timestamp
			self.lock_when_adding.release()

	def exists(self, element):
		return element in self.added
	# def remove(self, element):


		
		
