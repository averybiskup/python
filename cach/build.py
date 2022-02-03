#!/usr/bin/python3
import sqlite3

def rebuild():
    con = sqlite3.connect('cach.db')

    con.execute('''
                DROP TABLE IF EXISTS Cach;
            ''')

    con.execute('''
                CREATE TABLE Cach(id INT PRIMARY KEY, 
                                  date DATETIME, 
                                  title VARCHAR(100), 
                                  amount DECIMAL(10.10), 
                                  type VARCHAR(100), 
                                  location VARCHAR(100));
            ''')

    con.commit()
    con.close()

if input('>') == 'yes':
    rebuild()
