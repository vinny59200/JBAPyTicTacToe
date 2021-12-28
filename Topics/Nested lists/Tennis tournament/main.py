n = int(input())
list = []
for i in range(n):
    name = input()
    list.append(name)
print([name[:-4] for name in list if name.endswith("win")])
print(len([name for name in list if name.endswith("win")]))
