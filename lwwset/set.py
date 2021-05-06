import time
from threading import RLock
class LWWSet:
	'''
		A Last-Write-Wins Set CRDT implementation
	'''
	def __init__(self):
		# a lock to add elements
		self.added = dict() # {element: timestamp_when_added}
		self.removed = dict()
		self.lock_when_adding = RLock()
		self.lock_when_removing = RLock()
	
	def add(self, element, timestamp):
		added_elements = self.added
		if element in added:
			current_timestamp = added[element]
			if current_timestamp < timestamp:
                added[element] = timestamp
        else:
            added[element] = timestamp
	
		
		
