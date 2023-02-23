mistakes = 0
n = int(input())
word = input()
user_word = input()

for i in range(0, n):
    if word[i] != user_word[i]:
        mistakes += 1

print(mistakes)