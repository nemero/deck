class Observer:
	"""docstring for Observer"""
	def __init__(self):
		self.events = {}
		
	def register(self, *events_group):
		"""register observe events group"""
		for event in events_group:
			if event not in self.events:
				self.events[event] = []
			else:
				"""raise throw error if event already observed"""
				pass

		print(self.events)
		
	def subscribe(self, event_group, callback):
		if event_group in self.events:
			self.events[event_group].append(callback)
		else:
			"""raise throw if event_group not exist"""
			pass

	def event(self, event_group, data, *args, **keywords):
		"""call all subscribe methods for pass event name"""
		if event_group in self.events:
			for event in self.events[event_group]:
				event(data, *args, **keywords)
		else:
			# raise throw or notify if event not exist
			pass