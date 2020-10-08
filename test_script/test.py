# import pandas as pd
#
#
# df = pd.read_table("bilan.txt", skiprows=3,  skipfooter =43, engine = 'python', delimiter='\s+')
#
# df.head()
# df.tail()
#
#
#
#
#
#
#
# "C:\\Users\\Xavier\\Thèse\\EXP 2017\\Suivi EXP\\AVRIL18\\PHEN\\inter\\Total weight GR\\bilan.txt".split('\\')
#
# import numpy as np
# np.array("C:\\Users\\Xavier\\Thèse\\EXP 2017\\Suivi EXP\\AVRIL18\\PHEN\\inter\\Total weight GR\\bilan.txt".split('\\'))[-4:-1]

if __name__=="__main__":

    #%% Dependencies
    import os
    import argparse
    # from ParseClass import ParseFile

    # Permet de récupérer les arguments de la commande shell
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--source', help='the source folder', type = str )
    # parser.add_argument('--param', default = 'QST', help='the parameter value', type = str )
    # parser.add_argument('--filename', help='the target filename', default='bilan.txt', type = str )
    # parser.add_argument('--skipfoot', help='the number of lines to skip from the end', default=43, type = int )
    # parser.add_argument('--mode', help='number of folders to save', default=3, type = int )
    # parser.add_argument('--savename', help='the saved filename', default='extractedvalue.csv', type = str )
    # args = parser.parse_args()
    #

    rootdir =  "E:/FORMANRISK/Formanrisk Mimizan/252.csv" #args.source
    # paramtoextract = args.param
    # filenametoparse = args.filename
    # skipfoottodel =  args.skipfoot
    # modefolder = args.mode
    # savename = args.savename

    from ParseProject.ParseClass import ParseFile, ParseTreeFolder



    parse_file = ParseFile(rootdir)
    parse_file.desc_file()
    parse_file.clean_file()
    parse_file.desc_file()


    parse_file.assess_file()

    parse_file.file.loc[0,['Pressure_Mpa']]='a'
    parse_file.file.loc[0,['Sampling_location']]='mza'

    parse_file.assess_file()



    #
    # [print(i) for i in parse_file.file]
    #
    # print(parse_file.file[['Pressure_Mpa']])
    # print(parse_file.file[['Rawdata_DISTANCE_pixel']])
    # print(parse_file.file[['Sampling_location']])


class Menu:
'''Display a menu and respond to choices when run.'''
def __init__(self):
self.notebook = Notebook()
self.choices = {
"1": self.show_notes,
"2": self.search_notes,
"3": self.add_note,
"4": self.modify_note,
"5": self.quit
}
def display_menu(self):
print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")
def run(self):
'''Display the menu and respond to choices.'''
while True:
self.display_menu()
choice = input("Enter an option: ")
action = self.choices.get(choice)
if action:
action()
else:
print("{0} is not a valid choice".format(choice))
def show_notes(self, notes=None):
if not notes:
notes = self.notebook.notes


def get_valid_input(input_string, valid_options):
  input_string += "({}) ".format(", ".join(valid_options))
  response = input(input_string)
  while response.lower() not in valid_options:
    response = input(input_string)
  return response


get_valid_input("what laundry?", ("coin", "ensuite", "none"))


import sys
from notebook import Notebook, Note
class Menu:
'''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.quit
            }
    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
        notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
            note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")
    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
