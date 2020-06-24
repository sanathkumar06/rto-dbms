# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:44:26 2019

@author: root
"""
import sqlite3


curs = sqlite3.connect('gaadinew.db')
connection = curs.cursor()

def Create_all_the_tables(curs,connection):



   curs.execute("create table people "
   "(sin CHAR(15), name VARCHAR(40), height number(5,2), weight number(5,2),"
   "eyecolor VARCHAR (10), haircolor VARCHAR(10), addr VARCHAR2(50), gender CHAR,"
   "birthday      DATE,"
   "PRIMARY KEY (sin), CHECK ( gender IN ('m', 'f') ))")

   curs.execute("create table drive_licence "
   "(licence_no CHAR(15), sin char(15), class VARCHAR(10),"
   "issuing_date DATE, expiring_date DATE,"
   "PRIMARY KEY (licence_no), UNIQUE (sin), FOREIGN KEY (sin) REFERENCES people ON DELETE CASCADE)")

   curs.execute("create table driving_condition "
   "(c_id INTEGER, description VARCHAR(1024),"
   "PRIMARY KEY (c_id))")

   curs.execute("create table restriction "
   "(licence_no   CHAR(15), r_id INTEGER,"
   "PRIMARY KEY (licence_no, r_id), FOREIGN KEY (licence_no) REFERENCES drive_licence,"
   "FOREIGN KEY (r_id) REFERENCES driving_condition)"
   )


   curs.execute("create table vehicle_type "
   "(type_id integer, type CHAR(10),"
   "PRIMARY KEY (type_id))")
   curs.execute("create table vehicle "
   "(serial_no CHAR(15), maker VARCHAR(20), model VARCHAR(20), year number(4,0),"
   "color VARCHAR(10),"
   "PRIMARY KEY (serial_no))")

   curs.execute("create table owner "
   "(owner_id CHAR(15), vehicle_id CHAR(15), is_primary_owner CHAR(1),"
   "PRIMARY KEY (owner_id, vehicle_id),FOREIGN KEY (owner_id) REFERENCES people,"
   "FOREIGN KEY (vehicle_id) REFERENCES vehicle, CHECK ( is_primary_owner IN ('y', 'n')))")

  
   print("defining tables all done")

   connection.commit()
Create_all_the_tables(connection,curs)
