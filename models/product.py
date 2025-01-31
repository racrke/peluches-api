from db import db
class Product:

    ID = None
    name = None
    p_type = None
    images = None
    price = None
    stock = None
    description = None

    def to_tuple(self):
        return(self.name,self.p_type,self.images,self.price,self.stock,self.ID)

    def to_tuple_no_id (self):
        return (self.name,self.p_type,self.images,self.price,self.stock)

    def get(self, ID):
        repo = db.Repo() 
        sql_select_query = """select * from Product where pid = '{0}'""".format(ID)
        repo.cursor.execute(sql_select_query)
        record = repo.cursor.fetchone()
        repo.close()
        
        self.ID = record["pid"]
        self.name = record["name"]
        self.p_type = record["ptype"]
        self.images = record["imgs"]
        self.price = record["price"]
        self.stock = record["stock"]
        self.description = record["descripcion"]


    def insert(self):
        repo = db.Repo() 
        postgres_insert_query = """INSERT INTO Product (name, pType, imgs, price, stock, pID) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = self.to_tuple()
        repo.cursor.execute(postgres_insert_query, record_to_insert)
        repo.connection.commit()
        repo.close()

    def delete(self):
        repo = db.Repo() 

        if self.ID != None:
            query = """DELETE FROM Product WHERE PID = '{0}'""".format(self.ID)
            repo.cursor.execute(query)
            repo.connection.commit()
        repo.close()

    def update(self):
        repo = db.Repo() 
        postgres_insert_query = """UPDATE Product
        SET name = %s,
        ptype = %s,
        imgs = %s,
        price = %s,
        stock = %s
        WHERE pID = %s"""
        record_to_insert = self.to_tuple()
        repo.cursor.execute(postgres_insert_query,record_to_insert )
        repo.connection.commit()
        repo.close()
    
    def all(self):
        repo = db.Repo() 
        query = """SELECT * FROM Product"""
        repo.cursor.execute(query)
        records = repo.cursor.fetchall()
        repo.close()
        return records
        
    def to_json(self):
        return { "pid": self.ID ,
       "name": self.name ,
       "pType": self.p_type, 
       "images": self.images , 
        "prices": str(self.price) , 
        "stock":self.stock,
        "description":self.description }
    
def to_json(record):
        return { "pid": record["pid"] ,
       "name": record["name"] ,
       "pType": record["ptype"], 
       "images": record["imgs"] , 
        "prices": str(record["price"] ), 
        "stock":record["stock"],
        "description":record["descripcion"]}


