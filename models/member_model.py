import sys 
import datetime 

sys.path.append("../")

from libraries import DB

class MemberModel:

  objDB = None
  table = ''

  def __init__(self):
    self.objDB = DB()
    self.table = 'data_members'

  def data(self):
    return self.objDB.execute_sql("SELECT * FROM "+ self.table +" ORDER BY fullname").fetchall()
  
  def detail(self, pk):
    sql = "SELECT * FROM "+ self.table +" WHERE id = ?";

    return self.objDB.execute_sql(sql, (pk,)).fetchone();

  def primary_key(self):
    query = self.objDB.execute_sql("SELECT id FROM "+ self.table +" ORDER BY id DESC").fetchone()
    
    if(query == None):
      return 1
    else:
      return int(query[0]) + 1

  def save(self, fullname, description):
    # prepare save 
    pk = self.primary_key()
    created_at = datetime.datetime.now()
    sql = "INSERT INTO "+ self.table +" VALUES (?, NULL, ?, ?, ?)"

    # save 
    self.objDB.execute_sql(sql, (created_at, pk, fullname, description))
    self.objDB.commit()

    return True

  def update_the_winner(self, primary_key, date):
    sql = "UPDATE "+ self.table +" SET won_on_date = ? WHERE id = ?"

    self.objDB.execute_sql(sql, (date, primary_key))
    self.objDB.commit()

    return True

  def delete(self, primary_key):
    sql = "DELETE FROM "+ self.table +" WHERE id = ?"
    
    self.objDB.execute_sql(sql, (primary_key,))
    self.objDB.commit()

    return True