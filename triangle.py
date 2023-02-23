angles = input()

angles = angles.split(' ')
a, b, c = int(angles[0]), int(angles[1]), int(angles[2])
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Yes")
else:
    print("No")