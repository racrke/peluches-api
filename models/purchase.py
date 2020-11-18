from db import db
import uuid , datetime
class Purchase:

    client_id = None
    clientOrder = None
    products = None #e.g [{pid:121,amount:1}]


    """
        [RealDictRow([('oid', 'O00000001'),
              ('clientid', 'C00000002'),
              ('total', Decimal('1025.00')),
              ('date', datetime.date(2020, 11, 16)),
              ('status', 'Entregado')])]

        """

    def get_purchases(self):
        repo = db.Repo() 
        sql_select_query = """select * from ClientOrder where clientid = '{0}'""".format(self.client_id)
        repo.cursor.execute(sql_select_query)
        records = repo.cursor.fetchall()
        repo.close()
        return records

    def all(self):
        repo = db.Repo() 
        sql_select_query = """select * from ClientOrder"""
        repo.cursor.execute(sql_select_query)
        records = repo.cursor.fetchall()
        repo.close()
        return records


    def create_order(self):
        repo = db.Repo() 
        postgres_insert_query = """Insert into ClientOrder(oID, ClientId, date) Values (%s,%s,%s)"""
        self.clientOrder  = str(uuid.uuid4())[:20]
        record_to_insert = (self.clientOrder, self.client_id,str(datetime.datetime.today()).split()[0])
        repo.cursor.execute(postgres_insert_query, record_to_insert)
        repo.connection.commit()
        repo.close()

        for prod in self.products:
            repo = db.Repo() 
            postgres_insert_query = """Insert into detailOrder(DetailId, OId, Pid, Cantidad, total) Values (%s, %s, %s, %s, %s);"""
            record_to_insert = (str(uuid.uuid4())[:20],self.clientOrder,prod["pid"],prod["amount"],prod["total"])
            repo.cursor.execute(postgres_insert_query, record_to_insert)
            repo.connection.commit()
            repo.close()

        return True

    def get_order(self):
        repo = db.Repo() 
        postgres_get_query = """select *
            from detailOrder d, clientOrder c, product p
            where d.oId = c.oId and c.oId = %s and d.pid = p.pid"""
        value = (self.clientOrder,)
        repo.cursor.execute(postgres_get_query, value)
        records = repo.cursor.fetchall()
        repo.close()
        return records 

    def update_status(self,value):
        repo = db.Repo() 
        postgres_insert_query = """update clientorder set status = %s where oId = %s;"""
        record_to_insert = (value,self.clientOrder)
        repo.cursor.execute(postgres_insert_query, record_to_insert)
        repo.connection.commit()
        repo.close()


def client_order_to_json(record):
    return {"oid":record["oid"],
    "clientid":record["clientid"],
    "total":str(record["total"]),
    "date":record["date"],
    "status":record["status"],
    }

def client_detail_to_json(record):
    return {"detailid":record["detailid"],
    "pid":record["pid"],
    "oid":record["oid"],
    "clientid":record["clientid"],
    "amount":str(record["cantidad"]),
    "name": record["name"],
    "price": str(record["price"])
}




        