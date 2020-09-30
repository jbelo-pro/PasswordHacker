n = int(input())
b = (n).to_bytes(2, byteorder='big')
f = 0
for v in b:
    f += v

print(type(f))
