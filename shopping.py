names = []
quantities = []
prices = []
line_totals = []

for i in range(1, 4):
    name = input("Product name: ")
    qty = int(input("Quantity: "))
    price = float(input("Unit price: "))

    line_total = qty * price

    names.append(name)
    quantities.append(qty)
    prices.append(price)
    line_totals.append(line_total)

subtotal = sum(line_totals)
vat = subtotal * 0.19
total = subtotal + vat

print("-" * 39)
print(f"{'Product':<12}{'Qty':>5}{'Unit':>8}{'Line total':>14}")
print("-" * 39)

for i in range(3):
    print(f"{names[i]:<12}{quantities[i]:>5}{prices[i]:>8.2f}{line_totals[i]:>14.2f}")

print("-" * 39)
print(f"{'Subtotal':<25}{subtotal:>14.2f}")
print(f"{'VAT (19%)':<25}{vat:>14.2f}")
print(f"{'Total':<25}{total:>14.2f}")
print("-" * 39)