def get_punched(health, armor):
    # ?


def get_slashed(health, armor):
    # ?


# Don't touch below this line


def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=====================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=====================================")


test(400, 5)
test(300, 3)
test(200, 1)

# Complete both the get_punched and get_slashed functions. They should each take 2 arguments:

# health: An integer
# armor: An integer
# Change the functions so if no armor argument is passed, armor defaults to 0.

# Each attack does a different amount of damage. Getting 
# punched does 50 damage. Getting slashed does 100 damage. The armor should
# absorb some of the attack by subtracting from the damage.
# The rest of the damage should be applied to the health. Return a single integer, 
# the health left over after the attack.