height =float(input("Enter your Height(in m):"))
weight =float(input("Enter your weight(in kg):"))

BMI = weight/(height**2)
print("Your BMI Value:",BMI)
if(BMI<16):
    print("You are severely underweight...!!")
elif( BMI>=16 and BMI<18.5):
    print("You are Underweight...!!")
elif( BMI>=18.5 and BMI<24):
    print("You are Healthy...!!")
elif( BMI>=24 and BMI<30):
    print("You are Overweight...!!")
else:
    print("Your are obese")

