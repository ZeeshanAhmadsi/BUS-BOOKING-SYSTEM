import sqlite3

def connect_database():
    conn=sqlite3.connect("bus_database.db")
    return conn

def create_table():
    conn=connect_database()
    cursor=conn.cursor()

    cursor.execute('''
create table if not exists operators(
                   id text primary key,
                   name text,
                   address text,
                   phone integer,
                   email text
)
                   ''')
    

    cursor.execute('''
create table if not exists buses(
                   id text primary key,
                   name text,
                   address text,
                   phone integer,
                   email text
)
                   ''')
    

    conn.commit()

    conn.close()


def add_operators(op_data):
    conn=connect_database()
    cursor=conn.cursor()

    cursor.execute('insert into operators ()sd.
                    
                    ')

    conn.commit()

    conn.close()



    