# Calories counter

# inPut user data
Age = input("Enter your age (in years): ")
Height = input("Enter your height (in cm): ")
Weight = input("Enter your weight(in kg): ")
Sex = input("Enter M for Male, F for Female: ")

# Convert variables into floats to use in the calculations.
A = float(Age)
H = float(Height)
W = float(Weight)

# Revised Harris-Benedict Equation to calculate BMR depends on the sex
if Sex == "M":
    BMR = 88.362 + (13.397 * W) + (4.799 * H) - (5.677 * A)
if Sex == "F":
    BMR = (9.247 * W) + (3.098 * H) - (4.330 * A) + 447.593

print("Your Basic Metabolic Rate is: BMR = ", BMR, "Calories")
print("BMR is the amount of energy expended per day at rest.")

# TDEE depend on the activity
print("""Chose the number coresponding to your activity level
         1. Secondary: Little to no exercise
         2. Light: Exercise activities
         3. Moderate: at least exercise 3 times a week pluse medium work.
         4. Active: at least exercise 5 times a week pluse hard work.
         5. Extra active: very intence daily exercise or work.
            """)
Activity = input("Choose the number coresponding to your activity: ")

if Activity == "1":
    TDEE = BMR*1.2
if Activity == "2":
    TDEE = BMR*1.375
if Activity == "3":
    TDEE = BMR*1.55
if Activity == "4":
    TDEE = BMR*1.727
if Activity == "5":
    TDEE = BMR*1.9

print("Your Total Daily Energy Expenditure is: TDEE = ", TDEE, "Calories")

input("press any key to exit app")
