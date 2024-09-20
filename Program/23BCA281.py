###[ 7 ] Create table contact(fname,laname,contact,email,city). Perform following operation on it
##1. Insert Contact 8 records
##2. Delete Contact¶"""


import sqlite3 as sq

#Connect to the py.db databse
conn=sq.connect("D:\\sqlite\\csv\\py.db")
cur=conn.cursor()
#Create table contact
cur.execute('''
CREATE TABLE IF NOT EXISTS contact (
    fname TEXT,
    lname TEXT,
    contact TEXT,
    email TEXT,
    city TEXT
)
''')
#Insert 8 records in the table
records = [
    ('Om', 'Patel', '1234567890', 'om@gmail.com', 'Surat'),
    ('Sai', 'Patel', '9876543210', 'sai@gmail.com', 'Bardoli'),
    ('Ram', 'Shah', '4561237890', 'ram@gmail.com', 'Madhi'),
    ('Bob', 'Brown', '7894561230', 'bob@example.com', 'Vyara'),
    ('Charlie', 'Johnson', '1231231234', 'charlie@example.com', 'Surat'),
    ('Diana', 'Williams', '3213213210', 'diana@example.com', 'Mahuva'),
    ('Eve', 'Davis', '4567891230', 'eve@example.com', 'Vapi'),
    ('Frank', 'Miller', '6543219870', 'frank@example.com', 'Navsari')
]
#Execute insert query
cur.executemany('''
INSERT INTO contact (fname, lname, contact, email, city)
VALUES (?, ?, ?, ?, ?)
''', records)
conn.commit()
#Create trigger
cur.execute('''
CREATE TRIGGER IF NOT EXISTS delete_trigger
BEFORE DELETE ON contact
FOR EACH ROW
WHEN OLD.fname = 'Ram'
BEGIN
    DELETE FROM contact WHERE fname = 'Ram';
END;
''')
conn.commit()
#Execute delete query
cur.execute("DELETE FROM contact WHERE fname = 'Ram'")
conn.commit()
cur.execute('SELECT * FROM contact')
#Print records after delete
rows = cur.fetchall()
for row in rows:
    print(row)
