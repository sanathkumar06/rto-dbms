# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:11:32 2019

@author: root
"""

import sys
import sqlite3

def Search1(curs, connection):



   curs.execute("SELECT name from people p, drive_licence dl where p.sin = dl.sin")
   s1_col_pname = curs.fetchall()
   namelist = []
   for row in s1_col_pname:
      namelist.append(row[0].strip())


   curs.execute("SELECT licence_no FROM drive_licence")
   s1_col_dllicence = curs.fetchall()
   licencelist = []
   for row in s1_col_dllicence:
      licencelist.append(row[0].strip())


   ask = input("Do you want to enter a licence number or a name? (1/2)\n")
   while ask not in ['1', '2']:
      ask = input("Invalid Input. Licence number or name? (1/2)\n")

   # Licence number inputs
   if ask == '1':
      search_input = input("Input search term: ")
      if search_input == "":
         print("Invalid Input. Input a new search term: ")

      # Checks if the user input is a real licence in the list
      elif search_input in licencelist:
         curs.execute("SELECT p.name, dl.licence_no, p.addr, p.birthday, dl.class, dc.description, dl.expiring_date "
               "from people p, drive_licence dl, driving_condition dc, restriction dr " +
               "where dl.sin = p.sin and dl.licence_no = '" + search_input + "' and dr.licence_no = '" + search_input + "' and dr.r_id = dc.c_id")
         output = curs.fetchall()


         if output == []:
            curs.execute("SELECT p.name, dl.licence_no, p.addr, p.birthday, dl.class, dl.expiring_date "
               "from people p, drive_licence dl "
               "where dl.sin = p.sin and dl.licence_no = '" + search_input + "'")
            output = curs.fetchall()

            # Prints the new ouput from the new query
            for row in output:
               print("\n")
               display = []
               for i in row:
                  display.append(i)
               print("Driver Name: " + display[0])
               print("Licence Number: " + display[1])
               print("Address: " + display[2])
               print("Birthday: " + display[3])
               print("Driving Class: " + display[4])

               print("Expiring Date: ",display[5])
            return

         # If they do have a driving condition print the relevant information
         else:
            for row in output:
               print("\n")
               display = []
               for i in row:
                  display.append(i)
               print("Driver Name: " + display[0])
               print("Licence Number: " + display[1])
               print("Address: " + display[2])
               print("Birthday: " + display[3])
               print("Driving Class: " + display[4])

               print("Expiring Date: " + display[6])
            return


      else:
         redo = input("No results found. Redo search or exit to search menu? Redo/Exit")
         if redo == 'redo':
            Search1(curs, connection)
         else:
            return

   # Name Inputs
   else:
      search_input = input("Input search term: ")
      if search_input == "":
         print("Invalid Input. Input a new search term: ")


      elif search_input in namelist:
         curs.execute("SELECT p.name, dl.licence_no, p.addr, p.birthday, dl.class, dc.description, dl.expiring_date " +
               "from people p, drive_licence dl, driving_condition dc, restriction dr " +
               "where p.name = '" + search_input + "' and dl.sin = p.sin and dl.licence_no = dr.licence_no and dr.r_id = dc.c_id")
         output = curs.fetchall()

         # If they do not have a driving condition
         if output == []:
            curs.execute("SELECT p.name, dl.licence_no, p.addr, p.birthday, dl.class, dl.expiring_date "
               "from people p, drive_licence dl "
               "where p.name = '" + search_input + "' and dl.sin = p.sin ")
            output = curs.fetchall()

            # Print the ouput from the new query
            for row in output:
               print("\n")
               display = []
               for i in row:
                  display.append(i)
               print("Driver Name: " + display[0])
               print("Licence Number: " + display[1])
               print("Address: " + display[2])
               print("Birthday: " + display[3])
               print("Driving Class: " + display[4])

               print("Expiring Date: ",display[5])
            return

         # If they do have a driving condition print the relevant information
         else:
            for row in output:
               print("\n")
               display = []
               for i in row:
                  display.append(i)
               print("Driver Name: " + display[0])
               print("Licence Number: " + display[1])
               print("Address: " + display[2])
               print("Birthday: " + display[3])
               print("Driving Class: " + display[4])

               print("Expiring Date: ", display[6])
            return

      # If no results are found
      else:
         redo = input("No results found. Redo search or exit to search menu? Redo/Exit ")
         if redo == 'redo':
            Search1(curs, connection)
         else:
            return






def Search3(curs,connection):

   curs.execute("SELECT serial_no FROM vehicle")         # Add all the serial_no from vehicle into a list to check for any invalid serial_no.
   s3_col_vserial = curs.fetchall()
   vrowlst = []
   for vrow in s3_col_vserial:
      vrowlst.append(vrow[0].strip())

   serial_no = input("Enter vehicle serial number: ").strip()  # Ask user to enter a serial_no.

   while serial_no == "" or serial_no not in vrowlst:    # Raise error if user enter blank or non-existing serial_no.
      if serial_no not in vrowlst:
         serial_no = input("Vehicle already does not exist in database. Serial Number? or type 'exit' to main menu ").strip()

         if serial_no == "exit":
            return None
      elif serial_no == "":
         serial_no = input("Input cannot be blank. Serial Number? or type 'exit' to main menu ").strip()

         if serial_no == "exit":
            return None


   curs.execute("select serial_no, maker, model, year, color  from vehicle  where serial_no = '"+serial_no+"' ")
   # Print out all the output.
   v_history = curs.fetchall()
   for v_history_row in v_history:
      print("Serial Number: ", v_history_row[0])
      print("Maker: ", v_history_row[1])
      print("Model: ", v_history_row[2])
      print("Year: ", v_history_row[3])
      print("Colour: ",v_history_row[4])
      
