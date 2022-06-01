"""Place any code needed to start the API in this file.
"""

from pathlib import Path
import sqlite3
import json
from fastapi import FastAPI, Request, status, HTTPException
import uvicorn



def get_db_connection():
    """
    Return a connection to the local input DB.

    You can assume that there will be a SQLite3 DB file named `input.db` at the top
    level of this repo.

    This file will contain a single table ("keys") created by the following SQL:
        `create table keys(key text, val text)`

    It will contain some number of records that should be initially available right
    after the API starts up.

    Feel free to use/modify this method as needed.
    """
    db_path = (Path(__file__).parent.parent / "input.db").resolve()
    return sqlite3.connect(db_path)

def execute_query(query:str, target=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    if target is not None:
        query_result = cursor.execute(query,target)
    else:
        query_result = cursor.execute(query)
    connection.commit()
    return query_result
    
class App():
    """
    Entrypoint for the API. You can perform any necessary setup in here. 
    Feel free to call other functions, etc.
    """
    app = FastAPI()
    
    #=== Application Endpoints ===
    @app.on_event("startup")
    def create_table():
        execute_query("CREATE TABLE IF NOT EXISTS keys(key text, val text)")
        return None
    
    #Retrives all records from table.
    @app.get("/all", status_code=status.HTTP_200_OK)
    def get_records():
        retrieved_data = execute_query("SELECT * FROM keys").fetchall()
        return retrieved_data
    
    
    @app.post("/set",status_code=status.HTTP_200_OK)
    def set_records(request: Request, input_record: dict):
        """
        Validates body input. Sets a key in the store using execute_query function.
        """
        try:
            execute_query("INSERT INTO keys(key, val) VALUES (?,?)",[input_record["key"],input_record["val"]])
            return f"Record {input_record} has been saved to database."
        except KeyError:
            return "Key Error: Please check your body format. Acceptable format is: {'key': foo, 'val': bar}."

    
    @app.get("/get/{given_key}", status_code=status.HTTP_200_OK)
    def get_records(request: Request, given_key: str):
        """
        Validates provided input. Retrieves the value of a given key using execute_query function. 
        Raises Error 404 NOT FOUND, if not match.
        """
        try:
            #Finds key-value pair based on provided key in Table key. Note: retrived_data variable is a tuple.
            retrieved_data = execute_query("SELECT key, val FROM keys WHERE key=?",(given_key,)).fetchone()
            if not retrieved_data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The value based on: {given_key} was not found.")
            #Assigns elements to new dictionary.
            result = {"key":"","val":""}
            result["key"] = retrieved_data[0]
            result["val"] = retrieved_data[1]
            return result
        
        except KeyError:
            return "Key Error: Please check your body format. Acceptable format is: {'key': foo}."
        
    #Runs server. app is the object created inside of Main class.
    uvicorn.run(app, host="0.0.0.0", port=8000)    
    
if __name__ == "__main__":
    App()
