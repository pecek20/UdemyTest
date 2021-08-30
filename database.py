import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

#c.execute("""CREATE TABLE customers (
#	first_name TEXT,
#	last_name TEXT,
#	email TEXT
#)""")

## DATATYPES ##

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Pojedynczy rekord
# c.execute("INSERT INTO customers VALUES ('Mary', 'Jonas', 'mary@jonas.pl')")

# Wieksza ilosc z listy

#many_customers = [('Wes', 'Brown', 'wes@wes.pl'), ('Steph', 'Kolo', 'steph@kolo.pl'), ('Dan', 'Pas', 'dan@pas.pl'),]
#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#c.execute("SELECT * FROM customers WHERE first_name = 'Wes'")

#c.fetchone()
#c.fetchmany()
#c.fetchall()

#print(c.fetchmany(3))
#print(c.fetchone()[0])

#for item in items:
#	print('email: ' + item[2])

#c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%'")

## UPDATE RECORDS ##
c.execute("""UPDATE customers SET first_name = 'Bob'
	WHERE rowid = 1
	""")

conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
	print(item)

# connection close
conn.close()
