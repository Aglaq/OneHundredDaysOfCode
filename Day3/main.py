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
print("One of more of your adventures brought you to the magical, calm forest. After walking for few hours, you got really tired and goes to sleep")
print("Suddenly, terrible roar wakes you up. You open your eyes and see big ogre with a mallet in his hand looking at you like hungry man looks at the sandwich.")
print("Without hesitation you start to run, but you don't remember from where you have come. You run straight by path.")
direction = input("The path divides into two. To turn left and go to the river type 'left', to turn right and go deeper to the forest type 'right'.\n")
if direction == "left" or direction == "Left":
    print("You turned left to reach the river. Maybe you will lose the chase on the other side.")
    print("You reach the river and look around, there is an old bridge full of holes and parked boat on the shore.")
    river_crossing = input("To go through bridge type 'bridge', to take a boat type 'boat'.\n")
    if river_crossing == "bridge" or river_crossing == "Bridge":
        print("Without any more hesitation you took your chance with a bridge. You managed to jump over each hole and reach the other side. The ogre is swimming after you")
        print("You still aren't safe. You have few minutes to hide and wait for monster to go away. There is field of wheat with the big tree, scarecrow and few bundles of hay.")
        print("You look around and see some places to hide.")
        hiding_spot = input("To climb very tall tree and hide between it's leaves type 'tree'. To take old cloth from scarecrow, dress as one and hide on the field type 'scarecrow'. To hide in one of bundles of hay type 'hay'.\n")
        if hiding_spot == "scarecrow" or hiding_spot == "Scarecrow":
            print("You took old rags and stand on the fiels pretending to be scarecrow. Ogre came, checked every bundle of hay.")
            print("You weren't found. You survived. You waited few more minutes just to be sure. You reached old house in the end of the field. Farmer showed you way home.")
            print("Congratulations, YOU WON!!!")
        elif hiding_spot == "tree" or hiding_spot == "Tree":
            print("You reach the tree and starts climbing. Unfortunatelly, one of the branches broke under your weight. You felt right into big hands of the ogre.")
            print("GAME OVER")
        elif hiding_spot == "hay" or hiding_spot == "Hay":
            print("You jump into biggest bundle of hay and hold your breath to not make any sound. What were you thinking? That's the first place where ogre looked. You've been found.")
            print("GAME OVER")
        else:
            print("error - unrecognized hiding spot")
    elif river_crossing == "boat" or river_crossing == "Boat":
        print("You reached the boat and noticed that it's full of holes, too late to go through bridge now. Ogre caught you!")
        print("GAME OVER")
    else:
        print("error - wrong crossing method")
elif direction == "right" or direction == "Right":
    print("You turned right and run deeper into the forest, maybe you have lost the ogre, but you never found way home.")
    print("GAME OVER")
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
