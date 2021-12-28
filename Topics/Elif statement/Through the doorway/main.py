a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
flagX = False
flagY = False
if x >= a or x >= b or x >= c:
    flagX = True
if y >= a or y >= b or y >= c:
    flagY = True
if flagX and flagY:
    print("The box can be carried")
else:
    print("The box cannot be carried")