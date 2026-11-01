temperature = float(input("Enter Machine Temperature: "))

if temperature <= 50:
    risk = 0
elif temperature <= 100:
    risk = (temperature - 50) / 50
else:
    risk = 1

print("Machine Risk:", round(risk, 2))

if risk >= 0.7:
    print("Critical Temperature")
    print("Maintenance Required")
elif risk >= 0.3:
    print("Warning: Monitor Machine")
else:
    print("Machine Operating Normally")