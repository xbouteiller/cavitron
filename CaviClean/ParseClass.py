import time
print('------------------------------------------------------------------------')
print('---------------                                    ---------------------')
print('---------------              CaviClean             ---------------------')
print('---------------                 V5.0               ---------------------')
print('----------------                                   ---------------------')
print('------------------------------------------------------------------------')
time.sleep(2)

num_col = ['PLC','Meas_cavispeed_rpm','Pressure_Mpa']
group_col=['Sampling_location', 'Treatment', 'Operator']
empty_col='Sample_ref_2'

# python setup.py develop

class ParseFile():
    import pandas as pd
    import numpy as np

    def __init__(self, path, skipfoot=43):
        '''
        initialization
        path of the file
        skipfoot : number of rows to skip at the end of the txt file

        portability : allow manual definition of skiprows and delimiter
                      test the file format and provide the good function for reading the file
        '''

        import pandas as pd
        import numpy as np
        self.file = pd.read_csv(path, skiprows=1, sep = ",")

    def desc_file(self):
        '''
        method for printing information of the file
        '''
        print(self.file.head())
        print("\n")
        print(self.file.tail())
        print("\n")
        print("\ndim of text file is :\n -nrow: {}\n -ncol: {}".format(self.file.shape[0],self.file.shape[1]))
        print("\n")


    def clean_file(self):
        '''
        clean the file
        '''
        import re
        import pandas as pd
        import numpy as np

        #drop full na
        self.file = self.file.dropna(axis = 0, how = 'all')

        # convert to numeric if possible
        self.file = self.file.apply(lambda x: pd.to_numeric(x, errors ="ignore"))

        # lower strings
        self.file = self.file.applymap(lambda s:s.lower() if (isinstance(s, str) and s!='None')  else s)

        return self.file



class ParseTreeFolder():

    def __init__(self):
        # super().__init__()
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename, askdirectory

        Tk().withdraw()
        folder = askdirectory(title='What is the root folder that you want to parse ?')
        self.path = folder.replace('/','\\')
        print('\n\n\nroot path is {}'.format(self.path))

        self.choices = {
        "1": self.do_nothing,
        "2": self.modify,
        "3": self.extract_strings,
        "4": self.erase,
        "5": self.extract_strings_and_nums
        }

    def _listdir_fullpath(self, p, s):
        import os
        import re
        d=os.path.join(p, s)
        return [os.path.join(d, f) for f in os.listdir(d) if re.search(r'^\d+\.csv|\d+\.\d+\.csv',f)]

    def parse_folder(self):
        '''
        parse the folder tree and store the full path to target file in a list
        '''
        import os
        import time
        import re

        file_root=[]
        self.listOfFiles = []

        # print(os.listdir(self.path))
        # for f in os.listdir(self.path):
        #     if re.search(r'^\d+\.csv|\d+\.\d+\.csv',f):
        #         print(os.path.join(self.path, f))

        try:
            file_root = [os.path.join(self.path, f) for f in os.listdir(self.path) if re.search(r'^\d+\.csv|\d+\.\d+\.csv',f)]
            self.listOfFiles.append(file_root)
            # print(file_root)
        except:
            print('no file detected within root directory')
            pass

        try:
            for pa, subdirs, files in os.walk(self.path):
                for s in subdirs:
                    self.listOfFiles.append(self._listdir_fullpath(p=pa, s=s))
        except:
            print('no file detected within childs directory')
            pass

        # [print(len(i)) for i in self.listOfFiles]
        # [print("- find : {0} matching files\n".format(len(i))) for i in self.listOfFiles]
        print('\n')
        try:
            [print("- find : {0} matching files in folder {1}".format(len(i),j)) for i,j in zip(self.listOfFiles, range(1,len(self.listOfFiles)+1))]
        except:
            print('no files detected at all')
            pass

        time.sleep(4)

        return self.listOfFiles

    def print_listofiles(self):
        '''
        print full path to target file
        '''
        # Print the files
        for elem in self.listOfFiles:
            print(elem)

    def _check_num(self, _df, _col):
        import pandas as pd
        check_num = _df[_col].applymap(lambda x: isinstance(x, (int, float))).apply(lambda x: all(x))

        # if all(check_num):
        #     print('columns {} are numeric'.format(_col))
        # else:
        #     print('at least one value is not numeric')

        return [all(check_num), check_num]


    def _check_group(self, _df, _col):

        check_group = [len(_df[c].unique())==1 for c in _col]

        # if all(check_group):
        #     print('group are ok'.format(_col))
        # else:
        #     print('at least one group is not ok')

        return [all(check_group), check_group]


    def _check_empty(self, _df, _col):

        import pandas as pd
        check_empty = self.frame[_col].isna()

        # if any(check_empty):
        #     print('\n\n------------------------------------------')
        #     print('one value of {} is empty'.format(_col))
        # else:
        #     print('\n\n------------------------------------------')
        #     print('contains no empty value'.format(_col))

        return [any(check_empty), check_empty]



    def _get_valid_input(self, input_string, valid_options):
        input_string += "({}) ".format(", ".join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response

    def display_menu(self):
        print("""
        --------------------
        List of actions

        1. do nothing
        2. modify
        3. extract strings
        4. erase rows
        5. extract strings and numbers
        """)

    def run(self):
        '''Display the menu and respond to choices.'''

        self.display_menu()
        choice = input("Enter an option: ")
        action = self.choices.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))
            self.run()

    def do_nothing(self):
        print('chose to do nothing\n')
        pass

    def modify(self):
        import numpy as np
        import pandas as pd
        print('choose to do modify')

        while True:
            try:
                nval = int(input('how many values do you want to modify ? '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        for i in np.arange(0,nval):
            tobemodified = input('Which value do you want to change ? ')
            newvalue = input('What is the new value ? ')
            self.frame.loc[self.frame[self.i]==tobemodified,self.i] = newvalue
            print('new values are {}'.format(self.frame[self.i].unique()))
            input('press any key to continue')

    def extract_strings(self):
        print('choose to extract strings')
        import re
        import numpy as np

        print('col',self.frame[self.i])


        self.frame[self.i]=self.frame[self.i].str.extract('([a-zA-Z]+)', expand = False)

        print('modified to {}'.format(self.frame[self.i].unique()))
        inp=input('press any key to continue --- or enter 1 to modify values ---')
        if inp == str(1):
            self.modify()
        else:
            print('no values to be modified')

    def extract_strings_and_nums(self):
        print('choose to extract strings and numbers')
        import re
        import numpy as np
        # print('col',self.frame[self.i])
        reg = self.frame[self.i].str.extract('([a-zA-Z]+)\W(\d+)', expand = False)

        self.frame[self.i]=reg[0]
        self.frame['Sample_ref_2']=reg[1]#.astype('int')
        print('modified {} to {}'.format(self.i, self.frame[self.i].unique()))
        print('modified "Sample_ref_2" to {}'.format(self.frame['Sample_ref_2'].unique()))

        inp=input('press any key to continue --- or enter 1 to modify {} values ---'.format(self.i))
        if inp == str(1):
            self.modify()
        else:
            print('no values to be modified')

    def erase(self):
        import numpy as np
        import pandas as pd
        print('choose to do erase rows')
        while True:
            try:
                nval = int(input('how many values do you want to erase ? '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")


        for i in np.arange(0,nval):
            tobemodified = input('Which row value do you want to erase ? ')
            self.frame=self.frame[self.frame[self.i]!=tobemodified]
            print('new values are {}'.format(self.frame[self.i].unique()))
            input('press any key to continue')


    def check_frame_num(self):
        import pandas as pd
        all_cn, cn = self._check_num(_df = self.frame , _col= num_col)
        # cn = self._check_num(_df = self.frame , _col= num_col)[1]

        # if not all_cn:
        #     print('\n -----------------------')
        #     [print('col {} is Numeric'.format(i)) if j else print('col {} is not Numeric'.format(i)) for i, j in zip(num_col, cn)]
        #     input('press any key to continue')
        if not all_cn:
            print('\n ---------------------------------------------------------------------')
            [print('col {} is Numeric'.format(i)) if j else print('col {} is not Numeric'.format(i)) for i, j in zip(num_col, cn)]

            for i, j in zip(num_col, cn):
                if not j:
                    self.i=i
                    # I want to register on my log the message recived on ORIGINAL VALUE
                    # print(self.frame[self.i].head())
                    mask = pd.to_numeric(self.frame[self.i], errors='coerce').isna()
                    #if possible missing values
                    # mask = pd.to_numeric(df['ORIGINAL_VALUE'].fillna('0'), errors='coerce').isna()
                    L = self.frame.loc[mask, self.i].tolist()
                    print('\nin col {}'.format(self.i))
                    print ("Not converted to numeric values are: " + ", ".join(L))

                    print('What do you want to do ? ')
                    self.run()



    def check_frame_group(self):
            all_cg, cg= self._check_group(_df = self.frame , _col = group_col)#[0]
            # cg = self._check_group(_df = self.frame , _col = group_col)[1]
            if not all_cg:
                print('\n ---------------------------------------------------------------------')
                [print('label of col {} is unique'.format(i)) if j else print('label of col {} is NOT unique'.format(i)) for i, j in zip(group_col, cg)]

                for i, j in zip(group_col, cg):
                    if not j:
                        self.i=i
                        print('labels of col {} are {}\nWhat do you want to do ?'.format(self.i, self.frame[self.i].unique()))
                        self.run()

    def _compute_empty(self):
        self.frame[empty_col]=self.frame[empty_col].fillna(self.frame['Sample_ref_1']-self.frame['Sample_ref_1'].min())
        print('new value in {} are {}'.format(empty_col, self.frame[empty_col].unique()))
        input('press any key to continue')

    def _manual_empty(self):
        for man in self.frame['Sample_ref_1'].unique():
            if any(self.frame.loc[self.frame['Sample_ref_1']==man, empty_col].isna()):
                while True:
                    try:
                        newvalue= int(input('What is the identifiant for "ref number 2" for individual {}: '.format(man)))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                self.frame.loc[self.frame['Sample_ref_1']==man,empty_col]=newvalue
            else:
                pass

        print('new value in {} are {}'.format(empty_col, self.frame[empty_col].unique()))
        input('press any key to continue')

    def _extract_empty(self):
        self.frame[empty_col]=self.frame[empty_col].fillna(self.frame['Comment'].str.extract('(\d+)', expand = False))
        print('new value in {} are {}'.format(empty_col, self.frame[empty_col].unique()))
        input('press any key to continue')

    def check_frame_empty(self):
        any_empty, empty = self._check_empty(_df = self.frame , _col= empty_col)

        while any_empty:
            print('\n ---------------------------------------------------------------------')
            print('parsing list of files from : {}\n'.format(self.presentfile))

            print('{} contains empty values'.format(empty_col))
            print('value in Comment columns are {}'.format(self.frame['Comment'].unique()))
            print('''
            --------------------
            List of actions

            1: do nothing
            2: calculate from 1 to n
            3: extract numbers from Comment columns
            4: enter values manually
            ''')
            wtd = self._get_valid_input('What do you want to do ? Choose one of : ', ('1','2', '3', '4'))
            if wtd == '1':
                break
            if wtd == '2':
                self._compute_empty()
                any_empty = self._check_empty(_df = self.frame , _col= empty_col)[0]
            if wtd == '3':
                self._manual_empty()
                any_empty = self._check_empty(_df = self.frame , _col= empty_col)[0]
            if wtd == '4':
                self._extract_empty()
                any_empty = self._check_empty(_df = self.frame , _col= empty_col)[0]

        print('\nExiting from empty verification\nnew value in {} are {}'.format(empty_col, self.frame[empty_col].unique()))


    def _inactive_indiv(self):
        while True:
            try:
                newvalue= int(input('What is the identifiant of the individual that you want to inactive ? '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        while True:
            if newvalue in self.frame['Sample_ref_1'].unique():
                break
            else:
                print("Oops! identifiant not existing choose one among : {}".format(self.frame['Sample_ref_1'].unique().tolist()))
                while True:
                    try:
                        newvalue= int(input('What is the identifiant of the individual that you want to inactive ? '))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")

        self.frame.loc[self.frame['Sample_ref_1']==newvalue,'Note']='yes'


    def inactive_indiv(self):
        print('\n ---------------------------------------------------------------------')
        print('\nDo you want to inactive (turn to yes) some individuals ? ')

        print('''
        --------------------
        List of actions

        1: no, escape and continue
        2: yes, inactive some individuals
        ''')
        wtd = self._get_valid_input('What do you want to do ? Choose one of : ', ('1','2'))

        if wtd == '2':
            inactive = True
        else:
            inactive = False

        while inactive:
            self._inactive_indiv()
            exit = input('press any key to continue or enter -- exit -- to stop ')
            if exit == 'exit' or exit == 'e':
                inactive = False

        L = self.frame.loc[self.frame['Note']=='yes','Sample_ref_1'].unique().tolist()
        L = [str(i) for i in L]
        print('\nExiting from inactivating individuals\ninactivated individuals are : ' + ", ".join(L))


    def _change_values(self):

        num_col = ['PLC','Meas_cavispeed_rpm','Pressure_Mpa']
        group_col=['Sampling_location', 'Treatment', 'Operator']
        empty_col='Sample_ref_2'


        print('''
        --------------------
        Columns that you can change

        1: Sample_ref_2 (tree number)
        2: Sampling_location
        3: Treatment
        4: Operator
        5: Note
        ''')
        ctc = self._get_valid_input('What do you want to do ? Choose one of : ', ('1','2','3','4','5'))

        if ctc == '1':
            col_to_change = 'Sample_ref_2'
        if ctc == '2':
            col_to_change = 'Sampling_location'
        if ctc == '3':
            col_to_change = 'Treatment'
        if ctc == '4':
            col_to_change = 'Operator'
        if ctc == '5':
            col_to_change = 'Note'

        print('\nmodified column will be : {}'.format(col_to_change))

        while True:
            try:
                newvalue= int(input('What is the identifiant of the individual that you want to change ? '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        while True:
            if newvalue in self.frame['Sample_ref_1'].unique():
                break
            else:
                print("Oops! identifiant not existing choose one among : {}".format(self.frame['Sample_ref_1'].unique().tolist()))
                while True:
                    try:
                        newvalue= int(input('What is the identifiant of the individual that you want to change ? '))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")

        modified_value= input('\nWhat is the new value that you want to change for individual {} in column {} ? '.format(newvalue, col_to_change))
        self.frame.loc[self.frame['Sample_ref_1']==newvalue,col_to_change]=modified_value
        # print(self.frame.loc[self.frame['Sample_ref_1']==newvalue,col_to_change])
        assert self.frame.loc[self.frame['Sample_ref_1']==newvalue,col_to_change].unique().tolist() == [modified_value], 'pb with new value'

    def manual_change(self):
                print('\n ---------------------------------------------------------------------')
                print('\nDo you want to change manually some values ? ')

                print('''
                --------------------
                List of actions

                1: no, escape and continue
                2: yes, change manually some individuals values
                ''')
                wtd = self._get_valid_input('What do you want to do ? Choose one of : ', ('1','2'))

                if wtd == '2':
                    change = True
                else:
                    change = False

                while change:
                    self._change_values()
                    exit = input('press any key to continue or enter -- exit -- to stop ')
                    if exit == 'exit' or exit == 'e':
                        change = False



    def append_values(self):
        '''
        method for filling the lists
        '''

        import numpy as np
        import pandas as pd

        dimfolder = len(self.listOfFiles)


        li_all = []
        for d in np.arange(0,dimfolder):
            print('\n\n\n---------------------------------------------------------------------')
            print(d)
            li = []
            try:
                self.presentfile=self.listOfFiles[d][0]
            except:
                self.presentfile = 'No file'
            print('parsing list of files from : {}'.format(self.presentfile))

            if self.presentfile != 'No file':
                for elem in self.listOfFiles[d]:
                    # print(elem)
                    df = ParseFile(path = elem).clean_file()
                    # print(df)
                    li.append(df)

                self.frame = pd.concat(li, axis=0, ignore_index=True, sort=False)
                print('shape of frame is {}'.format(self.frame.shape))
                self.check_frame_num()
                self.check_frame_group()
                self.check_frame_empty()
                self.inactive_indiv()
                self.manual_change()
                li_all.append(self.frame)
                #check integrity
            else:
                print('skip empty folder')
                pass

        self.final_frame = pd.concat(li_all, axis=0, ignore_index=True, sort=False)
        print('shape of final frame is {}'.format(self.final_frame.shape))

        return self.final_frame


    def save_finaldf(self):
        '''
        saved the concatened df into a csv file
        '''
        import pandas as pd

        FileSaveName = input('enter final file name : ') or 'DefaultTable'
        FileSaveName += '.csv'
        self.final_frame.to_csv(FileSaveName,index=False, header=True)
        print('saved file {}'.format(FileSaveName))
