import sys 
import time
import datetime 
import random

sys.path.append("../")

from libraries import UI, Config
from models.member_model import MemberModel

class LotteryPage:

    def __init__(self):
        self.memberModel = MemberModel()

    def confirm(self):
        c = input("ARE YOU READY (Y/n)> ")

        if c.lower() == 'n':
            Config.route = 'home'
            return False
        else:
            # get data 
            query = self.memberModel.data()

            # valid: data member is must exists
            if len(query) < 1:
                print("You do not have any members")
                self.confirm()
                return False

            # fill to list
            members = []
            for member in query:
                members.append( member[2] )

            # loading 
            print('Loading: ', end='')
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
            for ano in range(toolbar_width):
                time.sleep(.04)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n") # this ends the progress bar

            # random & get the winner 
            winner = random.randrange(0, len(members))
            the_winner = self.memberModel.detail(pk = members[winner])

        # UI.figlet(text="THE WINNER IS ......", font = "cybersmall")
        print("The winner is: ")
        print("\n", end="")
        UI.figlet(text = str(the_winner[3]), font = "twopoint")
        
        # ask 
        c = input("Save the winner (Y/n)> ")
        c = c.lower()

        # update the winner 
        now = datetime.datetime.now()
        self.memberModel.update_the_winner(the_winner[2], now)
        