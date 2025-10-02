
name_key = "name"
gender_key = "gender"
age_key = "age"
address_key = "address"
phone_key = "phone"

print ("This program lets you look up a detail of a person from the following list:")

personal_details = { name_key: "Mark Polo", gender_key: "male", age_key: 326, address_key: "101 Silk Rd, India", phone_key: "+25 44 3346-2234" }
print (personal_details.keys())

print()

requested = input ("Type the key you wish to look up: ")

print ("The value of", requested, "is", personal_details[requested])

