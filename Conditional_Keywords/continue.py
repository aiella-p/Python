name = 'Jesaa29Roy'

size = len(name)
i = -1
# iterate loop till the last character
while i < size - 1:
    i = i + 1
    # skip while loop body if current character is not alphabet
    if not name[i].isalpha():
        continue
    # print current character
    print(name[i], end=' ')
