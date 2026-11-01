distance = float(input("Enter Obstacle Distance: "))

if distance <= 5:
    risk = 1
elif distance <= 20:
    risk = (20 - distance) / 15
else:
    risk = 0

print("Obstacle Risk:", round(risk, 2))

if risk >= 0.7:
    print("Vehicle Stops")
elif risk >= 0.3:
    print("Vehicle Slows Down")
else:
    print("Vehicle Moves Normally")