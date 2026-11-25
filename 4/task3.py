word = input()
max = 0;

for char in "abcdefghijklmnopqrstuvwxyz":
    cur = word.count(char)
    if cur > max:
        max = cur
        max_char = char

new = word.replace(max_char, "")
print(new)
    