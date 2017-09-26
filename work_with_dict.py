import smtplib


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

	def send_email(self):
		print("Your email is: {}".format(self.email))
		self.pswrd = input("Enter your pasword: ")
		self.reciver_email = input("Thankyou, now enter email for reciver: ")
		self.message = input("Enter message: ") 
		return self.message



mest_party = Event()
mest_party.register_person()
mest_party.search_contact()
mest_party.send_email()

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(mest_party.email,mest_party.pswrd)
mail.sendmail(mest_party.email,mest_party.reciver_email,mest_party.message)
mail.close()
print("Succesfully sent :)")




