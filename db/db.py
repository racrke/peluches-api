import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor

class Repo:

    cursor = None
    connection = None

    def __init__ (self):
        try:
            self.connection = psycopg2.connect(user = "postgres",
                                            password = "hmsdwpHmqPPbvmyL",
                                            host = "34.123.147.152",
                                            port = "5432",
                                            database = "postgres",
                                            cursor_factory=RealDictCursor)

            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Repo::Error", error)

    def close(self):
        self.cursor.close()
        self.connection.close()