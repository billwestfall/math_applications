import time
import sys
import random
#####
class Player:

    def __init__(self, name):
        self.name = name
        self.money = 0
###############################
        self.health = 100
        self.water = 100
        self.food = 100
###############################
        pass


p = Player("Player")




class emblem:

    def __init__(self,name):
        self.name = name
        self.emblem = 0
        pass

begemb = emblem("Begger Emblem")
apart = emblem("Apartment Key")
college = emblem("College emb")

admin = emblem("Admin Emblem")

class Job:

    def __init__(self, name, requirements, pay):
        self.name = name
        self.requirements = requirements
        self.pay = pay
        pass
beg = Job("Begging", 0, 10)
jojo = Job("Fast Food", 0, 100) #requires apartment emblem


class foo:

    def __init__(self, name, price, fill):
        self.name = name
        self.price = price
        self.fill = fill
        pass
dai = foo("Daily Set of Essentials", 30, 100)   ##decrease of 10 per day for


#upkeep



def stats():
    p.water -= 10
    p.food -= 10
    print("Food:")
    print(p.food)
    print("Water:")
    print(p.water)
    if p.water == 0:
        print("Game Over")
        sys.exit()
    else:
        print("Money:")
        print p.money
        cycle()

def cycle():
    if apart.emblem == 1:
        print("1.) Store")
        print("2.) To The Day")
        print("3.) School")
        cyclea = input("")
        if cyclea == 1:
            store()
        elif cyclea == 2:
            job()
        elif cyclea == 3:
            school()
    else:
        print("1.) Store")
        print("2.) To The Day")
        cycle = input("")
        if cycle == 1:
            store()
        if cycle == 2:
            job()

def stores():
    store()

def store():
    print("1.) +100 Health, 100 Water, 100 Food. (30$)")
    print("2.) Apartment Key (300$)")
    print("3.) Back")
    store = input("")
    if store == 1:
        p.money -= 30
        p.health += 100
        p.water += 100
        p.food += 100
        print("+100 Health")
        print("+100 Water")
        print("+100 Food")
        stores()
    elif store == 2:
        apart.emblem += 1
        stores()
    elif store == 3:
        cycle()
    elif store == 887324:
        admin.emblem += 1
        stores()

def job():
    if college.emblem == 1:
        print("You are eligible for:")
        print("1.) Begging / Pay: 10")
        print("2.) Working in fast food restuarant / Pay: 100")
        print("3.) Working in office / Pay: 1000")
        print("4.) Working in institution / Pay: 3500")
        cme = input("")
        if cme == 1:
            p.money += 10
            stats()
        elif cme == 2:
            p.money += 100
            stats()
        elif cme == 3:
            p.money += 1000
            stats()
        elif cme == 4:
            p.money += 3500
            stats()


    elif high.emblem == 1:
        print("You are eligible for:")
        print("1.) Begging / Pay: 10")
        print("2.) Working in fast food restuarant / Pay: 100")
        print("3.) Working in office / Pay: 1000")
        highme = input("")
        if highme == 1:
            p.money += 10
            stats()
        elif highme == 2:
            p.money += 100
            stats()
        elif highme == 3:
            p.money += 1000
            stats()



    elif apart.emblem == 1:
        print("You are eligible for:")
        print ("1.) Begging / Pay: 10")
        print("2.) Working In Fast Food Restuarant / Pay: 100")
        job = input("")
        if job == 1:
            p.money += 10
            stats()
        if job == 2:
            p.money += 100
            stats()
    else:
        print("You are eligible for:")
        print("1.) Begging / Pay: 10")
        job1 = input("")
        if job1 == 1:
            p.money += 10
            stats()
high = emblem("High School Graduate")

def schools():
    school()

def school():
    if high.emblem == 1:
        print("1.) College / 5000")
        print("2.) Back")
        papi = input("")
        if papi == 1:
            college.emblem += 1
            schools()
        elif papi == 2:
            cycle()



    elif admin.emblem == 1:
        print("1.) Admin School / FREE")
        adme = input("")
        if adme == 1:
            high.emblem += 1
            cycle()
    else:
        print("1.) High School / 1000")
        print("2.) Back")
        schoolme = input("")
        if schoolme == 1:
            p.money -= 1000
            high.emblem += 1
            schools()
        elif schoolme == 2:
            cycle()


def day():
    print("")














stats()
