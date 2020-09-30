en_message = input()
key = int(input())
b = (key).to_bytes(2, byteorder='big')
f = 0
for v in b:
    f += v
n = ''
for c in en_message:
    n += chr(int.from_bytes(c.encode(), 'little') + f)
print(n)
