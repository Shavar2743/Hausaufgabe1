operatorliste = ["+", "-", "/", "*"]

zahl1 = int(input("Erste Zahl: "))
operator = input("Operator: ")
zahl2 = int(input("Zweite Zahl: "))

if operator in operatorliste:
    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "/":
        ergebnis = zahl1 / zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    print(ergebnis)
else:
    print("Gib einen gültigen Operator ein")