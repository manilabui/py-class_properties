from student import Student

me = Student()
me.last_name = 'Bui'
me.first_name = 'Manila'
me.cohort = 36
me.age = 27
print(me)

from patient import Patient

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

print(cashew.ssn)
print(cashew.full_name)
print(cashew.hian)
print(cashew.dob)
print(cashew.address)