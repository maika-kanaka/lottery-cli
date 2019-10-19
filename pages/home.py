from libraries import UI
import sys 

sys.path.append("../")

from libraries import Config

class HomePage:

  def menu():
    UI.figlet("LOTTERY")
    UI.print_color(text="Version: ", color='blue', end='')
    print('0.1.0')

    print("\n")
    print("(1) Member")
    print("(2) Run Lottery")
    print("(0) Exit")
    print("\n")

    choose = input("Select the menu> ")

    Config.route = choose