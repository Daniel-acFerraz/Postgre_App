from fastapi import FastAPI
import uvicorn
from backend.database.db_interface import DBInterface

user="postgres" #usuario digitado pelo usuario
password="Postx89f7+" #password digitado pelo usuario
host = "localhost"
dbname="fakeapp"



app = FastAPI()

@app.get("/conn_data")
def get_conn_data() -> str:
    print(myInterface)
    return 'Welcome!'



if __name__ == '__main__':
    myInterface = DBInterface(user, password, dbname, host)
    myInterface.get_connection()
    myInterface.check_db_connection()
    print("It's working!")
    uvicorn.run(app, port=8000)