post_out = input("input post-puts: ")
post_out_list = post_out.split()
print(post_out_list)

run_again = True

while run_again is True:
    Tanks = {'wuflungpu': 1, 'ragnarokmol': 1, 'zellax': 1, 'Tjdent': 1}
    Healers = {'aerie': 6, 'alviaren': 8, 'clynlyn': 8, 'kalishnakov': 8, 'lightscythe': 8, 'stympy': 6, 'violente': 7, 'yakitori': 7}
    Melee = {'aiden': 8, 'chozen': 10, 'compensator': 9, 'crushero': 6, 'deathkingz': 8, 'kountswagula': 9, 'paez': 7, 'ramstrom': 5, 'shadez': 8, 'thorninass': 5}
    Ranged = {'awnek': 7, 'bowwow': 7, 'caessa': 10, 'darknhorny': 8, 'deadpets': 5, 'feralwarrior': 5, 'fide': 10, 'grim': 10, 'jakskelingtn': 8, 'lynxz': 9, 'phantum': 10, 'rvr': 8}

    for each in post_out_list:
        if each in Healers:
            Healers.pop(each)
        if each in Ranged:
            Ranged.pop(each)
        if each in Melee:
            Melee.pop(each)

    heals = int(len(Healers)/2)
    melee = int(len(Melee)/2)
    ranged = int((len(Ranged)/2) - 1)

    raid1 = dict([Tanks.popitem(), Tanks.popitem(), ('mass', 6), ('sola', 5)])
    while heals > 0:
        heals -= 1
        healer = dict([Healers.popitem()])
        raid1.update(healer)

    while melee > 0:
        melee -= 1
        melees = dict([Melee.popitem()])
        raid1.update(melees)

    while ranged > 0:
        ranged -= 1
        rangers = dict([Ranged.popitem()])
        raid1.update(rangers)

    heals = int(len(Healers))
    melee = int(len(Melee))
    ranged = int(len(Ranged))

    raid2 = dict([Tanks.popitem(), Tanks.popitem()])
    while heals > 0:
        heals -= 1
        healer = dict([Healers.popitem()])
        raid2.update(healer)

    while melee > 0:
        melee -= 1
        melees = dict([Melee.popitem()])
        raid2.update(melees)

    while ranged > 0:
        ranged -= 1
        rangers = dict([Ranged.popitem()])
        raid2.update(rangers)

    raid1_list = list(raid1.values())
    raid2_list = list(raid2.values())

    raid1_avg = sum(raid1_list)/len(raid1_list)
    raid2_avg = sum(raid2_list)/len(raid2_list)

    if abs(raid1_avg - raid2_avg) > 1:
        run_again = True
    else:
        run_again = False

print(raid1_avg, len(raid1_list))
print(raid2_avg, len(raid2_list))
print(raid1)
print(raid2)
