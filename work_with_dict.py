import smtplib


class Event:

	def __init__(self, contacts_dict={}):
		self.contacts_dict = contacts_dict

	def register_person(self,name,email):
		self.contacts_dict[name] = email
		return self.contacts_dict

	def search_contact(self, name):
		return self.contacts_dict.get(name, "Sorry, name not found")

	def get_email_addresses(self):
		contact_list = []
		for value in self.contacts_dict.values():
			contact_list.append(value)
		return contact_list		



gmail_mail = "elkana@meltwater.org"
gmail_password = "elykips+254"

#----------- CREATE INSTANCE OF CLASS EVENT -----------# 
mest_party = Event()

#----------- CREATE PERSON WITH GIVEN PARAMETERS -----------#
mest_party.register_person('ouma','rodgers.ouma@meltwater.org')

#----------- SEARCH AND DISPLAY EMAIL FOR GIVEN NAME -----------#
search_results = mest_party.search_contact("ouma")
print(search_results)

#----------- GET LIST OF EMAIL ADDRESSES FROM DICT -----------#
receiver_emails = mest_party.get_email_addresses()
print(receiver_emails)

#----------- CAPTURE CONTENT -----------#
content = input("Type your email here: ")


#----------- SMTP CONFIGS -----------# 
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(gmail_mail,gmail_password)
mail.sendmail(gmail_mail,receiver_emails,content)
mail.close()
print("Succesfully sent :)")


