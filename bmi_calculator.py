def get_weight():
    while True:
        unit = input("Enter weight unit (kg/lbs): ").strip().lower()
        if unit in ["kg", "lbs"]:
            break
        print("Invalid input. Please type 'kg' or 'lbs'.")
    
    while True:
        try:
            weight = float(input(f"Enter your weight in {unit}: "))
            if weight > 0:
                break
            else:
                print("Weight must be greater than 0.")
        except ValueError:
            print("Invalid number. Please enter a valid weight.")
    
    if unit == "lbs":
        weight = weight / 2.205  # convert lbs to kg
    return weight

def get_height():
    while True:
        unit = input("Enter height unit (m/cm): ").strip().lower()
        if unit in ["m", "cm"]:
            break
        print("Invalid input. Please type 'm' or 'cm'.")
    
    while True:
        try:
            height = float(input(f"Enter your height in {unit}: "))
            if height > 0:
                break
            else:
                print("Height must be greater than 0.")
        except ValueError:
            print("Invalid number. Please enter a valid height.")
    
    if unit == "cm":
        height = height / 100  # convert cm to meters
    return height

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "You should consider a nutritious diet to gain weight."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Great! Keep maintaining a healthy lifestyle."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Try to exercise regularly and watch your diet."
    else:
        return "Obesity", "Consult a healthcare professional for guidance."

def display_bmi(bmi, category, advice):
    print("\n" + "="*30)
    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print(f"Advice: {advice}")
    print("="*30)
    
    # ASCII progress bar
    max_bmi = 40
    bar_length = 30
    bmi_position = min(int((bmi / max_bmi) * bar_length), bar_length)
    print("BMI Progress:")
    print("[" + "="*bmi_position + " "*(bar_length - bmi_position) + "]")
    print("\n")

def main():
    print("Welcome to the BMI Calculator!\n")
    weight = get_weight()
    height = get_height()
    bmi = calculate_bmi(weight, height)
    category, advice = bmi_category(bmi)
    display_bmi(bmi, category, advice)

if __name__ == "__main__":
    main()
