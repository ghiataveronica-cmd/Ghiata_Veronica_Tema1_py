product = input("Product: ")

# ValueError: input() returneaza string, trebuie convertit in int.
quantity = int(input("Quantity: "))

# SyntaxError: lipsea o paranteza inchisa.
price = float(input("Unit price: "))

# TypeError: quantity trebuie sa fie numar pentru inmultire.
subtotal = quantity * price

# NameError: vat_rate nu era definit.
vat_rate = 0.19
vat = subtotal * vat_rate

total = subtotal + vat

# SyntaxError: lipsea virgula dintre argumente.
print("Product:", product)

print(f"Quantity: {quantity}")

# TypeError: nu putem concatena direct un string cu un float.
print("Subtotal:", subtotal)

# SyntaxError: lipsea ghilimeaua de inchidere.
print(f"VAT: {vat:.2f}")

# SyntaxError: lipsea paranteza de inchidere.
print(f"Total: {total:.2f}")