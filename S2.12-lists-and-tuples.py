print ("This progrma asks for your birthday and determines which month you were born in.")

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

birthday = input ("Please enter your birthday (DD-MM-YYYY): ")

birth_month = birthday.split('-')
birth_month_num = int(birth_month[1])

print ("You were born in", months[birth_month_num-1])

print ("Now let's add your name to the class list.")
new_name = input ("PLease enter your first name: ")

names = ['Aaron', 'Belinda', 'Everly', 'Walter']

names.append (new_name)

print ("The class list is now", names);


