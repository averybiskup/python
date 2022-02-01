#!/usr/bin/python3
import sqlite3

con = sqlite3.connect('cach.db')

con.execute(
        '''
        DROP TABLE IF EXISTS Cache;
        '''
        )
con.execute(
        '''
        CREATE TABLE Cach(id INT PRIMARY KEY, 
                              givenName VARCHAR(100), 
                              familyName VARCHAR(100), 
                              orgName VARCHAR(100), 
                              gender VARCHAR(10), 
                              date VARCHAR(20));
        '''
        )


con.commit()
con.close()
