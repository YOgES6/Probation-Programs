def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h
def BMI(weight, height):
    return weight / height**2
def evaluate_BMI(bmi):
    if bmi < 15:
        return "Very severely underweight"
    elif bmi < 16:
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal (healthy weight)"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class I (Moderately obese)"
    elif bmi < 40:
        return "Obese Class II (Severely obese)"
    else:
        return "Obese Class III (Very severely obese)"
f = compose(evaluate_BMI, BMI)
again = "y"
while again == "y":
    weight = float(input("weight (kg) "))
    height = float(input("height (m) "))
    print(f(weight, height))
    again = input("Another run? (y/n)")
