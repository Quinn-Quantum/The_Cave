#Text -Base Adventure Game:'The Cave'

import time     #module to add a pause

#Figuring out how users might respond

answer_A=["A","a"]
answer_B=["B","b"]
answer_C=["C","c"]

#Grabbing objects
sword=0
toothe=0
chein=0

requiered = ("\nUse only A,B or C") #Cutting down on duplication

#intro
def intro ():
    print("You have a crippled dream. You wake up in the moment\n"
          "you fall in a black hole. You breath heavliy and register that you\n"
          "are in a dark room. Alary eye opens further back in the room. It looks in your\n"
          "direction. A second eye oppears. Some come closer. You will: \n")
    time.sleep(1)
    print("A. Grab a nearby rock and throw it at the eye of the monster\n"
          "B. Lie down and wait to be mauled\n"
          "C. Run to the right sid\n")
    choice=input (">>>  ") # Here is youe first choice
    if choice in answer_A:
        option_rock ()
    elif choice in answer_B:
        print ("\nWelp, that was quick\n"
               "\n\nYou died! Good night!")
        time.sleep(1)
        print (requiered)
        intro ()

    elif choice in answer_C:
        option_run_right ()
    else:
        print (requiered)
        intro ()

def option_rock ():
    print("\nThe monster is stunned, but regains control.\n"
          "He begins moving towards you agein. You will: \n")
    time.sleep(1)
    print("A. Run to the right side\n"
          "B. Throw another rock\n"
          "C. Run to the left sid")
    choice=input(">>>  ")
    if choice in answer_A:
        option_run_right ()
    elif choice in answer_B:
        print("\n You decided to throw antother rock,as\n"
              "if the first rock thrown did much damage. The rock\n"
              "flew well over the monster head. You missed.\n"
              "\n\n You died! Good night!?n")
        time.sleep(1)
        print (requiered)
        intro ()
    elif choice in answer_C:
            print("\nYou run to the left side, when something\n"
                  "big and heavy hits you. \n"
                  "\n\nYou died! Good night!\n")
            time.sleep(1)
            print (requiered)
            intro ()
    else:
        print (requiered)
        intro ()

def option_run_right ():
    print("\n You run to the right side and concead behind a rock.\n"
          "Besides that you feel something cold and smooth. It is a sword.\n"
          "You will: \n")
    time.sleep(1)
    print ("A. pick up the sword\n"
           "B. do not pick up the sword\n")
    choice=input(">>>  ")
    if choice in answer_A:
        sword=1     #add a sword
    else:
            sword=0
    print("\n What do yo do nexst?\n")
    time.sleep (1)
    print("A. Hide in silence\n"
         "B. Fight\n"
          "C. Run\n")
    choice = input(">>>  ")
    if choice in answer_A:
        print ("\nReally? You think the monster do not know where\n"
               "you hide. So short you died! Good night!\n")
        time.sleep(1)
        print (requiered)
        intro ()
    elif choice  in  answer_B:
        if sword >0:
            print ("\nYou run towards the monser and feel\n"
                   "how the sword leads you. It helps you to kill\n"
                   "the monster. It drop a tooth and a chein.\n"
                   "You will: ")
            time.sleep(1)
            print("A. pick the tooth\n"
                  "B. pick the chein\n")
            choice=input(">>>  ")
            if choice in answer_A:
                tooth=1
                option_win()
            elif choice in answer_B:
                chain=1
                option_win()
            else:
                option_win()
        else: #if the user didn`t grab the sword
            print ("\nYou should have pick up that sword.\n"
                   "you`re defenseless.\n\nYou died! Good night!\n")
            time.sleep(1)
            print (requiered)
            intro ()
    elif choice in answer_C:
        print("\nYou run but since it is dark you stumbled\n"
              "and die! Good night!\n")
        time.sleep(1)
        print (requiered)
        intro ()
    else:
        print(requiered)
        intro ()
def option_win ():
    print ("\nThe sword feeld you to a stature. The\n"
           "statue holds an oven hand in front of it. You will: \n")
    time.sleep(1)
    print("A. Put the sword insid\n"
          "B. Put the thoothe insid\n"
          "C. Put the chain insid\n")
    choice = input (">>>  ")
    if choice in answer_A:
        if toothe<=0 and chein<=0:
            print("\nA light blind you. When you can see\n"
                  "dedication you lie in your bed.\n"
                  "Fin")
        if toothe>0:
            print ("\mYour body starts to hurt. In pain you lose the consciousness of being aware.\n"
                   "When you wake up again you realize that you\n"
                   "are now the monster.\n"
                   "Fin")
        if chein >0:
            print("\nThe chain in your hand beginn to shin.\n"
                  "A voci beginn to tork to you: 'You give ab the sword\n"
                  "and hold the chain so you will becam a Gardian\n"
                  "of this world\n'"
                  "Fin")
    if choice in answer_B:
        if toothe >0:
            print ("\nA deep style speaks to you:\n"
           "'You have welt the tooth so you are a sleepwalker\n"
           "from now on. You will lif in this world from now on.'\n"
           "Fin")
        elif toothe <= 0:
            option_win
    if choice in answer_C:
        if chein==0:
            print("\nA deep style speeks to you:' So you have\n"
              "wolfed the chain then you are probably a world wanderer'\n"
              "In the nexs moment you lie un your bed.\n"
              "Next to you ther is the sword and around your neck is the chain.\n"
              "Fin")
        elif chein <= 0:
            option_win
    else:
      print (requiered)
      intro ()

intro ()
