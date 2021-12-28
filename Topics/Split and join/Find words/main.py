words = input().split()
result=[]
for i in words:
    if i.endswith("s"):
        result.append(i)
print("_".join(result))