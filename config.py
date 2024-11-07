import os
import psycopg2


def DBConnect():
    host=os.getenv("DBHOST")
    port=os.getenv("DBPORT")
    user=os.getenv("DBUSER")
    password=os.getenv("DBPASSWORD")
    database=os.getenv("DATABASE")

    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    cursor=connection.cursor()
    return cursor
