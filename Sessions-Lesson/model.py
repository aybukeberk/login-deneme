import sqlite3

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()

def authenticate(username, password):
# returns id from users DB (or None)
    # connect_to_db()
    query = "SELECT username, password FROM users WHERE username = ?"
    connect_to_db()
    DB.execute(query, (username,))
    search_results = DB.fetchone()
    if username == search_results[0] and password == search_results[1]:
        return search_results[0]
    else:
        return None

def get_user_by_name(username):
# returns id for a user
    query = "SELECT id FROM users WHERE username = ?"
    connect_to_db()
    DB.execute(query, (username,))
    search_results = DB.fetchone()
    id_from_users = search_results[0]
    print "ID from users: ", id_from_users
    return id_from_users

def get_wall_posts_by_user_id(id_from_users):
# returns wall posts for a user's wall
    query = "SELECT author_id, created_at, content FROM wall_posts WHERE owner_id = ?"
    connect_to_db()
    DB.execute(query, (id_from_users,))
    wall_results = DB.fetchall()
    return wall_results

# def new_wall_post(id_from_users):
# # post a new message on a wall)=
#     query = "INSERT into wall_posts VALUES ()"