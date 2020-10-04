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

        # remove ;
        # self.file = self.file.applymap(lambda x: re.sub(';', '', str(x) if x is not np.nan else x))

        # convert to numeric if possible
        self.file = self.file.apply(lambda x: pd.to_numeric(x, errors ="ignore"))

        # lower strings
        self.file = self.file.applymap(lambda s:s.lower() if isinstance(s, str) else s)


    def _check_num(self, col):
        import pandas as pd
        check_num = self.file[col].applymap(lambda x: isinstance(x, (int, float))).apply(lambda x: all(x))
        self.check_num = check_num
        if all(check_num):
            print('columns {} are numeric'.format(col))
        else:
            print('at least one value is not numeric')

    def _check_group(self, col):

        check_group = [len(self.file[c].unique())==1 for c in col]
        self.check_group = check_group
        if all(check_group):
            print('group are ok'.format(col))
        else:
            print('at least one group is not ok')


    def assess_file(self, num_col = ['PLC','Meas_cavispeed_rpm','Pressure_Mpa'],
                          group_col=['Sampling_location', 'Treatment', 'Operator']):
        '''
        print the values extracted from the file
        '''
        self._check_num(col = num_col)
        self._check_group(col = group_col)





class ParseTreeFolder(ParseFile):

    def __init__(self):
        super()

    def parse_folder(self, path_folder, targetfilename):
        '''
        parse the folder tree and store the full path to target file in a list
        '''
        import os
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(path_folder):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.lower() == targetfilename]
        self.listOfFiles = listOfFiles


    def print_listofiles(self):
        '''
        print full path to target file
        '''
        # Print the files
        for elem in self.listOfFiles:
            print(elem)

    def instantiate_list(self):
        '''
        instantiate empty list for appending and storing extracted value
        '''

        self.Parameter = []
        self.Folder = []
        self.Value = []
        print("Parameter, Folder, Value lists instantiated")

    def append_values(self, param, skipfoot=43, mode = 3):
        '''
        method for filling the lists

        fill 3 lists with the values extracted from each file

        1 with the paramater extracted
        1 with the path splitted in several columns
        1 with extracted values

        attributes
        self.Parameter
        self.Folder
        self.Value
        '''
        import numpy as np
        self.mode = mode
        for elem in self.listOfFiles:
            pf = ParseFile(elem, skipfoot=skipfoot)
            val = pf.extract_values(param=param)

            par_list = [pf.param]
            par_fold = elem.split('\\')[(-mode-1):] # replace / by \\
            par_val = val.values.tolist()[0]

            self.Parameter.append(par_list)
            self.Folder.append(par_fold)
            self.Value.append(par_val)

    def make_value_df(self):
        '''
        concat the 3 lists into the same data frame

        attributes:
        self.finaldf
        '''
        import pandas as pd
        import numpy as np

        Parameterdf=pd.DataFrame(self.Parameter)
        Valuedf=pd.DataFrame(self.Value)
        Folderdf=pd.DataFrame(self.Folder)

        self.finaldf = pd.concat([Parameterdf, Folderdf, Valuedf], axis=1)
        colname = ['parameter'] +['path_'+str(i) for i in range(0,self.mode+1)]+ ['mu.vect', '50%', '2.5%','97.5%' ]
        self.finaldf.columns = colname

    def save_finaldf(self, FileSaveName):
        '''
        saved the concatened df into a csv file
        '''
        import pandas as pd
        self.finaldf.to_csv(FileSaveName,index=False, header=True)
        print('saved file {}'.format(FileSaveName))

    def make_crosstab(self, choice="50%", print_tab = False):
        '''
        make a crosstab
        '''

        import pandas as pd

        self.finaldf['appended'] =  self.finaldf['path_' + str(self.mode-2)] + '$' + self.finaldf['path_' + str(self.mode-1)]
        self.finaldf[['path_' + str(self.mode), choice]]
        self.pivoteddf = self.finaldf.pivot(index = 'path_' + str(self.mode-1), columns='path_' + str(self.mode-2) , values=choice)
        if print_tab:
            print(self.pivoteddf )

    def plot_heatmap(self):
        '''
        print heatmap
        '''
        import matplotlib.pyplot as plt
        import numpy as np

        fig, ax = plt.subplots()
        im = ax.imshow(self.pivoteddf)

        # We want to show all ticks...
        ax.set_yticks(np.arange(self.pivoteddf.shape[0]))
        ax.set_xticks(np.arange(self.pivoteddf.shape[1]))
        # ... and label them with the respective list entries
        ax.set_yticklabels(self.pivoteddf.index)
        ax.set_xticklabels(self.pivoteddf.columns)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

         # Loop over data dimensions and create text annotations.
        for i in range(self.pivoteddf.shape[0]):
            for j in range(self.pivoteddf.shape[1]):
                text = ax.text(j, i, np.round(self.pivoteddf.iloc[i, j]*100,2),
                               ha="center", va="center", color="w")

        plt.show()
