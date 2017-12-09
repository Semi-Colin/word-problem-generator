import random;
namesMale = ["George","Joe","Harold","Bob","Luis","Luke","Jackson","Ethan","Jason","Jack","Noah","Jayden"]; #List of male names to be chosen randomly
namesFemale = ["Clarissa","Maria","Olivia","Emma","Ava","Isabella","Riley","Charlotte","Audrey","Lily","Chloe","Evelyn"]; #List of female names to be chosen randomly
objects = ["bottle caps","stamps","dog treats","apples","coins"]; #List of objects to be given or taken
objectp = ""; #INIT
name1 = ""; #INIT
name2 = ""; #INIT
name1Gender = 0; #INIT
name2Gender = 0; #INIT
number1 = 0; #INIT
number2 = 0; #INIT


def newName():  #Create new name for either subject1 or subject2

        gender = random.randrange(0,2); #Choose random gender for subject1, boy if 0, girl if 1

        if gender == 0:  #Choose name for subject1
            name = namesMale[random.randrange(0,len(namesMale))];
        else:
            name = namesFemale[random.randrange(0,len(namesFemale))];
            
        return name;

while True:  #Main Loop
    name1 = newName(); #Get name of subject1
    name2 = newName(); #Get name of subject2

    objectp = objects[random.randrange(0,len(objects))];

    number1 = str(random.randrange(8,23)); #Pick a random number
    number2 = str(random.randrange(10,22)); #Pick a random number

    if name1 in namesMale:
        name1Gender = "him";
    else:
        name1Gender = "her";
        
    if name2 in namesMale:
        name2Gender = "him";
    else:
        name2Gender = "her";
    
    input(name1 + " had " + number1 + " " + objectp + ". Then " + name2 + " gave " +name1Gender + " " + number2 + " more. How many " + objectp + " does " + name1 + " have now?");


