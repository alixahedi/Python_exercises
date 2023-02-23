n = int(input())
words = input()

words = words.split(' ')
words = words[slice(None, None,-1)]
for i in range(0, n):
    print(words[i], end=" ")
