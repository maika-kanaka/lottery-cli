import platform
import os
import sqlite3
from clint.textui import colored, puts
from pyfiglet import Figlet

class UI:

    def clear():
        if(platform.system() == 'Windows'):
            os.system("cls")

        elif(platform.system() == 'Ubuntu'):
            os.system("clear")

    def figlet(text, font = 'slant'):
      f = Figlet(font = font)
      print(f.renderText(text))

    def print_color(text, color = 'blue', end=''):
      if color == 'blue':
        print(colored.blue(text,), end=end)
      elif color == 'red':
        print(colored.red(text,), end=end)
      elif color == 'green':
        print(colored.green(text,), end=end)


class Config:

  route = 'home'
  lang = 'en'
  run_program = True



class DB:

  conn = None
  cursor = None 

  def __init__(self):
    # config 
    self.conn = sqlite3.connect("lottery.db")
    self.cursor = self.conn.cursor()

    # create table member
    self.create_table_member()

  def create_table_member(self):
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS data_members (
        created_at DATE,
        won_on_date DATE,
        id INTEGER PRIMARY KEY,
        fullname TEXT,
        description TEXT
      )
    ''')

  def execute_sql(self, sql, param = ()):
    return self.cursor.execute(sql, param)

  def commit(self):
    self.conn.commit()

  def close(self):
    self.conn.close()
