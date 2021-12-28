import re

name = input()

def normalize(name):

    # put your code here
    new_name = name.replace('é', 'e')
    new_name = new_name.replace('è', 'e')
    new_name = new_name.replace('ê', 'e')
    new_name = new_name.replace('ë', 'e')

    new_name = new_name.replace('à', 'a')
    new_name = new_name.replace('â', 'a')
    new_name = new_name.replace('ä', 'a')
    new_name = new_name.replace('æ', 'ae')


    new_name = new_name.replace('ô', 'o')
    new_name = new_name.replace('ö', 'o')
    new_name = new_name.replace('œ', 'oe')

    new_name = new_name.replace('î', 'i')
    new_name = new_name.replace('ï', 'i')

    new_name = new_name.replace('ç', 'c')

    new_name = new_name.replace('ù', 'u')
    new_name = new_name.replace('û', 'u')
    new_name = new_name.replace('ü', 'u')

    new_name = new_name.replace('ÿ', 'y')


    new = re.sub(r'[àáâãäå]', 'a', new_name)
    new = re.sub(r'[èéêë]', 'e', new)
    new = re.sub(r'[ìíîï]', 'i', new)
    new = re.sub(r'[òóôõö]', 'o', new)
    new = re.sub(r'[ùúûü]', 'u', new)




    return new

print(normalize(name))