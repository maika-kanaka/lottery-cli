import sys
import datetime
from prettytable import PrettyTable

sys.path.append("../")
sys.path.append("../models/")

from libraries import *
from models.member_model import MemberModel

class MemberPage:

  def __init__(self):
    self.etto = "ano, sumimasen ..."

  def data(self):
    print("\n")
    UI.figlet(text = "MEMBER ", font = 'bubble')
    print("\n")
    print("(<) Back to homepage")
    print("(+) Add")
    print("(-) Delete")
    print("\n")

    table = PrettyTable()
    table.field_names = ["No", "MemberID", "Fullname", "Description", "Created at", "Completed at"]

    datas = MemberModel().data()
    no = 1
    for cie in datas:
      
      table.add_row(row = [no, "M-{}".format(cie[2]), cie[3], cie[4], cie[0], cie[1]])
      no = no + 1

    print(table)
    print("\n")
    menu = input("Select the menu> ")

    if menu == '<':
      Config.route = 'home'
    elif menu == '+':
      self.add()
    elif menu == '-':
      self.delete()

  def add(self):
    UI.clear()

    UI.figlet(text = "MEMBER > ADD", font = 'bubble')
    fn = input("Fullname> ")
    desc = input("Description> ")
    
    menu = input("Do you want to save the data (y/n) ? ")
    menu = menu.lower()

    UI.clear()
    if menu == 'y':
      save = MemberModel().save(fullname=fn, description=desc)
      UI.print_color(text="Saving data successfully", color='green')
    elif menu == 'n':
      UI.print_color(text="Canceled save", color='red')
    else:
      print('Menu "'+ menu +'" not found')

    self.data()

  def delete(self):
    # header 
    UI.clear()
    UI.figlet(text = "MEMBER > DELETE", font = 'bubble')
    print("\n")

    # ask for delete
    pk = input("Type MemberID that you want to delete> ")
    pk = pk.lower()

    # valid: ID is exists
    if "m-" in pk:
      pk = pk.replace("m-","")
      if pk.isnumeric():
        dbdata = MemberModel().detail(pk = pk)
        
        if(dbdata == None):
          UI.print_color(text="The MemberID you typed is does not exists", color="red")
          self.data()
          return False
      else:
        UI.print_color(text="The MemberID you typed is does not exists", color="red")
        self.data()
        return False
    else:
      UI.print_color(text="The MemberID you typed is incorrect", color="red")
      self.data()
      return False

    # delete from db
    delete = MemberModel().delete(primary_key = pk)

    # message 
    UI.clear()
    if delete:
      UI.print_color(text="Delete data successfully", color="green")
    else:
      UI.print_color(text="Error while deleting data", color="red")

    # redirect
    self.data()