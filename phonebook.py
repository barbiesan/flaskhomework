import sqlite3

people = [
  "John Smith", "949-666-0088"
  "Natasha Koshka" "661-877-8866",
  "Vladimir Cabaka","441-111,9988",
  "Loschet Galoboy","714-555-4411",
  ]

people = sorted(people)

connection = sqlite3.connect("people_list.db")
cursor = connection.cursor()

cursor.execute("create table people (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(people)):
  cursor.execute("insert into people (name) values (?)",[people[i]])
  print("added ", people[i])
