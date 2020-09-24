from sys import exit
from textwrap import dedent
from random import randint

# global variables declaration
lives = 3
tag = False
found_key = False
room1_enter_has_been_called = False
room2_enter_has_been_called = False
room3_enter_has_been_called = False
check_picture_called_second_time = False


def life_count():
    global lives
    lives -= 1

    print("\nYOU LOST A LIFE!")
    print("YOU HAVE A TOTAL OF {} LIVES LEFT.\n".format(lives))


def separator():
    print("-"*60)

def sepause():
    print("Read above lines and Hit Enter!")
    input()
    separator()

class Info(object):

    def __init__(self):
        global lives
        print("\nWELCOME to FIND THE TREASURE game!")
        separator()
        print(dedent("""
            NOTE!!! If you want to totally get into the game, be patient
            with reading every word that appears on the screen. Otherwise
            you are just wasting your time!
            """))
        sepause()

        print(dedent("""
            NOTE!!! Options are provided within brackets for each question
            you are asked. You must choose among the options, matching every
            characters exactly. There would be an error otherwise.
            """))
        sepause()

        print(dedent("""
            hard_level => 3 lives
            easy_level => 5 lives
            """))
        choice = input("Which level do you want to play with?(hard/easy) > ")
        while choice != "hard" and choice != "easy":
            print("Invalid Input! Cannot Compute!")
            choice = input("Which level do you want to play?(hard/easy) > ")

        if choice == "easy":
            lives = 5
        else:
            pass

        print(dedent("""
            You found a map in the drawer of your GrandDad who
            recently died. The map seems to a Treasure map. You
            immediately start to follow the map. After two days
            of your travel following the map, you reach a departed
            house in the middle of a jungle. You enter the house
            and your TREASURE HUNTING game begins....
            """))
        sepause()

        print(dedent("""
            I am your guide in this game and I am pretty sure you
            won't be able to win it without me.
            """))

        print(dedent("""
            Some of the information, I provide here, might be useful.
            Read them.
            """))

        sepause()
        print(dedent("""
            1. You got {} lives.
            2. Each mistake you make cost a life.
            3. Be careful! The game will be encoded after you play it
                once and you won't be able to access it after your
                lives are over. I am just kidding ;)
            4. I have't any more information.
            """.format(lives)))

        print("\nPress ENTER to start GAME...")
        input("")
        separator()


class Scene(object):

    def enter(self):
        print("You will do things here.")
        print("These are later to be overwritten.")
        exit(1)

    def unlock_room(self):

        global lives
        print(dedent("""
            Shit! This door is password protected. The password, as
            far as it seems, is a 2-DIGIT number. You have 5 tries
            to make it right. I wish you brought plenty of luck with
            you today.
            """))


        code = f"{randint(1, 9)}{randint(1, 9)}"
        print("Enter code:")
        guess = input("> ")
        count = 0

        while guess != code and count < 4:
            print("WRONG CODE!")
            print("You have got {} tries left.".format(4-count))

            if count == 1:
                print(dedent("""
                    I want to pause the game here and talk to you
                    a little.
                    """))
                sepause()

                print(dedent("""
                    OK! I should not be doing this but I think its
                    a little bit hard on you. I can help you if
                    you want. But this is someone's mind playing
                    you and even if you accept my help it will cost
                    you something.
                    """))
                sepause()

                print(dedent("""
                    So listen. I will help you by providing first
                    digit of the code (REMEMBER! Only first digit!)
                    and in return you will have to offer me a life.
                    It seems pretty obvious to me that you are an
                    unlucky BASTARD and you are gonna lose a life
                    anyway. So it seems a pretty good deal to me.\n
                    """))

                choice = input("Do you accept the deal?(y/n) > ")
                while choice != "y" and choice != "n":
                    print("Invalid Input!")
                    choice = input("Do you accept the deal?(y/n) > ")

                if choice == "y":
                    if lives == 1:
                        print(dedent("""
                            Sorry! You have only one life remaining!
                            You'll be dead if you use it here. So I
                            can't help you at the moment.
                            """))
                        print("\n")

                        print("Enter the code:")
                        count += 1
                        guess = input("> ")

                        continue
                    else:
                        pass

                    life_count()
                    sepause()

                    print("The passcode is {}{}".format(code[0], code[1]))
                    print(dedent("""
                        Good luck Ahead! And please don't tell
                        anyone I helped you.
                        """))
                    print("\n")
                    print("Enter the passcode:")

                else:
                    print("OH! So you want to move on your own.")
                    print("Good for you! Anyway Good luck!")
                    print("\n")
                    print("Enter the passcode:")

            count += 1
            guess = input("> ")

        if guess == code:
            print("\n")
            print("Oh! you made it. You got the code right.\n")
            sepause()
            return "room"

        else:
            print("\nSorry Bud! You didn't get the code right.")

            life_count()

            if lives == 0:
                return "death"
            else:
                pass

            print("Now you're being taken to previous nearest scene.")
            sepause()

            return self.unlock_room()


class Hall(Scene):

    def user_choice(self):

        choice = input("Which room you would like to enter?(1/2/3) > ")

        if choice == "1" or " 1" in choice or "one" in choice:
            if room1_enter_has_been_called:
                print(dedent("""
                    You have previously entered this room and there
                    is nothing else to further inspect in this room.
                    So I am returning you back to the hall."""))
                sepause()
                return self.user_choice()
            else:
                print("\n")
                print("OK, Now you are entering Room1....")
                sepause()
                return "room_1"

        elif choice == "2" or " 2" in choice or "two" in choice:
            if room2_enter_has_been_called:
                print(dedent("""
                    You have previously entered this room! Would
                    you like to enter it again?(y/n)
                    """))

                choice = input("> ")
                while choice != "y" and choice != "n":
                    print("Invalid Input!")
                    choice = input("> ")

                if choice == "y":
                    if found_key:
                        print(dedent("""
                            You entered Room2 with the key and forwarded
                            towards the locked door to open it!
                            """))
                        sepause()
                        return "locked_room"

                    else:
                        print(dedent("""
                            Whaaat? You haven't found the key yet? You
                            might be losing hope. If you want to suicide
                            just tell me, OKAY? I'll help without hesitation!
                            """))

                        choice = input("Do you want to suicide?(y/n) > ")
                        while choice != "y" and choice != "n":
                            print("Invalid Input!")
                            choice = input("> ")

                        if choice == "y":
                            print("You suicide with despair! I feel sorry!")
                            print("You thought I was kidding huh? No, I wasn't!")
                            sepause()
                            return "death"
                        else:
                            pass

                        print(dedent("""
                            Okay! Then I am returning you back to hall.
                            And one thing don't return back until you've found
                            the key."""))

                        return self.user_choice()

                else:
                    return self.user_choice()

            else:
                return "room_2"


        elif choice == "3" or " 3" in choice or "three" in choice:
            if room3_enter_has_been_called:
                print("\n")
                print("Sorry you can't visit this room twice!")
                print("\n")
                return self.user_choice()

            else:
                print(dedent("""
                    Ok! I want to tell you something about Room3. I don't
                    know how they engineered but the door is designed such that
                    it can only be opened twice -- once for entering and once
                    for exiting -- so forget about re-entering the room! It can
                    only be visited once.
                    """))
                sepause()
                return "room_3"

        else:
            print("WRONG INPUT!")
            return self.user_choice()

    def enter(self):

        print("You enter THE HALL.")
        print(dedent("""
            Soon as you entered the hall, you can notice the
            following things.
            """))
        sepause()

        print(dedent("""
            1. A picture of Monalisa
            2. A picture of Krishna eating Makkhan.
            3. A television with a still picture of again a movie
                of Mahabharata with Krishna in it.
            4. There is a certificate of someone's achievement in
                counting similar pictures.
            5. Others are just furnitures and some regular stuff.
                Don't think there might be any clue there.
            """))
        sepause()

        print(dedent("""
            Now is the time to show your spy skills. There are total
            of three doors form the hallway. Be a detective and from above
            hints, figure out which room you would like to enter?
            """))

        return self.user_choice()



class Room1(Scene):

    def enter(self):

        global room1_enter_has_been_called
        room1_enter_has_been_called = True

        print("\nYou have opened the door and now you are in Room1.")
        print("You examine Room1 and gathered following informations:\n")
        sepause()

        print(dedent("""
            1. Room1 is another Bedroom.
            2. There is statue of Da Vinci holding a torch which is on.
            """))
        sepause()


        choice = input("Do you want to examine the statue further?(y/n) > ")
        while choice != "y" and choice != "n":
            print("Invalid Input!")
            choice = input("Do you want to examine the statue further?(y/n) > ")

        if choice == "y":
            print("\n")
            print("There is nothing more to be found around this statue.")
            print("There is no sign of anything here.\n")
            sepause()
        else:
            pass

        choice = input(dedent("""
                    Other things seem normal. Do you wish to continue
                    examining?(y/n)
                    > """))

        while choice != "y" and choice != "n":
            print("Invalid Input!")
            choice = input(dedent("""
                        Do you wish to continue examining?(y/n)
                        > """))

        if choice == "y":
            print("\n")
            print("3. There is a bed with clean bedsheet over it.")
            print("4. There is another teatable here.\n")
            sepause()
        else:
            pass

        print(dedent("""
            So, it turns out that this Room was not worth visiting and
            it merely was a waste of your time. But remember, you might
            need to revisit this room later. So it'll be better for
            you to memorize the informations you collected from this
            room.
            """))
        sepause()

        print(dedent("""
            There are two doors in this Room. One is which leads you
            to Room2 and another back to the hall. You can choose either
            to enter Room2 or to head back to the hall.
            """))

        choice = input("Which room do you like to enter?(hall/room2) > ")
        while choice != "hall" and choice != "room2":
            print("Invalid Input")
            choice = input("Which room do you like to enter?(hall/room2) > ")

        if choice == "hall":
            print("\n")
            print("You came back to the hall.")
            sepause()
            return Hall().user_choice()

        elif choice == "room2" and room2_enter_has_been_called:
            print(dedent("""
                You have previously entered this room! Would
                you like to enter it again?(y/n)
                """))
            choice = input("> ")
            while choice != "y" and choice != "n":
                print("Invalid Input!")
                choice = input("> ")

            if choice == "y":
                if found_key:
                    print(dedent("""
                        You entered Room2 with the key and forwarded
                        towards the locked door to open it!
                        """))
                    sepause()
                    return "locked_room"
                else:
                    print(dedent("""
                        Whaaat? You haven't found the key yet? You
                        might be losing hope. If you want to suicide
                        just tell me, OKAY? I'll help without hesitation!
                        """))
                    choice = input("Do you want to suicide?(y/n) > ")
                    while choice != "y" and choice != "n":
                        print("Invalid Input!")
                        choice = input("> ")

                    if choice == "y":
                        print("You suicide with despair! I feel sorry!")
                        print("You thought I was kidding huh? No, I wasn't!")
                        sepause()
                        return "death"

                    else:
                        pass

                    print(dedent("""
                        Search for the key and enter Room2. Without the key
                        there is no point in re-entering Room 2 and I won't
                        let you either coz I'll have to write extra codes
                        for this option and I don't want to! ;)
                        """))
                    sepause()
                    print("Now I am returning you back to the hall.")
                    sepause()

                    print("You're in the Hall.")
                    return Hall().user_choice()

            else:
                print("Ok! So, I am returning you back to the Hall then.")
                sepause()

                print("You're in the Hall.")
                return Hall().user_choice()

        else:
            val = self.unlock_room()
            if val == "room":
                return "room_2"
            else:
                return val


class Room2(Scene):


    def return_room1(self):
        if self.unlock_room() == "room":
            return "room_1"

    def enter(self):

        global room2_enter_has_been_called
        room2_enter_has_been_called = True

        print("OH! So you chose to enter Room2. Now you are here!")
        sepause()

        print(dedent("""
            These are the things you notice as soon as you enter
            the room:
            """))
        sepause()

        print(dedent("""
            1. Room2 seems to be a bedroom.
            2. The bedsheets are in a mess.
            3. There is a teatable and a lamp which is on.
            5. There is a door here labeled "Room1".
            4. There is another door here labeled "ROOM LOCKED".
            """))
        sepause()

        print(dedent("""
            To unlock the locked room, you will need to find the
            key.
            """))
        sepause()
        if found_key:
            print(dedent("""
                Looks like you have entered Room2 with the key
                so you forwarded towards the locked door to open it!
                """))
            sepause()
            return "locked_room"

        else:
            print(dedent("""
                There is no going back coz the door you came from
                is locked. So you will need to enter Room1. There is no
                other choice.
                """))
            sepause()

            print("Opening door to Room1.....")
            sepause()
            val = self.return_room1()

            if room1_enter_has_been_called:
                print("Now you are in Room1.")
                print(dedent("""
                    You have previously entered this room and there
                    is nothing else to further inspect in this room.
                    So I am returning you to the hall."""))
                sepause()

                print("You're in the Hall.")
                sepause()

                return Hall().user_choice()
            else:
                print("\n")
                print("OK, Now you are entering Room1....")
                sepause()
                return val



class Room3(Scene):

    def enter(self):
        global room3_enter_has_been_called
        room3_enter_has_been_called = True

        print("You notice following things soon you entered Room3:\n")
        sepause()

        print(dedent("""
            1. It's a Kitchen Room.
            2. There is a TV playing an advertisement of tea leaves.
                Can't tell about you but it seems corny to me.
            """))

        def examine_TV():
            global found_key
            global lives

            choice = input("Do you wish to examine the TV box?(y/n) > ")
            while choice != "y" and choice != "n":
                print("Invalid Input!")
                choice = input("Do you wish to examine the TV box?(y/n) > ")

            if choice == "y":
                print(dedent("""
                    This TV is damn heavy. It will cost you a life to
                    displace it from its position and examine it.
                    """))

                choice1 = input("Do you still want to examine?(y/n) > ")
                while choice1 != "y" and choice1 != "n":
                    print("Invalid Input!")
                    choice1 = input("Do you want to examine?(y/n) > ")

                if choice1 == "y":
                    life_count()
                    if lives == 0:
                        return "death"
                    sepause()

                    print(dedent("""
                        You have removed the TV from its position and
                        now you can see various items that were hidden
                        in the TV box. If you have read every word from
                        the start, you are more like to figure out which
                        item to examine.
                        1. A tea cup
                        2. A shoe box
                        3. A vase
                        """))

                    choice2 = input(dedent("""
                                Which item would you like to examine?
                                (1/2/3) > """))
                    while choice2 != "1" and choice2 != "2" and choice2 != "3":
                        print("Invalid Input!")
                        choice2 = input(dedent("""
                                    Which item would you like to examine?
                                    (1/2/3) > """))

                    if choice2 == "1":
                        print(dedent("""
                            CONGRATULATIONS! The key was in the tea cup
                            and you've found it. Now I'll return you back
                            to Hall.
                            """))
                        sepause()
                        print("You're in the Hall.")
                        found_key = True
                        val = Hall().user_choice()
                        return val

                    elif choice2 == "2":
                        print(dedent("""
                            You insert your hand inside the shoe box to
                            search for the key. Instead, there was a scorpion
                            inside the box which stings you at an instant.
                            The poison was so powerful that it took all your
                            remaining lives away and you die!
                            """))
                        sepause()
                        return "death"

                    else:
                        print(dedent("""
                            You wanted to check the vase for the key. So,
                            you insert your hand inside. But shit! There
                            was a Black Mamba sleeping inside there whose
                            sweet dreams you just disturbed. Furiously, the
                            mamba bites you and inject all of its poison
                            inside you. You die at an instant, regardless of
                            your remaining lives.
                            """))
                        sepause()
                        return "death"

                else:
                    print("\n")

            else:
                print("\n")

        val = examine_TV()

        if not val:
            print("3. There is a pot in a corner of the room.\n")
            choice = input("Do you want to check inside the pot?(y/n) > ")

            while choice != "y" and choice != "n":
                print("Invalid Input!")
                choice = input("Do you want to check inside the pot?(y/n) > ")

            if choice == "y":
                print(dedent("""
                    You insert your hand inside the pot inorder to
                    search for the key. Instead, there was a scorpion
                    inside the pot which stings you at an instant.
                    The poison was so powerful that it took all your
                    remaining lives away and you die!
                    """))
                sepause()
                return "death"

            else:
                print(dedent("""
                    All of your desire to find the treasure went in vain
                    coz you couldn't find the key to the locked room. You
                    die of despair.
                    """))
                sepause()
                return "death"

        else:
            return val


class LockedRoom(Scene):

    def enter(self):

        global check_picture_called_second_time
        print(dedent("""
            You insert the key in the keyhole of lock and slowly push
            the door. The door screeches and moves making 'grrrrrrr'
            sound. There is entire darkness.
            """))
        sepause()

        print("\nBOOM! You're DEAD!\n")
        sepause()

        print(dedent("""
            I'm just kidding! You're not dead yet. Be careful! You
            might find something amazing inside this room but I can
            be certain that this room is emmiting EVIL aura. It makes
            you chilling down to your bones.
            """))
        sepause()

        print(dedent("""
            The light inside is very dim. You can hardly notice anything
            inside. After streching you eyes for a minute or two you
            start to notice following things inside the room:
            """))
        sepause()

        print(dedent("""
            1. Skulls all over. F**k! This room must have been closed for
                decades.
            2. Whaaaaat? There's another picture of Monalisa here. Is it
                just a mere coincidence?
                """))
        sepause()

        print(dedent("""
            Do you want to examine the picture? I am not sure but it might
            cost you a life rather worse you might even die. Who knows a
            ghost might pop up and start to chase you. I don't know anything
            about this room. Trust me I haven't felt this useless in my
            whole life. So I'd suggest not to check but rest is up to you.
            """))
        sepause()

        def check_picture():

            global tag
            choice = input("Check?(y/n) > ")

            if choice == "y":
                print(dedent("""
                    The picture is tightly screwed to the wall. You remove
                    the picture by force and see a key in the hole, the
                    hole hidden by the picture. Seems like you made a right
                    decision -- you are not dead yet -- that proves it.
                    """))
                sepause()

                if not check_picture_called_second_time:
                    print(dedent("""
                        But wait! A key? A key for what? There is nothing
                        to be unlocked, not yet! Forget it! You found the
                        key - you keep it in the pocket - who cares?
                        """))
                    sepause()
                else:
                    pass

                tag = not tag

            elif choice == "n":
                pass

            else:
                print("Invalid Input!")
                return check_picture()

        check_picture()

        print(dedent("""
            3. I see a box like structure at the corner. HOLY SHIT! It's
                a 'tamate box'. Oh Sorry! You don't know what that means
                do you?
            """))
        sepause()
        print("It's a TREASURE box, you dumbass!")

        def take_gold():

            print(dedent("""
                And say what you've already found the key! You lucky
                bastard! Go on open the TAMATE BOX.
                """))

            input("Hit Enter to Open the BOX...")
            print(dedent("""
                Oh shit! shit! shit! Its sparkling man! The box! Its
                full man. Its full of this shiny gold. You're rich. MF!
                You're totally rich!
                """))
            sepause()

            print(dedent("""
                Roughly I can estimate there might be nearly 30 kg of
                gold. There is also a gold-written note inside the box.
                It says "Please leave some for your predecessors!". I
                suggest you to take only half of the gold. That would
                be better. If you take all, who will I guide to this
                room later?
                """))

            # Initialize choice to any number not in range (0, 30).
            choice = 100
            index = True

            while index or choice not in range(0, 30):
                try:
                    choice = int(input(dedent("""
                        How much do you want to take(0-30kg)? > """)))
                    if choice not in range(0, 30):
                        print("Invalid Input! Out of Range.")
                    index = False
                except ValueError:
                    print("Please enter an integer input!")

            if choice <= 15:
                print("\n")
                print("You are pretty generous you know.")
                sepause()

                print("CONGRATULATIONS! CONGRATULATIONS!")
                print(dedent("""
                    You WIN the game! You can take the treasure
                    with you now!
                    """))
                sepause()

                print("Again: CONGRATULATIONS! CONGRATULATIONS!")
                print("C ya later!")
                sepause()

                return "finished"

            else:
                print("You are greedy! You bastard!")
                sepause()

                print(dedent("""
                    A huge rock fall from nowhere upon your head
                    crushing your head to a shape of pizza! You
                    should have gone with my suggestion! This must've
                    been a trap set up by the treasure-keeper to kill
                    the greedy bastards trying to take his treasure.
                    """))
                return "death"


        if tag:
            val = take_gold()
            return val

        else:
            print(dedent("""
                Well you're Lucky I say. But that box is locked damnit.
                Where is the key?
                """))
            sepause()

            print(dedent("""
                Well I would suggest again to go through all things you
                noticed in the room. And answer next question briefly.
                """))

            answer = input("What would you like to do now?\n> ")

            if "monalisa" in answer or "Monalisa" in answer:
                check_picture_called_second_time = True
                print("So you want to check the Monalisa picture huh?")
                check_picture()
                val = take_gold()
                return val

            else:
                print(dedent("""
                    You kept roaming around the Room searching for the
                    key. The door to leave the room also won't open unless
                    you've opened the box. Its--either you leave rich or
                    you die--sort of case.
                    """))
                sepause()

                print(dedent("""
                    You came so close to the treasure. Its been 3 years now
                    and you are one among those skulls! Someone enters the
                    room in three years looking the same treasure for which
                    you died.
                    """))
                sepause()

                print(dedent("""
                    OK! Thats just a fancy way to say that in present, you're
                    DEAD!
                    """))

                sepause()
                return "death"

class Finished(Scene):

    def enter(self):
        exit(1)


class Death(Scene):

    def __init__(self):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your Mom would be proud...if she were smarter.",
            "Such a loser.",
            "I have a small puppy that's better at this.",
            "You're worse than your Dad's jokes."
            ]

    def enter(self):
        print("{}".format(self.quips[randint(0,4)]))
        return "finished"


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        last_scene = self.scene_map.next_scene("finished")
        current_scene = self.scene_map.current_scene()

        while current_scene != last_scene:
            current_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(current_scene_name)


class Map(object):

    scenes = {
        "hall": Hall(),
        "room_1": Room1(),
        "room_2": Room2(),
        "room_3": Room3(),
        "locked_room": LockedRoom(),
        "death": Death(),
        "finished": Finished(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, current_scene):
        val = self.scenes.get(current_scene)
        return val

    def current_scene(self):
        return self.next_scene(self.start_scene)


print_info = Info()
map = Map("hall")
game_play = Engine(map)
game_play.play()
