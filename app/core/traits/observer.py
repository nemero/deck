class ObserverTrait:
	"""docstring for ObserverTrait"""
	def __init__(self, observer):
		print(observer)
		self.observer = observer

	def parse_command(self, response):
		"""parse response command"""
		pass