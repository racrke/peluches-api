from db import db
import base64, bcrypt

class User:

	ID = None
	name = None
	u_type = None
	mail = None
	password = None

	def to_tuple(self):
		return(self.name,self.u_type,self.mail,self.password,self.ID)

	def to_tuple_no_id (self):
		return (self.name,self.u_type,self.mail,self.password)

	def get(self, ID):
		try:
			repo = db.Repo() 
			sql_select_query = """select * from StoreUser where mail = '{0}'""".format(ID)
			repo.cursor.execute(sql_select_query)
			record = repo.cursor.fetchone()
			repo.close()
			
			self.ID = record[0]
			self.mail = record[1]
			self.name = record[2]
			self.password = record[4]
			self.u_type = record[5]

			return True
		except Exception as e:
			print(e)
			return False

	def set_password(self, password):
		salt = bcrypt.gensalt()
		hashed = bcrypt.hashpw(password.encode(), salt)
		encoded = base64.b64encode(hashed).decode()
		self.password = encoded

	def insert(self):
		try:
			repo = db.Repo() 
			postgres_insert_query = """INSERT INTO StoreUser (uname, uType, mail, encryptedPassword, uID) VALUES (%s,%s,%s,%s,%s)"""
			record_to_insert = self.to_tuple()
			repo.cursor.execute(postgres_insert_query, record_to_insert)
			repo.connection.commit()
			repo.close()
		except Exception as e:
			return e
		return True