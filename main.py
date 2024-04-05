body_weight = float(input("Please enter you body weight: "))

protein_min = body_weight
protein_max = body_weight * 1.2

drink = body_weight * 30 -800

print(f"You should eat between {protein_min} and {protein_max} gramms of protein and drink {drink/1000} liters per day.")
