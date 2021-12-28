s = input()
snake_case = ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')
print(snake_case)
