pyramid = int(input())
result = " " * (pyramid - 1) + "#" + " " * (pyramid - 1)
for i in range(pyramid):
    if i != 0:
        result = result + "\n" + " " * (pyramid - i - 1) + "#" + "#" * 2 * i + " " * (pyramid - i - 1)
for line in result.splitlines():
    print(line)
