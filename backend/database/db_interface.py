import psycopg2

class DBInterface:

    def __init__(self, user, password, db_name, hostname):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.hostname = hostname
        self.db_connection = None

    def get_connection(self):
        try:
            self.db_connection = psycopg2.connect(
                host=f"{self.hostname}", 
                dbname=f"{self.db_name}", 
                user=f"{self.user}", 
                password=f"{self.password}", 
                port="5432"
                )
            print(f"Connected with database successfully: {self.db_connection}")
            return self.db_connection
        except(psycopg2.DatabaseError, psycopg2.OperationalError) as e:
            print(repr(e))
            if "senha falhou" in repr(e):
                self.db_connection = None
                print("Incorrect user or password")
                return {"error": "Incorrect user or password"}
            else:
                self.db_connection = None
                print("Login failed, try again later")
                return {"error": "Login failed"}
        except Exception as e:
            self.db_connection = None
            print(f"Unexpected error: {repr(e)}")
            return {"error": "Unexpected error trying to connect to DB"}

    def check_db_connection(self):
        if self.db_connection is None or self.db_connection.closed !=0:
            print("No connection to database, trying to reestablish...")
            self.get_connection()
            if self.db_connection is None or self.db_connection.closed !=0:
                print("Failed trying to reestablish connection")
                return False
        print("Connected!")
        return True

# user="postgres" #usuario digitado pelo usuario
# password="Postx89f7+" #password digitado pelo usuario
# host = "localhost"
# dbname="fakeapp"

# if __name__ == '__main__':
#     myInterface = DBInterface(user, password, dbname, host)
#     myInterface.get_connection()
#     myInterface.check_db_connection()
#     print("It's working!")