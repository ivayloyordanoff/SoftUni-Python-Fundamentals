def total_price(current_product, current_quantity):
    if current_product == "coffee":
        return 1.50 * current_quantity
    elif current_product == "water":
        return 1.00 * current_quantity
    elif current_product == "coke":
        return 1.40 * current_quantity
    elif current_product == "snacks":
        return 2.00 * current_quantity


product = input()
quantity = int(input())

result = total_price(product, quantity)

print(f"{result:.2f}")
