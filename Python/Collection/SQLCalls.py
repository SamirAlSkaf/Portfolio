import sqlite3
import os

#Verbindung herstellen
db_name = 'my_test_database.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

#Tabelle erstellen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

#Einfügen
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Diana', 28)")
conn.commit()

#Alle Auswählen
cursor.execute("SELECT * FROM users")
print('Alle Benutzer:', cursor.fetchall())

#Spalte auswählen
cursor.execute("SELECT name FROM users")
print('Namen:', cursor.fetchall())

#Daten von einer bestimmten Zeile zur anderen auswählen
cursor.execute("SELECT * FROM users LIMIT 2 OFFSET 1")  #Holt 2 Zeilen ab der zweiten Zeile
print('Zeilen 2 und 3:', cursor.fetchall())

#Spezifische Spalten aus einem Bereich von Zeilen auswählen
cursor.execute("SELECT name, age FROM users LIMIT 3")  #Holt die ersten 3 Zeilen
print('Erste 3 Benutzer:', cursor.fetchall())

#Auswahl mit einer Bedingung 
ageCondition = 30
cursor.execute("SELECT * FROM users WHERE age > ?", (ageCondition,))
print(f'Benutzer mit Alter > {ageCondition}:', cursor.fetchall())

#Auswahl mit einer Bedingung auf den Namen
cursor.execute("SELECT * FROM users WHERE name = 'Alice'")
print("Benutzer mit Namen 'Alice':", cursor.fetchall())

#Aktualisieren
cursor.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
conn.commit()

#Löschen
cursor.execute("DELETE FROM users WHERE name = 'Bob'")
conn.commit()

#Tabelle löschen
cursor.execute("DROP TABLE IF EXISTS users")
conn.commit()

#Verbindung schließen
conn.close()

#Datenbankdatei löschen
os.remove(db_name)