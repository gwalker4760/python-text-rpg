from playsound import playsound
from time import sleep
import logging
logging.basicConfig(filename='user_log.log', filemode='w', level=logging.INFO)

def beginning_of_game():
    global name
    name = input("Who are you? ")
    logging.info("User input name")
    start = input(f'Hello {name} would you like to play the game? (yes / no) ')
    if start == "yes":
        logging.info('User chose to play the game')
        print("You're walking down a stright road")
        sleep(1)
        path()
    elif start == "no":
        print("That's to bad")
        sleep(1)
        logging.info("Game has ended")
        exit()
    else:
        print("I didn't catch you, can you repeat that?")
        sleep(1)
        beginning_of_game()


def path():
    direction = input("Would you like to go left or right? ")
    if direction == "left":
        print("You went on your merry way down the road on the left and tripped on a twig! Game Over.")
        sleep(1)
        play_again()
    elif direction == "right":
        print('Great choice {name} you survived!')
        # sleep(1)
        second_path()
    elif direction == "up":
        print("You feel the need to defy the laws of the universe and will not be limited to such foolish things. You choose your own your own path so you call for no your trusty steed Buttstallion. The a ray of sunshine beams next to you, as you see your trusted companion decend from the heavens. You hop and ride off into the distance never to be seen again. All the evil in the world suddenly vanished as if it never existed. You win the game.")
        sleep(5)
        play_again()
    else:
        print("You wanna do what now?")
        sleep(1)
        path()


def second_path():
    sleep(1)
    direction = input("Now would you like to go up or down? ")
    if direction == "up":
        print(f'Quick {name}! Your absurd decision some how got us in Cloud City and that bounty hunter is headed toward you? You can either hide in this closet next you that says "occupied" or fight him head on! What are you gonna do?')
        hide_or_fight()
    elif direction == "down":
        print('')
    else:
        print("You wanna do what now?")
        sleep(1)
        second_path()


def hide_or_fight():
    sleep(1)
    choice = input(
        'Hide in closet that says "occupied" / Fight the Bounty Hunter (hide / fight) ')
    if choice == "hide":
        hide()
    elif choice == "fight":
        fight()
    else:
        print("You wanna do what now?")
        sleep(1)
        hide_or_fight()


def hide():
    print("Of course! The Bounty Hunter obviously hasn't spotted you yet. Hurry up and get in that closet. You frantically rush into the closet and immediately run into something. This something can speak as it yelled 'Hey give me some room here!' You freak out and feel the walls for a light switch. You find the light and turn it on and you will not believe what you see before your very eyes. It's Solo Han and Chewbacco both half dressed in stormtrooper armor that they stole off of a couple of unconscious guys in the corner. You can't help but fangirl over them and exposed your new hiding spot. The Bounty Hunter opens the door and catches all three of you. Now thanks to you there never was a new triology featuring Adam Driver as Kylo Ren aka Ben Solo. I hope you can sleep at night I'm done with you!")
    sleep(5)
    check_point()


def fight():
    print("You really wanna fight him? This guy is a fan favorite among a lot of Star Wars fans AND he's capable of defeating Jedi, so you will not be much a challenge for him! You really wanna fight him huh? Alrighty then your funeral I gonna be smart and get on outa here. Morgan Freeman ain't gonna support my family.")
    sleep(20)
    print("(Que Morgan Freeman voice over) You were left alone to fight against Boba Fett, and obviously you aren't gonna beat him alone if fact you died immediately, but hey you died in combat which means you have earned yourself a spot in Valhalla. I would say your a lucky man. Game Over.")
    playsound("./sound.mp3")
    sleep(1)
    check_point()


def play_again():
    restart = input("Would you like play to again? (yes / no)")
    if restart == "yes":
        beginning_of_game()
    elif restart == "no":
        print("That's too bad")
        logging.info("Game has ended")
        exit()
    else:
        print("You wanna do what now?")
        sleep(1)
        play_again()


def check_point():
    restart = input('Would you like to play again? (yes / no) ')
    if restart == 'yes':
        check_point_spawn()

    elif restart == "no":
        print("That's too bad")
        logging.info("Game has ended")
        exit()

    else:
        print("You wanna do what now?")
        sleep(1)
        check_point()


def check_point_spawn():
    spawn = input(
        'Where would you like to start at? (up / down) (hide / fight) ')
    if spawn == "up" or spawn == "down":
        second_path()
    # elif spawn == "down":
    #     second_path()
    elif spawn == "hide" or spawn == "fight":
        hide_or_fight()
    # elif spawn == "fight":
    #     hide_or_fight()
    else:
        print("You wanna do what now?")
        sleep(1)
        check_point_spawn()


beginning_of_game()
logging.info("Game has ended")
# fight()