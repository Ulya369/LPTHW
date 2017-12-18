import ex45_module
from sys import exit

def using_external_file():
    ex45_module.make_fun()


# ------------------INHERITANCE.Parent class----------
class Room_Father(object):
    def welcome(self):
        print "..........father: welcome message"
    def goodbye(self):
        print "......father: goodbye message"

# ------------------INHERITANCE.Child classes---------
# class 0
class Room_0(Room_Father):
    def enter(self):
        print "\n||||||||||||||||||||||||||||||||||||||||||"
        print ":::::::::::::room-0 is here:::::::::::::"
        super(Room_0, self).welcome()
        print "..............kid: room_0's personal message"
        print "how many countries in the world, roughly ?"
        userInput = input()
        if userInput > 150 and userInput <300:
            print "::::::::::::: Ok, '%d' is good answer!. Next room is Room_1" % userInput
            return 1
        else:
            print "::::::::::::: No, '%d' is very bad answer! YOU LOST THE GAME" % userInput
            return 'lose'

# class 1
class Room_1(Room_Father):

    def enter(self):
        print "\n||||||||||||||||||||||||||||||||||||||||||"
        print ":::::::::::::room-1 is here:::::::::::::"
        super(Room_1, self).welcome()
        print "............kid: room_1's personal message"
        print "how many stars in the galaxy ?"
        userInput = input()
        if userInput > 100000000:
            print "::::::::::::: Ok, '%d' is good answer!. Next room is Room_2" % userInput
            return 2
        else:
            print "::::::::::::: No, '%d' is very bad answer! YOU LOST THE GAME" % userInput
            return 'lose'

# class 2
class Room_2(Room_Father):

    def enter(self):
        print "\n||||||||||||||||||||||||||||||||||||||||||"
        print ":::::::::::::room-2 is here:::::::::::::"
        super(Room_2, self).welcome()
        print "............kid: room_2's personal message"
        print "how many moons orbiting earth ?"
        userInput = input()
        if userInput == 1:
            print "::::::::::::: Ok, '%d' is good answer!. Next room is Room_3" % userInput
            return 3
        else:
            print "::::::::::::: No, '%d' is very bad answer! YOU LOST THE GAME" % userInput
            return 'lose'

# class 3
class Room_3(Room_Father):

    def enter(self):
        print "\n||||||||||||||||||||||||||||||||||||||||||"
        print ":::::::::::::room-3 is here:::::::::::::"
        super(Room_3, self).welcome()
        print "............kid: room_3's personal message"
        print "what is population of Germany ?"
        userInput = input()
        if userInput > 65000000 and userInput <100000000:
            print "::::::::::::: Ok, '%d' is good answer!. Next room is Room_4" % userInput
            return 4
        else:
            print "::::::::::::: No, '%d' is very bad answer! YOU LOST THE GAME" % userInput
            return 'lose'


# class 4
class Room_4(Room_Father):

    def enter(self):
        print "\n||||||||||||||||||||||||||||||||||||||||||"
        print ":::::::::::::room-4 is here:::::::::::::"
        super(Room_4, self).welcome()
        print "............kid: room_4's personal message"
        print "how much money you have ?"
        userInput = input()
        if userInput > 100000:
            print "::::::::::::: Ok, '%d' is good amount of money!. Next room is Winner's room" % userInput
            return 'win'
        else:
            print "::::::::::::: No, '%d' is very bad answer! YOU LOST THE GAME" % userInput
            return 'lose'

# class 5
class Room_win(Room_Father):

    def enter(self):
        print "\n\n\n____________________________________________________."
        using_external_file()
        print "----------------------------------------------------*"



        exit(1)


# class 6
class Room_lose(Room_Father):

    def enter(self):
        print "\n\n\n___________________________________________________."
        ex45_module.dont_make_fun()
        print "---------------------------------------------------*"


        exit(1)



# ----------------------Main-------------------
class Main(object):

    rooms = {0: Room_0(),
             1: Room_1(),
             2: Room_2(),
             3: Room_3(),
             4: Room_4(),
             'win': Room_win(),
             'lose': Room_lose()
             }
    print "***************************************************"
    print "*******************...STARTING...******************"
    print "****************************************************\n"*3
    temp = rooms[0]
    while True:
        return_value = temp.enter()
        temp = rooms[return_value]
