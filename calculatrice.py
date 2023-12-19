def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro"
    
def question():
    print("Sélectionnez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("Q. Quittez")
    choix = input("Entrez votre choix (1/2/3/4/Q): ")
    return choix

operation=question()
while operation !="Q":
    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))

    if operation == '1':
        print("Résultat:", addition(num1, num2))
    elif operation == '2':
        print("Résultat:", soustraction(num1, num2))
    elif operation == '3':
        print("Résultat:", multiplication(num1, num2))
    elif operation == '4':
        print("Résultat:", division(num1, num2))
    else:
        print("Choix invalide")
    operation=question()
