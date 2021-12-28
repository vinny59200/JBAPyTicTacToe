name, cats = input().split()
max_name = name.strip()
max_cats = int(cats)
while True:
    data = input()
    if data == 'MEOW':
        break
    name, cats = data.split()
    name = name.strip()
    cats = int(cats)
    if cats > max_cats:
        max_name = name
        max_cats = cats
        continue
print(max_name)