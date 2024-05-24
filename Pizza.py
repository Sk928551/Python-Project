print("Wellcome to pizza House")

a=int(input("choose one of the following: 1.Nonveg pizza 2.Vegetable pizza "))
bill=0
if a==1:
    non= int(input("choose one of the following: 1.chiken barbeque  2.chiken loaded   3. mutton"))
    chi = int(input("choose one of the following: 1 small 100rs 2.medium 150rs 3.large 300rs "))
    if non==1 and chi==1 :
        print("Small chicken barbeque ")
        bill=bill+100
    elif non==1 and chi==2:
        print("Medium chicken pizza 150rs")
        bill=bill+150
    elif non==1 and chi==3:
        print("Large chicken pizza")
        bill=bill+300

    if non == 2 and chi == 1:
        print("small chicken loaded 100rs ")
        bill = bill + 120
    elif non == 2 and chi == 2:
        print("Medium chicken loaded pizza 150rs")
        bill = bill + 180
    elif non == 2 and chi == 3:
        print("Large chicken  loaded pizza 300rs")
        bill = bill + 390

    if non == 3 and chi == 1:
        print("Small mutton barbeque ")
        bill = bill + 200
    elif non == 3 and chi == 2:
        print("Medium mutton pizza 150rs")
        bill = bill + 250
    elif non == 3 and chi == 3:
        print("Large mutton pizza")
        bill = bill + 350
    else:
        bill=bill

# vegitarian
elif a==2:
    veg= int(input("choose one of the following: 1.Vegetable pizza 2.onion pizza  3.veg loaded  "))
    vegs = int(input("choose one of the following: 1. small 100rs  2.medium 150rs 3.large 300rs "))

    if veg==1 and vegs==1:
        print(" Small vegetable pizza is 200rs ")
        bill=bill+200

    elif veg==1 and vegs==2:
        print(" medium vegetable pizza is 250")
        bill=bill+250

    elif veg==1 and vegs==3:
        print(" large vegetable pizza is 300")
        bill=bill+300

    if veg == 2 and vegs == 1:
        print(" Small onion  pizza is 200rs ")
        bill = bill + 200

    elif veg == 2 and vegs == 2:
        print(" medium onion  pizza is 250")
        bill = bill + 250

    elif veg == 2 and vegs == 3:
        print(" large onion pizza is 300")
        bill = bill + 300

    if veg == 3 and vegs == 1:
        print(" Small veg loaded pizza is 200rs ")
        bill = bill + 200

    elif veg == 3 and vegs == 2:
        print(" medium veg loaded  pizza is 250")
        bill = bill + 250

    elif veg == 3 and vegs == 3:
        print(" large veg loaded  pizza is 300")
        bill = bill + 300

s=print("your bill is ",bill)
print(s)









