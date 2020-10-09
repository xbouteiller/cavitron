import time
print('------------------------------------------------------------------------')
print('---------------                                    ---------------------')
print('---------------             CavitClean             ---------------------')
print('---------------                 V2.0               ---------------------')
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
        # print(self.file.dtypes)

    def clean_file(self):
        '''
        clean the file
        '''
        import re
        import pandas as pd
        import numpy as np

        #drop full na
        self.file = self.file.dropna(axis = 0, how = 'all')
        self.file = self.file.dropna(axis = 1, how = 'all')
        # self.file = self.file.fillna('None') ###################
        # remove ;
        # self.file = self.file.applymap(lambda x: re.sub(';', '', str(x) if x is not np.nan else x))

        # convert to numeric if possible
        self.file = self.file.apply(lambda x: pd.to_numeric(x, errors ="ignore"))

        # lower strings
        self.file = self.file.applymap(lambda s:s.lower() if (isinstance(s, str) and s!='None')  else s)
        # self.file = self.file.applymap(lambda s:s.lower() if (isinstance(s, str) and s!='None')  else s)

        return self.file

    # def _check_num(self, col):
    #     import pandas as pd
    #     check_num = self.file[col].applymap(lambda x: isinstance(x, (int, float))).apply(lambda x: all(x))
    #     self.check_num = check_num
    #     if all(check_num):
    #         print('columns {} are numeric'.format(col))
    #     else:
    #         print('at least one value is not numeric')
    #
    # def _check_group(self, col):
    #
    #     check_group = [len(self.file[c].unique())==1 for c in col]
    #     self.check_group = check_group
    #     if all(check_group):
    #         print('group are ok'.format(col))
    #     else:
    #         print('at least one group is not ok')
    #
    #
    # def assess_file(self, num_col = num_col, group_col= group_col):
    #     '''
    #     print the values extracted from the file
    #     '''
    #     self._check_num(col = num_col)
    #     self._check_group(col = group_col)





class ParseTreeFolder():

    def __init__(self, path):
        # super().__init__()
        self.path = path

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
        self.listOfFiles = []
        for pa, subdirs, files in os.walk(self.path):
            for s in subdirs:
                self.listOfFiles.append(self._listdir_fullpath(p=pa, s=s))

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

        if all(check_num):
            print('columns {} are numeric'.format(_col))
        else:
            print('at least one value is not numeric')

        return [all(check_num), check_num]


    def _check_group(self, _df, _col):

        check_group = [len(_df[c].unique())==1 for c in _col]

        if all(check_group):
            print('group are ok'.format(_col))
        else:
            print('at least one group is not ok')

        return [all(check_group), check_group]


    def _check_empty(self, _df, _col):

        import pandas as pd
        check_empty = self.frame[self.i].isna()

        if any(check_empty):
            print('one value of {} is empty'.format(_col))
        else:
            print('contains no empty value').format(_col))

        return [any(check_empty), check_empty]



    def _get_valid_input(self, input_string, valid_options):
        input_string += "({}) ".format("\n,\n ".join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response

    def display_menu(self):
        print("""
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
        print('chose to do nothing')
        pass
    def modify(self):
        import numpy as np
        import pandas as pd
        print('choose to do modify')

        while True:
            try:
                nval = int(input('how many values do you want to modify ?'))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        for i in np.arange(0,nval):
            tobemodified = input('Which value do you want to change ?')
            newvalue = input('What is the new value ?')
            self.frame.loc[self.frame[self.i]==tobemodified,self.i] = newvalue
            print('new values are {}'.format(self.frame[self.i].unique()))
            input('press any key to continue')

    def extract_strings(self):
        print('choose to extract strings')
        import re
        import numpy as np
        # print(self.frame[self.i])
        # self.frame[self.i] =  self.frame[self.i]
        # reg = [re.findall(r'[a-zA-Z]+', f) for f in self.frame[self.i]] #if f!='None' else f[0]
        # reg=[]
        print('col',self.frame[self.i])
        # for f in self.frame[self.i].values:
        #     print('f',f)
        #     if f==np.nan:
        #         reg.append(np.nan)
        #     else:
        #         reg.append(re.findall(r'[a-zA-Z]+', f))

        self.frame[self.i]=self.frame[self.i].str.extract('([a-zA-Z]+)', expand = False)

        # self.frame[self.i]=np.array(reg)
        # print('modified to {}'.format(np.unique(np.array(reg))))
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
        print('col',self.frame[self.i])
        reg = self.frame[self.i].str.extract('([a-zA-Z]+)\W(\d+)', expand = False)
        print(reg)
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
        nval = int(input('how many values do you want to erase ?'))
        for i in np.arange(0,nval):
            tobemodified = input('Which row value do you want to erase ?')
            self.frame=self.frame[self.frame[self.i]!=tobemodified]
            print('new values are {}'.format(self.frame[self.i].unique()))
            input('press any key to continue')

    def append_values(self):
        '''
        method for filling the lists
        '''

        import numpy as np
        import pandas as pd

        dimfolder = len(self.listOfFiles)


        li_all = []
        for d in np.arange(0,dimfolder):
            print('------------------------------------------')
            print(d)
            li = []
            for elem in self.listOfFiles[d]:
                print(elem)
                df = ParseFile(path = elem).clean_file()
                # print(df)
                li.append(df)

            self.frame = pd.concat(li, axis=0, ignore_index=True, sort=False)
            print('shape of frame is {}'.format(self.frame.shape))

            all_cn = self._check_num(_df = self.frame , _col= num_col)[0]
            cn = self._check_num(_df = self.frame , _col= num_col)[1]

            if not all_cn:
                print('\n -----------------------')
                [print('col {} is Numeric'.format(i)) if j else print('col {} is not Numeric'.format(i)) for i, j in zip(num_col, cn)]
                input('-NUM ALERT- press any key to continue')

            all_cg = self._check_group(_df = self.frame , _col = group_col)[0]
            cg = self._check_group(_df = self.frame , _col = group_col)[1]
            if not all_cg:
                print('\n -----------------------')
                [print('label of col {} is unique'.format(i)) if j else print('label of col {} is NOT unique'.format(i)) for i, j in zip(group_col, cg)]
                # [i if j else print('labels of col {} are {}'.format(i, frame[i].unique())) for i, j in zip(group_col, cg)]

                for i, j in zip(group_col, cg):
                    if not j:
                        self.i=i
                        print('labels of col {} are {}\nWhat do you want to do ?'.format(self.i, self.frame[self.i].unique()))
                        self.run()

            any_empty = self._check_empty(_df = self.frame , _col= empty_col)[0]
            empty = self._check_empty(_df = self.frame , _col= empty_col)[1]
            if any_empty:
                print('{} contains empty values'.format(empty_col))
                print('value in Comment columns are {}'.format(self.frame['Comment'].unique()))
                wtd = _get_valid_input(self, 'What do you want to do ?', ('nothing', 'replace'))
                if wtd == 'nothing':
                    pass
                else:
                    self.frame[empty_col]=self.frame[empty_col].fillna(self.frame['Comment'].str.extract('(\d+)', expand = False))
                    print('new value in {} are {}'.format(empty_col, self.frame[empty_col].unique()))

            li_all.append(self.frame)

            #check integrity

        self.final_frame = pd.concat(li_all, axis=0, ignore_index=True, sort=False)
        print('shape of final frame is {}'.format(self.final_frame.shape))

        return self.final_frame



    def save_finaldf(self):
        '''
        saved the concatened df into a csv file
        '''
        import pandas as pd
        FileSaveName = input('enter final file name:') or 'DefaultTable'
        FileSaveName += '.csv'
        self.final_frame.to_csv(FileSaveName,index=False, header=True)
        print('saved file {}'.format(FileSaveName))
