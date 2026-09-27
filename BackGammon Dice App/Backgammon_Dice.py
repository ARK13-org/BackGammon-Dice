import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

def generate_num() :
    num_list = []
    a = random.randint(1,6)
    b = random.randint(1,6)
    if a == b :
        return [a , a , a , a]
    return [a , b]

def generate_dice_faces(num_list):
    if len(num_list) != 2:
        print("You rolled a double! Here are your four dice:")
    else:
        print("Here are the results of your dice roll:")

    for lines in zip(*(DICE_ART[num] for num in num_list)):
        print("   ".join(lines))

num_list = generate_num()
generate_dice_faces(num_list)