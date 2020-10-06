import db

class product:

	ID = None
	name = None
	p_type = None
	images = None
	price = None
	stock = None

	def to_tuple(self):
		return(self.name,self.p_type,self.images,self.price,self.stock,self.ID)

	def to_tuple_no_id (self):
		return (self.name,self.p_type,self.images,self.price,self.stock)

	def get(self, ID):
		repo = db.Repo()
		sql_select_query = """select * from products where id = %s"""
        repo.cursor.execute(sql_select_query, ID)
        record = cursor.fetchone()
        repo.close()

       	self.ID = record.ID
       	self.name = record.name
       	self.p_type = record.p_type
		self.images = record.images
		self.price = record.price
		self.stock = record.stock


	def insert(self):
		repo = db.Repo()
		postgres_insert_query = """INSERT INTO products (name, p_type, images, price, stock,ID) VALUES (%s,%s,%s,%s,%s,%s)"""
   		record_to_insert = self.to_tuple()
   		repo.cursor.execute(postgres_insert_query, record_to_insert)
   		connection.commit()
   		repo.close()

	def delete(self):
		repo = db.Repo()

		if self.ID != None:
			query = """DELETE FROM products WHERE ID = %s"""
   			recordepo.cursor.execute(query, self.ID)
   			connection.commit()
   		repo.close()

	def update(self):
		repo = db.Repo()
		postgres_insert_query = """UPDATE products
		SET name = %s,
		p_type = %s,
		images = %s,
		price = %s,
		stock = %s
		WHERE ID = %s"""
   		record_to_insert = self.to_tuple()
   		repo.cursor.execute(postgres_insert_query,record_to_insert )
   		connection.commit()
   		repo.close()

