import random

names = ["Yara","Parsa","Bahar","Nariman"]

def randomAgeGenerator():
    for name in names:
        print(name + ' ' + str(random.randint(1,100)))
    
randomAgeGenerator()
