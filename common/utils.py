from pymysql import (connect as sql_conn,)
from pymysql.cursors import (DictCursor as DictCursor)
from os import getenv
from datetime import datetime
from functools import wraps
import os
from dotenv import load_dotenv
load_dotenv()

def execute_query(query,data):
    """Function to execute query

    Args:
        query (str): SQL Query to execute
        data (tuple): tuple of parameters

    Raises:
        e: Exception if the query fails to execute

    Returns:
        list: list of all queried items
    """

    database_connection = sql_conn(host=str(getenv("DB_URL")),
                                        user=str(getenv("DB_USER")),
                                        password=str(getenv("DB_PASSWORD")),
                                        db=str(getenv("DB_NAME")),
                                        charset="utf8mb4",
                                        cursorclass=DictCursor)

    try:
        # Cursor object creation
        cursor_object = database_connection.cursor()
        # Execute the sqlQuery
        cursor_object.execute(query,data)

        return cursor_object.fetchall()
    except Exception as e:
        raise Exception("Database Failed to fetch the data\nError Description--->",str(e))

    finally:
        database_connection.close()


def update_logs(func):
    @wraps(func)
    def decorated(*args,**kwargs):
        status,message,func_name =  func(*args,**kwargs)
        with open(os.path.join(os.path.abspath("App"),"logs.txt"),"a") as file:
            file.write("\n"+str(func_name)+"---["+datetime.now().strftime(r"%Y-%m-%d_%H:%M:%S")+"]--"+status+"-->"+message)
            file.close()
    return decorated
