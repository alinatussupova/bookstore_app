import sqlite3


class Database:
    # Connect function
    def __init__(self, db):
        # Establish connection to a database
        self.con = sqlite3.connect(db)
        # Define a cursor object
        self.cur = self.con.cursor()
        # Execute SQL statement
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        # Commit changes
        self.con.commit()


    # Insert function: insert some data in the database
    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.con.commit()


    # View function: fetch all the rows of the table
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows


    # Search function
    def search(self,title="",author="",year="",isbn=""):    
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows


    # Delete function
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.con.commit()
        

    # Update function
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.con.commit()


    def __del__(self):
        self.con.close()
    


# insert("The Sun", "John Smith", 1918, 91393221113)
# delete(4)
# update(5,"The moon","Jake Shim",1917,91234567)
# print(view())
# print(search(author="John Smith"))