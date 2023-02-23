d = input()

r = d.count('R')
y = d.count('Y')
g = d.count('G')

if (r >= 3) or (r >= 2 and y >= 2) or (y >= 5):
    print("nakhor lite")
else:
    print("rahat baash")
