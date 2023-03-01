budget = float(input())
price_for_one_kg_flour = float(input())

eggs_price = price_for_one_kg_flour * 0.75
milk_price = price_for_one_kg_flour * 1.25 / 4
one_bread_price = price_for_one_kg_flour + eggs_price + milk_price

colored_eggs = 0
bread_count = 0

while budget >= one_bread_price:
    budget -= one_bread_price
    bread_count += 1
    colored_eggs += 3.

    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2

print(f"You made {bread_count} loaves of Easter bread! Now you have {int(colored_eggs)} eggs and {budget:.2f}BGN left.")
