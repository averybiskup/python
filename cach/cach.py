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
                            {title},
                            {amount},
                            {_type},
                            {location})
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

def user_input():
  print('What would you like to do?')
  print('0: insert\n1: show')
  _input = input('>')
  
  if _input = '0':
    insert_input()
  else:
    show()
    

insert('1','2','3','4')
  
show()


