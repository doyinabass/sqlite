
import sqlite3

conn = sqlite3.connect("SGA_1_3_learners.db")

cursor = conn.cursor()

learners_list = [("abdullahi","Ali","abdulahiAli@gmail.com","DataScience"),
                 ("kephie","davies","kephiedavies@gmail.com","DataScience"),
                 ("Akira","Daniel","Akira@gmail.com","DataScience")
]
 
cursor.executemany("INSERT INTO learners VALUES(?,?,?,?)", learners_list)

print("we have inserted", cursor.rowcount, 'records to the table')

cursor.execute("SELECT * FROM learners")

conn.commit()


conn.close()

