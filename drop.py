import sqlite3 as sql

def drop_tables():
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()
    instruction = f"DROP TABLE users"
    cursor.execute(instruction)
    instruction = f"DROP TABLE jobs"
    cursor.execute(instruction)
    
    print ("Database tables were dropped successfully!")
    return 1
    
    
if __name__ == "__main__":
    drop_tables()