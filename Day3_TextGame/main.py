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
print("Welcome to THE ENCHANTED FOREST")
print("")
print("One of your many adventures has brought you to a magical, peaceful forest. After walking for a few hours, you grow tired and fall asleep.")
print("Suddenly, a terrible roar wakes you up. You open your eyes and see a huge ogre with a mallet in his hand, "
      "looking at you the way a hungry man looks at a sandwich.")
print("Without hesitation, you start running, but you don't remember which way you came from. You dash straight ahead along the path.")
direction = input("The path splits in two. To turn left and head toward the river, type 'left'.\n"
                  "To turn right and go deeper into the forest, type 'right'.\n").lower()
if direction == "left":
    print("You turn left toward the river. Maybe you can lose the ogre on the other side.")
    print("You reach the river and look around. There's an old bridge full of holes, and a small boat moored to the shore.")
    river_crossing = input("To cross the bridge, type 'bridge'.\n"
                           "To take the boat, type 'boat'.\n").lower()
    if river_crossing == "bridge":
        print("Without hesitation, you take your chances with the bridge. You manage to jump over each hole and reach the other side. "
              "The ogre is swimming after you!")
        print("You're still not safe. You have only a few minutes to hide before the monster catches up. "
              "Ahead lies a field of wheat with a big tree, a scarecrow, and a few bundles of hay.")
        print("You look around and spot some potential hiding places.")
        hiding_spot = input("To climb the tall tree and hide among its leaves, type 'tree'.\n"
                            "To take the old clothes from the scarecrow, dress like one, and stand in the field, type 'scarecrow'.\n"
                            "To hide in one of the hay bundles, type 'hay'.\n").lower()
        if hiding_spot == "scarecrow":
            print("You put on the ragged clothes and stand in the field, pretending to be a scarecrow. The ogre searches every bundle of hay.")
            print("You remain undiscovered. You survive! After waiting a few more minutes to be sure, "
                  "you walk toward an old farmhouse at the edge of the field. The farmer shows you the way home.")
            print("Congratulations, YOU WON!!!")
        elif hiding_spot == "tree":
            print("You climb the tree as fast as you can, but unfortunately, one of the branches snaps under your weight. "
                  "You fall right into the ogre's huge hands.")
            print("GAME OVER")
        elif hiding_spot == "hay":
            print("You dive into the biggest bundle of hay and hold your breath, trying not to make a sound. What were you thinking? "
                  "That's the first place the ogre checks. You've been found.")
            print("GAME OVER")
        else:
            print("It took you too long to decide, Ogre cought you!")
            print("GAME OVER")
    elif river_crossing == "boat":
        print("You reach the boat and notice too late that it's full of holes. The ogre catches you before you can escape!")
        print("GAME OVER")
    else:
        print("It took you too long to decide, Ogre cought you!")
        print("GAME OVER")
elif direction == "right":
    print("You turn right and run deeper into the forest. Maybe you've lost the ogre... but you never find your way home.")
    print("GAME OVER")
else:
    print("It took you too long to decide, Ogre cought you!")
    print("GAME OVER")





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
