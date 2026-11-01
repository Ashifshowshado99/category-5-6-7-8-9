temperature = float(input("Enter Body Temperature: "))

if temperature < 37:
    fever = 0
elif temperature < 39:
    fever = (temperature - 37) / 2
else:
    fever = 1

if fever >= 0.5:
    print("High Fever")
    print("Medical Attention Required")
else:
    print("Normal or Mild Temperature")