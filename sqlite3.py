import sqlite3

connection=sqlite3.connect("C:\\Users\\victo\\OneDrive\\Documents\\GitHub\\Tech-Academy-Projects\\Python-Projects\\test_database.db")
peopleValues=(('Ron','Obvious',42),('Luigi','Vercotti',43),('Arthur','Belling',28))

with sqlite3.connect('test_database.db') as connection:
    c=connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)",
                  peopleValues)

    c.execute("SELECT FirstName, LastName FROM People WHERE AGE>30")
    for row in c.fetchall():
        print(row)
