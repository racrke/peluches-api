import psycopg2
from psycopg2 import Error


class Repo:

  cursor = None
  connection = None

  def __init__ (self):
      try:
          self.connection = psycopg2.connect(user = "postgres",
                                        password = "pass@#29",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "postgres_db")

          self.cursor = connection.cursor()
          
      except (Exception, psycopg2.DatabaseError) as error :
          print ("Error", error)

  def close(self):
      self.cursor.close()
      self.connection.close()