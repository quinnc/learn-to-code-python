
print ("This program calculates your BMI.")

units = input ("Enter 'y' to use metric units otherwise imperial units will be used: ")
underweight_bmi_max = 18.5
normal_bmi_max = 24.9
overweight_bmi_max = 30

if (units == 'y'):
    weight = float(input ("Enter your weight (kg): "))
    height = float(input ("Enter your height (m): "))

    bmi = weight / (height ** 2)
else:
    weight = float(input ("Enter your weight (lbs): "))
    height = float(input ("Enter your height (ft): "))
    height = height * 12

    bmi = (weight / (height ** 2)) * 703
    
    
print ("Your BMI is", round(bmi, 1))

if (bmi <= underweight_bmi_max):
    print ("You are underweight.")
elif (bmi <= normal_bmi_max):
    print ("You are normal weight.")
elif (bmi < overweight_bmi_max):
    print ("You are overweight.")
else:
    print ("You are obese.")
