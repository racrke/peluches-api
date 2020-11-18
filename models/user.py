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
            sql_select_query = """select * from StoreUser where uid = '{0}'""".format(ID)
            repo.cursor.execute(sql_select_query)
            record = repo.cursor.fetchone()
            repo.close()
            print(record)
            self.ID = record["uid"]
            self.mail = record["mail"]
            self.name = record["uname"]
            self.password = record["encryptedpassword"]
            self.u_type = record["utype"]

            return True
        except Exception as e:
            print("user::",e)
            return False

    def get_with_email(self, ID):
        print("GETMIEMAIL",ID)
        try:
            repo = db.Repo() 
            sql_select_query = """select * from StoreUser where mail = '{0}'""".format(ID)
            repo.cursor.execute(sql_select_query)
            record = repo.cursor.fetchone()
            repo.close()
            print(record)
            self.ID = record["uid"]
            self.mail = record["mail"]
            self.name = record["uname"]
            self.password = record["encryptedpassword"]
            self.u_type = record["utype"]

            return True
        except Exception as e:
            print("user::",e)
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
            print("User::Insert",e)
            return e
        return True

    def to_json(self):
        return {"id":self.ID, 
                "mail":self.mail,
                "name":self.name,
                "type":self.u_type}
