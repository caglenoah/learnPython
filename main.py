dmg_one = 2
dmg_two = 4
dmg_three = 3
dmg_four = -1
dmg_five = 10
dmg_six = 5

# Don't touch above this line


def calculate_damage(opening_attack, core_damage, finishing_move):
    return opening_attack + core_damage + finishing_move


# Don't touch below this line

print("Getting damage for", dmg_one, dmg_two, "and", dmg_three, "...")
print(calculate_damage(dmg_one, dmg_two, dmg_three), "points of damage dealt!")
print("=====================================")

print("Getting damage for", dmg_four, dmg_five, "and", dmg_six, "...")
print(calculate_damage(dmg_four, dmg_five, dmg_six), "points of damage dealt!")
print("=====================================")
