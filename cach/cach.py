#!/usr/bin/python3
import sqlite3
import datetime

DB = 'cach.db'

def get_date():
  now = datetime.datetime.now() 
  return now.strftime("%Y-%m-%d")

def get_length():
  con = sqlite3.connect(DB)
  cur = con.cursor()
  
  for row in cur.execute("SELECT COUNT(*) FROM Cach"):
    return row[0]

  con.close()

def insert(title, amount, _type, location):
  con = sqlite3.connect(DB)
  cur = con.cursor()
  
  cur.execute(f'''
    INSERT INTO Cach VALUES({get_length()},
                            \"{get_date()}\",
                            \"{title}\",
                            {amount},
                            \"{_type}\",
                            \"{location}\")
  ''')

  con.commit()
  con.close()

def show():
  con = sqlite3.connect(DB)
  cur = con.cursor()
  
  rows = []
  for row in cur.execute("SELECT * FROM Cach"):
    rows.append(row)

  print(rows)

  con.close()

def create_record():
  title = input('title: ')
  amount = input('amount: ')
  _type = input('type: ')
  location = input('location: ')
  submit = input('submit (y/n): ')

  if (submit == 'y'):
      insert(title, amount, _type, location)
  else:
    create_record()

def user_input():
  print('What would you like to do?')
  print('0: insert\n1: show')
  _input = input('>')
  
  if _input == '0':
    create_record()
  else:
    show()
    

user_input()

