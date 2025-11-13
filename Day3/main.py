# Day 3 - Control Flow and Logical Operators
# Day 3 - Project: Enchanted Forest - THE GAME

print(''' 
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\ 
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \ 
                   /      ,               \,-`\`_,-`\_,..--'\ 
                  ,`    ,/,              ,>,   )     \--`````\ 
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \ 
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo
''')
print("One of more of your adventures brought you to magical, calm forest. After walking for few hours, you got really tired and goes to sleep")
print("Suddenly, terrible roar wakes you up. You open your eyes and see big ogre with a mallet in his hand looking at you like hungry man looks at the sandwich.")
print("Without hesitation you start to run, but you don't remember from where you have come. You run straight by path.")
direction = input("The path divides into two. To turn left and go to the river type 'left', to turn right and go deeper to the forest type 'right'.\n")
if direction == "left" or direction == "Left":
    print("You turned left to reach the river. Maybe you will lose the chase on the other side.")
    print("You reach the river and look around, there is an old bridge full of holes and parked boat on the shore.")
    river_crossing = input("To go through bridge type 'bridge', to take a boat type 'boat'.\n")
    if river_crossing == "bridge" or river_crossing == "Bridge":
        print("Without any more hesitation you took your chance with a bridge. You managed to jump over each hole and reach the other side. The ogre is swimming after you")
    elif river_crossing == "boat" or river_crossing == "Boat":
        print("You reached the boat and noticed that it's full of holes, too late to go through bridge now. Ogre caught you! GAME OVER")
    else:
        print("error - wrong crossing method")
elif direction == "right" or direction == "Right":
    print("You turned right and run deeper into the forest, maybe you have lost the ogr, but you never found way home. GAME OVER")
else:
    print("error - direction not recognized")




# Day 3 examples and exercises
# Checking if number is even or odd
# number = int(input("What is you number? "))
# if number % 2 == 0:
    # print(f"Number {number} is even!")
# else:
    # print(f"Number {number} is odd!")
# print("Welcome to Python Pizza Deliveries! ")
# bill = 0
# size = input("What size pizza do you want? (S, M, L) ")
# pepperoni = input("Do you want pepperoni on your pizza? (Y or N) ")
# extra_cheese = input("Do you want extra cheese? (Y or N) ")
# 
# if size == "S":
    # bill += 15
    # print("Small pizza chosen")
# elif size == "M":
    # bill += 20
    # print("Medium pizza chosen")
# elif size == "L":
    # bill += 25
    # print("Large pizza chosen")
# else:
    # print("Error - start all over again!")
# 
# if pepperoni == "Y":
    # if size == "S":
        # bill += 2
    # else:
        # bill += 3
# 
# if extra_cheese == "Y":
    # bill += 1
# print(f"Your bill is: ${bill}")
