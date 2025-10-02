print ("This progrma asks for your birthday and determines which month you were born in.")

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

birthday = input ("Please enter your birthday (DD-MM-YYYY): ")

birth_month = birthday.split('-')
birth_month_num = int(birth_month[1])

print ("You were born in", months[birth_month_num-1])
