class Event:

	def __init__(self):
		self.contacts_dict = {}

	def register_person(self):
		self.name = input("Enter name: ")
		self.email = input("Enter email: ")
		self.contacts_dict[self.name] = self.email
		return self.contacts_dict

	def search_contact(self):
		name = input("Enter name to search: ")
		for key in self.contacts_dict:
			if key == name:
				print(self.contacts_dict[key]) 


mest_party = Event()
mest_party.register_person()
mest_party.search_contact()




