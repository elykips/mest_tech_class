class Conversion:

	@staticmethod
	def grammes_to_lbs(grammes):
		#1gm = 0.0022lbs
		multiplier = 0.0022
		return grammes * multiplier

	@staticmethod
	def miles_to_kilometers(miles):
		#1mile = 1.6km
		multiplier = 1.6
		return miles * multiplier

	@staticmethod
	def litres_to_floz(litres):
		#1 liter = 33.815
		multiplier = 33.815
		return litres*multiplier
	@staticmethod
	def litres_to_floz(litres):
		#1 liter = 33.815
		multiplier = 33.815
		return litres*multiplier

	@staticmethod
	def degrees_to_farenheit(temprature):
		return temprature * 1.8 + 32
		
	@staticmethod
	def m_to_cm(meters):
		return meters * 2.54

print(Conversion.grammes_to_lbs(12))
print(Conversion.miles_to_kilometers(24))
print(Conversion.degrees_to_farenheit(100))
print(Conversion.m_to_cm(100))
