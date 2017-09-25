class EventSubscriber:

	def __init__(self, name, email):
		self.name = name
		self.email = email

	def add_event_subscriber(self):
		self.contact_dict = {}
		self.name = input("Enter name: ")
		self.email = input("Enter email: ")
		self.contact_dict[self.name]=[self.email]




