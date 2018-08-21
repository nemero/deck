class Observer:
	"""docstring for Observer"""
	def __init__(self):
		self.events = {}
		
	def register(self, event_group):
		"""register observe events group"""
		if event_group not in self.events:
			self.events[event_group] = []
		else:
			"""raise throw error if event already observed"""
			pass
		
	def subscribe(self, event_group, callback):
		if event_group in self.events:
			self.events[event_group].append(callback)
		else:
			"""raise throw if event_group not exist"""
			pass

	def event(self, event_group, data, *args, **keywords):
		"""call all subscribe methods for pass event name"""
		for event in self.events[event_group]:
			event(data, *args, **keywords)