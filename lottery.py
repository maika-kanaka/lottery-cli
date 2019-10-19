# system modules
import sys 

# import my modules
from libraries import *
from pages.home import HomePage
from pages.lottery import LotteryPage
from pages.member import MemberPage

# run run run ....
while Config.run_program:

  UI.clear()

  if(Config.route == 'home'):
    HomePage.menu()

  elif(Config.route == '1'):
    MemberPage().data()

  elif(Config.route == '2'):
    LotteryPage().confirm()

  elif(Config.route == '0'):
    Config.run_program = False

  else:
    print('Menu "'+ Config.route +'" not found')
    Config.route = "home"
  
DB().close()

