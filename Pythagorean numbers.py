
angles = []
angles.append (int(input()))
angles.append (int(input()))
angles.append (int(input()))

angles.sort()

if ((angles[0] ** 2) + (angles[1] ** 2) == (angles[2] ** 2)):
    print("YES")
else:
    print("NO")