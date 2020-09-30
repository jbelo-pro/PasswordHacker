word = input()
cipher = ''
for c in word:
    cipher += chr(ord(c) + 1)
print(cipher)
