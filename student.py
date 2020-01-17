# Define a Python class named Student. This class will have 5 properties.
class Student:
		@property
		def first_name(self):
				try:
						return self.__first_name
				except AttributeError:
						return 0

		@first_name.setter
		def first_name(self, new_first_name):
				if type(new_first_name) is str:
						self.__first_name = new_first_name
				else:
						raise TypeError('Please provide a string for the first name.')

		@property
		def last_name(self):
				try:
						return self.__last_name
				except AttributeError:
						return 0

		@last_name.setter
		def last_name(self, new_last_name):
				if type(new_last_name) is str:
						self.__last_name = new_last_name
				else:
						raise TypeError('Please provide a string for the last name.')

		@property
		def age(self):
				try:
						return self.__age
				except AttributeError:
						return 0

		@age.setter
		def age(self, new_age):
				if type(new_age) is int:
						self.__age = new_age
				else:
						raise TypeError('Please provide a float for the age.')

		@property
		def cohort(self):
				try:
						return self.__cohort
				except AttributeError:
						return 0

		@cohort.setter
		def cohort(self, new_cohort):
				if type(new_cohort) is int:
						self.__cohort = new_cohort
				else:
						raise TypeError('Please provide a float for the cohort.')

		@property
		def full_name(self):
				return f'{self.first_name} {self.last_name}'