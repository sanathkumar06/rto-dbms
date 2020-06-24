# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:53:04 2019

@author: root
"""

import sqlite3
import getpass
from VehicleRegistration import *
#from database_create import *
from Licence_Registration import *
from Search_Functions import *


connection = sqlite3.connect('gaadinew.db')
curs = connection.cursor()


def SearchEngine(curs, connection):
    while True:
        print("")
        print("| '1' Driving Licence                |")        
        print("| '2' Vehicle Registration                |")
        print("| press any other key to exit |")
        print("")
        key = input("selection please:  ")
        print(key)
        if key == '1':
            print('')
            Search1(curs,connection)
        elif key =='2':
            Search3(curs,connection)
        else:
            return

def applications(curs,connection):
    exit_code = False
    while exit_code == False:
        print("")
        print("| 'N' New Vehicle Registration    |")
        print("| 'R' Driver Licence Registration |")
        print("| 'S' Search Engine               |")
        print("| '0' exit                        |")
        print("")
        key = input("Input a key: ")
        if key == 'n' or key == 'N':
            print("")
            VehicleRegistration(curs, connection)
        elif key == 'r' or key == 'R':
            print("")
            LicenceRegistration(curs, connection)
        elif key == 's' or key == 'S':
            print("")
            SearchEngine(curs, connection)
        elif key =='0':
            return
        else:
            print("")
            print("Invalid input, please enter a valid key")


applications(curs,connection)
