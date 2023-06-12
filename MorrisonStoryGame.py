import random

def luck():
    return random.randint(1, 100)
def main ():
    q1 = ""
    q2 = ""
    q3 = ""

    life = 3
    swordroll = 0
    sword = 0
    gaurdroll = 0
    cityroll = 0
    bandit1roll = 0
    bandit2roll = 0
    pourchroll = 0
    ans = "true" 

    while (ans == "true"):
        print( "You wake up in a particular place that leads you somewhere in the woods for the most part.\n")
        print(  "Which way are you waklking? \n \n")
        print(  "A.) Stone Path \n")
        print(  "B.) Dirt Path\n")
        print(  "C.) Your own Path \n")

        q1 = input()

        if q1 == 'a' or q1 == 'A':
            print(  "Its a peacful walk you find a random sword on the path, roll higher then a 30 and you can pick up the sword. \n\n")
            swordroll = luck()
            print(  "You roll a ", swordroll,".\n")
            if (swordroll > 30):
                print(  "You pick up the sword.\n")
                sword = 1
            else:
                print(  "You left the sword.\n")
                sword = 0
            
            
            print(  "You find a town what are you going to do next to get some answers? \n")
            print(  "A.) Talk to gaurd \n")
            print(  "B.) Just walk around by yourself\n")
            print(  "C.) Find someone who looks informed \n")

            q2= input()

            if q2 == 'a' or q2 == 'A':
                if sword == 1:
                    print(  "The gaurd looks at you he sees that you have one of his men swords he tries to arrest you.")
                    print(  "Roll a number over 50 to run away.\n")
                    gaurdroll = luck()
                    print(  "You roll a ", gaurdroll,".\n")
    
                    if (gaurdroll > 50):
                        print(  "You ran into the woods with your sword still in hand.\n")
                    else:
                        print(  "You decied to fight even though you never pick up a sword in your life, so he won the fight and throw you in jail.\n")
                        sword = 0
                        end()
                else:
                    print(  "The gaurd says talk to the church, You might survive")
                    end()
                
            elif q2 == 'b' or q2 == 'B':
                print(  "You walk around and now you are lost.\n")
                print(  "You see a sign post with locations around town you see two that look promising the church or the libary. \n")
                print(  "Roll a number over 50 to go to the libary.\n")
                cityroll = luck()
                print(  "You roll a ", cityroll,".\n")

                if cityroll > 50:
                    print(  "You make your way towards the libary.\n")
                    end()
                else:
                    print(  "You make your way towards the church it says no weapons in the house of the lord.\n")
                    sword = 0
                    end()
                
            elif ( q2 == 'c' or q2 == 'C'):
                print(  "You find a smart looking women, she is a libary worker she tells you what you need to hear." )
                end()
            else:
                print( "Not A Choice")
            
        elif q1 == 'b' or q1 == 'B':
            print(  "You find a cabin at the end of the path and find a women on the pourch. \n")

            print(  "What are you going to do next? \n")
            print(  "A.) GO THE OTHER WAY!! \n")
            print(  "B.) Go say hello to if she can help. \n")
            print(  "C.) Tell the lady to come to you. \n")

            q3= input()

            if (q3 == 'a' or q3 == 'A'):
                print(  "You turn around and you run into bandits.")
                print(  "Run or fight? Roll a number over 20 to run.\n")
                bandit1roll = luck()
                print(  "You roll a ",bandit1roll,".\n")

                if (bandit1roll > 20):
                    print(  "You run towards the lady on the pourch.\n")
                else:
                    print(  "You decied to fight even though you are out numberd, you got jump took your sword and left you for dead.\n")
                    sword = 0
                    life -= 1
                    end()
                
            elif (q3 == 'b' or q3 == 'B'):
                print(  "You walk up to the lady and say hello, she smiles and say I have been expeting you." )
                end()
            elif ( q3 == 'c' or q3 == 'C'):
                print(  "She tells you if you dont want to get shot in the back then come to the pourch." )
                print(  "Go to pourch or don't go to pourch? Roll a number over 10 to go to pourch.\n")
                pourchroll = luck()
                print(  "You roll a ", pourchroll,".\n")

                if (pourchroll > 10):
                    print(  "You go towards the lady on the pourch.\n")
                    end()
                else:
                    print(  "You decied to not go to the pourch and got shot in the back whih some arrows and last thing you see is a flash of light.\n")
                    sword = 0
                    life -= 1
                    end()

            else:
                print( "Not A Choice ----")
            
        elif ( q1 == 'c' or q1 == 'C'):
            print(  "For some reason you walk ramdomly though the woods and you run into some bandits.\n")
            print(  "Now they are tring to kill you. \n")
            print(  "Run or fight? Roll a number over 30 to run.\n")
            bandit2roll = luck()
            print(  "You roll a", bandit2roll,".\n")
            if (bandit2roll > 30):
                print(  "You run towards a cabin with a lady on the pourch.\n")
                end()
            else:
                print(  "You decied to fight even though you are out numberd, you got jump took your belongings and left you for dead.\n")
                sword = 0
                life -= 1
                end()

def end():
    print(  "END for now \n")
    print(  "Do you want to play again. Y/N\n")
    again = input()
    if again == "n" or "N":
        ans = "false"
main()