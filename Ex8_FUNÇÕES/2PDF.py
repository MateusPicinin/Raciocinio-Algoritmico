def inverter(palavra):
    return(palavra[::-1])

def e_palindromo():
    a = input('Digite uma palavra palíndroma: ')
    if a == inverter(a):
        return True
    else:
        return False


print(e_palindromo())