class Toilet(object):
	def __eq__(self, other):
		return (isinstance(other, self.__class__) 
			and self.id == other.id 
			and self.name == other.name
			and self.latitude == other.latitude
			and self.longitude == other.longitude)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		if self.id:
			return hash(self.id)
		else:
			return hash(self.name + str(self.latitude) + ',' + str(self.longitude))

	def __init__(self, name, id, latitude, longitude, locality, state, facility_type, 
	p, address1, address2, sm, tt, hours, date):
		self.name = name
		self.id = id
		self.latitude = latitude
		self.longitude = longitude
		self.locality = locality
		self.state = state
		self.facility_type = facility_type
		self.p = p
		self.address1 = address1
		self.address2 = address2
		self.sm = sm
		self.tt = tt
		self.hours = hours
		self.date = date
		self.provided_by = {
			'name': '',
			'email': '',
			'url': ''
		}

	def __dir__(self):
		return [
			'provided_by', 'name', 'longitude', 'latitude', 'p', 'tt', 'sm', 
			'locality', 'state', 'address1', 'address2', 'facility_type', 'for_male', 'for_female', 'accessible_for_male', 'accessible_for_female', 'has_accessible_parking', 'has_showers', 'for_baby_changing', 'has_syringe_disposal'
		]
