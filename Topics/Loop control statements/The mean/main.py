mean = 0
index = 0
while True:
    number = input()
    if number == '.':
        break
    intNumber = int(number)
    mean += intNumber
    index += 1
print(mean / index)
