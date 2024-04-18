# Step 0 - import sqlite3
import sqlite3
import queries as q

# # Step 1 - Connect to the database
# # Triple-check the spelling of your database filename
# connection = sqlite3.connect('rpg_db.sqlite3')

# # Step 2 - Make the "cursor"
# cursor = connection.cursor()

# # Step 3 - Write a query (moved this over to queries.py)
# # query = 'SELECT character_id,name FROM charactercreator_character;'

# # Step 4 - Execute the query on the cursor and fetch the results
# # "Pulling the results" from the cursor
# results = cursor.execute(q.SELECT_ALL).fetchall()

# if __name__ == '__main__':
#     print(results[:5])

'''
BELOW IS AN ALTERNATE WAY USING METHODS INSTEAD OF THE ABOVE STEPS THAT WE'LL USE
'''

# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    # Make the "cursor"
    curs = conn.cursor()
    # Execute the query
    curs.execute(query)
    # Pull (and return) the results
    return curs.fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    print(execute_q(conn, q.SELECT_ALL)[:5])
