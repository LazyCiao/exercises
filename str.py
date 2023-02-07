word = input('Enter a word: ')

x = list(word)
for i in x[0::2]:
    print(i)