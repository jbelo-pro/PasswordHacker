first_word = input()
second_word = input()

new_word = ''

for fw, sw in zip(first_word, second_word):
    new_word += fw + sw

print(new_word)
