n = input()
print([(int(list(n)[i])+int(list(n)[i+1]))/2 for i in range(len(n)-1)])