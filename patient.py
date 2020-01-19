class Patient:
		def __init__(self, ssn, dob, hian, first_name, last_name, address):
				self.__first_name = first_name
				self.__last_name = last_name
				self.__ssn = ssn
				self.__dob = dob
				self.__hian = hian
				self.__address = address

		@property
		def full_name(self):
				return f'{self.__first_name} {self.__last_name}'

		@property
		def ssn(self):
				return self.__ssn

		@property
		def dob(self):
				return self.__dob

		@property
		def hian(self):
				return self.__hian

		@property
		def address(self):
				return self.__address

		@address.setter
		def address(self, new_address):
				if type(new_address) is str:
						self.__address = new_address
				else:
						raise TypeError('Please provide a string for the address.')