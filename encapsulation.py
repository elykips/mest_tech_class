class Secret:

	def __init__(self, secret, password):
		self.__secret = secret
		self.__password = password

	def get_secret(self, password):
		if password == self.__password:
			print(self.__secret)
		else:
			print("Go away Mum")

andrews_secret = Secret("Andrew is beautiful", "True")
andrews_secret.get_secret("True")