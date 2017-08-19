import numpy as np

def roll(attackers, defenders):
    num_attack = 3
    if attackers < 2:
        print "Insufficient attackers."
        return None
    if attackers < 3:
        num_attack = 1
    elif attackers < 4:
        num_attack = 2
    else:
        num_attack = 3

    num_defend = 2
    if defenders < 2:
        num_defend = 1

    attacks = sorted([np.random.random_integers(1, 6) for ii in range(num_attack)], reverse=True)
    defenses = sorted([np.random.random_integers(1, 6) for ii in range(num_defend)], reverse=True)

    diff = [0, 0]
    if num_attack >= 2 and num_defend == 2:
        if attacks[0] > defenses[0]:
            diff[1] += 1
        else:
            diff[0] += 1
        if attacks[1] > defenses[1]:
            diff[1] += 1
        else:
            diff[0] += 1
    if num_attack == 1 or num_defend == 1:
        if attacks[0] > defenses[0]:
            diff[1] = 1
        else:
            diff[0] = 1

    return diff

def simulate(attackers, defenders):
    while attackers > 1 and defenders >= 1:
        diff = roll(attackers, defenders)
        attackers -= diff[0]
        defenders -= diff[1]
        print "Num attackers: %d, Num defenders: %d" % (attackers, defenders)
