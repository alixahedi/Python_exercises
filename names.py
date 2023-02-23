def unique(data):
  return list(dict.fromkeys(data))

names = []
name_len = 0
largest_name_len = 0

n = int(input())

for i in range(0, n):
    names.append(input())
    names[i] = unique(names[i])
    name_len = len(names[i])
    if name_len > largest_name_len:
        largest_name_len = name_len

print(largest_name_len)
