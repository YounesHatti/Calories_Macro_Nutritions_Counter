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

# Exit
input("Press any key to exit")