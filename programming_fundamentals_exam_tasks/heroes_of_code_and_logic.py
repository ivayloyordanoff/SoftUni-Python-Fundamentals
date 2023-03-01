number_of_heroes = int(input())

heroes = {}

for hero in range(number_of_heroes):
    data = input().split(' ')

    heroes[data[0]] = [int(data[1]), int(data[2])]

while True:
    command = input().split(" - ")

    current_command = command[0]

    if current_command == "End":
        break

    if current_command == "CastSpell":
        hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
        available_mp = heroes[hero_name][1]

        if available_mp >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            current_mp = heroes[hero_name][1]
            print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif current_command == "TakeDamage":
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        heroes[hero_name][0] -= damage
        current_hp = heroes[hero_name][0]

        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif current_command == "Recharge":
        hero_name, amount = command[1], int(command[2])
        available_mp = heroes[hero_name][1]

        if available_mp + amount > 200:
            amount = 200 - available_mp
            heroes[hero_name][1] += amount
        else:
            heroes[hero_name][1] += amount

        print(f"{hero_name} recharged for {amount} MP!")

    elif current_command == "Heal":
        hero_name, amount = command[1], int(command[2])
        available_hp = heroes[hero_name][0]

        if available_hp + amount > 100:
            amount = 100 - available_hp
            heroes[hero_name][0] += amount
        else:
            heroes[hero_name][0] += amount

        print(f"{hero_name} healed for {amount} HP!")

result = ""

for hero in heroes:
    result += f"{hero}\n  HP: {heroes[hero][0]}\n  MP: {heroes[hero][1]}\n"

print(result)
