class Password:

	def __init__(self, password='elykips+254'):
		self.__password = password

	def change_password(self, old_password, new_password):
		if old_password == self.__password:
			self.__password = new_password
		else:
			print("Wrong Password!")



first_attempt = Password()
print("#-------------- Change Password --------------#")
old_password = input("Enter old pasword: ")
new_password = input("Enter new pasword: ")

first_attempt.change_password(old_password, new_password)


