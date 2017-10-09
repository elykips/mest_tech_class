class ElectricOutlet:
	pass
class UkOutlet(ElectricOutlet):
	pass
class UsOutlet(ElectricOutlet):
	pass

andrew_outlet = UsOutlet()
edem_outlet = UkOutlet()

if isinstance(andrew_outlet,UsOutlet):
	print("US outlet")
	
else:
	print("This is not US outlet")

print(isinstance(andrew_outlet, ElectricOutlet))
print(isinstance(edem_outlet,ElectricOutlet))