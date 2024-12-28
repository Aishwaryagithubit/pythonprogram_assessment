#ask user to input the number of sweets and the number of pupils
sweets = int(input("How many sweets?"))
pupils = int(input("how many pupils attend today?"))

# Calculate the number of sweets for each pupil and the number of leftovers
sweets_calculation = sweets//pupils
left_over_sweets = sweets % pupils
print(f"Each pupil will get {sweets_calculation} sweets.")
print(f"There will be {left_over_sweets} sweets left over.")