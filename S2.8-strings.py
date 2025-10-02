firstname=input("Please type your first name:")
middlename=input("Please type your second name:")
lastname=input("Please type your last name:")

print("Your initials are", firstname[0] + middlename[0] + lastname[0])

lot_number = input ("Please enter the log number: ")

product_array = lot_number.split('-')

print ("Using the split() function...")
print ("Country code:", product_array[0]);
print ("Product code:", product_array[1]);
print ("Batch number:", product_array[2]);

print()
print ("Using slices...")
print ("Country code:", lot_number[:3]);
print ("Product code:", lot_number[4:9]);
print ("Batch number:", lot_number[-5:]);
