# Calories counter

Age = input("Enter your age (in years): ")
Height = input("Enter your height (in cm): ")
Weight = input("Enter your weight(in kg): ")
Sex = input("Enter M for Male, F for Female: ")
Goal = input("Type 'G' if you want to gain weight, 'L' if you want to lose weight: ")

# Convert variables into floats to use in the calculations.

A = float(Age)
H = float(Height)
W = float(Weight)

if Sex == "M":
    BMR = 88.362 + (13.397 * W) + (4.799 * H) - (5.677 * A)
if Sex == "F":
    BMR = (9.247 * W) + (3.098 * H) - (4.330 * A) + 447.593

print("Your Basic Metabolic Rate is: BMR = ", BMR, "Calories")
print("BMR is the amount of energy expended per day at rest.")

print("""
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

#Prot is Protein
if Activity == 1:
    Prot = W*1
elif Goal == "G":
    Prot = W*1.7
elif Goal == "L":
    Prot = W*2
else:
    Prot=0

ProCal = Prot*4

# Fat is necessary
Fat = W
FatCal = Fat*9

# Carbs
CarbCal = TDEE - FatCal - ProCal
Carb = CarbCal/4

print("Your Total Daily Energy Expenditure is: TDEE = ", TDEE, "Calories")
print("Your daily needs of Carbs is", Carb, "g")
print("Responsible for ", CarbCal, "Calories")
print("Your daily needs of Protein is", Prot, "g")
print("Responsible for ", ProCal, "Calories")
print("Your daily needs of Fat is", Fat, "g")
print("Responsible for ", FatCal, "Calories")
print("""
        To maintain your weight, you need to eat calories equal to your TDEE
        To lose weight, you need to eat less calories than your TDEE (-300 cal recommanded)
        To gain weight, you need to eat more calories than your TDEE (+300 cal recommanded)
            """)
input("press any key to exit app")
