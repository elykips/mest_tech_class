class ElectricOutlet:
	pass
class UkOutlet(ElectricOutlet):
	pass
class UsOutlet(ElectricOutlet):
	pass

andrew_outlet = UsOutlet()
edem_outlet = UkOutlet()

print(isinstance(andrew_outlet, ElectricOutlet))
print(isinstance(edem_outlet,ElectricOutlet))