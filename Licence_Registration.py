# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:13:31 2019

@author: root
"""


def LicenceRegistration(curs,connection):


   curs.execute("SELECT sin from people")
   real_col = set()
   list_sin_from_people_table = set(curs.fetchall())
   for i in list_sin_from_people_table:
      real_col.add(i[0].strip())


   curs.execute("SELECT licence_no from drive_licence")
   licence_no__drive_licence = set(curs.fetchall())
   real_licence_no__drive_licence = set()
   for i in licence_no__drive_licence:
      real_licence_no__drive_licence.add(i[0].strip())


   curs.execute("SELECT sin from drive_licence")
   ifalreadylicenced = set()
   list_of_sinfromdrivelicence = curs.fetchall()
   for i in list_of_sinfromdrivelicence:
      ifalreadylicenced.add(i[0].strip())


   sin = input("please enter sin number")



   while sin =='':
      sin = input("empty sin, please enter sin again or type exit to exit to main menu")
      if sin == "exit":
        return


   while sin in ifalreadylicenced:
      sin = input("this person with the sin already licenced. reenter the sin or type 'exit' to exit")
      if sin == "exit":
         return



   if sin not in real_col:
      choice = input("no sin found, would you like to add new person into people table? y/n")
      if choice =='y':
         #begin data collection for the new people
         p_name = input("please enter people name")
         p_height = input("please enter height")
         p_weight = input("please enter weight")
         p_eyecolor = input("please enter eyecolor")
         p_haircolor = input("please enter haircolor")
         p_addr = input("please enter address")
         p_gender = input("please enter gender. m/f")
         p_birthday = input("please enter birthday")
         confirm = input("confirm entering:({},{},{},{},{},{},{},{},{}) Enter y to confirm, n to return to main menu".format(sin,p_name,p_height,p_weight,p_eyecolor,p_haircolor,p_addr,p_gender,p_birthday))
         values = (sin,p_name,p_height,p_weight,p_eyecolor,p_haircolor,p_addr,p_gender,p_birthday)


         if confirm == 'y':
            curs.execute("INSERT INTO people VALUES "+str(values) )
            connection.commit()
         else:
            return


         licence_no = input("please enter license number")
         while licence_no in real_licence_no__drive_licence:
            licence_no = input("license number already exists, enter a unique one please")
         classs = input("please enter class")

         issuing_date = input("please enter issuing date")
         expiring_date = input("please enter expry date")
         confirm = input("confirm entering({},{},{},{},{}) enter y to confirm, n to exit to main menu".format(licence_no,sin,classs,issuing_date,expiring_date))



         if confirm == 'y':


            insert = """insert into drive_licence(licence_no, sin, class,issuing_date, expiring_date)
               values (:licence_no, :sin, :class, :issuing_date, :expiring_date)"""
            curs.execute(insert,{'licence_no':licence_no, 'sin':sin, 'class':classs, 'issuing_date':issuing_date, 'expiring_date':expiring_date})


         else:
            return


      elif choice =='n':
         exit_or_redo = input("would you like to reinput the sin number or exit driver licence registration input? input 'redo' or 'exit'")
         if exit_or_redo == 'exit':
            return
         elif exit_or_redo =='redo':
            LicenceRegistration(curs,connection)


   else:
      licence_no = input("please enter license number")
      while licence_no in real_licence_no__drive_licence:
         licence_no = input("license must be unique! please reenter")
      classs = input("please enter class")

      issuing_date = input("please enter issuing date")
      expiring_date = input("please enter expry date")
      confirm = input("confirm entering({},{},{},{},{}) enter y to confirm, n to exit to main menu".format(licence_no,sin,classs,issuing_date,expiring_date))
      if confirm =='y':


         insert = """insert into drive_licence(licence_no, sin, class,issuing_date, expiring_date)
               values (:licence_no, :sin, :class, :issuing_date, :expiring_date)"""
         curs.execute(insert,{'licence_no':licence_no, 'sin':sin, 'class':classs,  'issuing_date':issuing_date, 'expiring_date':expiring_date})
        
      else:
         return
   connection.commit()
