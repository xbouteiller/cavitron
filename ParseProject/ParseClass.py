class ParseFile():
    import pandas as pd
    import numpy as np

    def __init__(self, path, skipfoot=43):
        import pandas as pd
        import numpy as np
        self.textfile = pd.read_table(path, skiprows=3,  skipfooter=skipfoot, engine = 'python', delimiter='\s+')

    def desc_textfile(self):
        print(self.textfile.head())
        print("\n")
        print(self.textfile.tail())
        print("\n")
        print("\ndim of text file is :\n -nrow: {}\n -ncol: {}".format(self.textfile.shape[0],self.textfile.shape[1]))

    def extract_values(self, param):
        self.param = param
        self.val = self.textfile.loc[self.textfile.index == param, ['mu.vect', '50%', '2.5%','97.5%']]
        return self.val

    def print_extractedvalues(self):
        print('\nparam is:\n{}'.format(self.param))
        print('\nextracted values are:\n{}'.format(self.val))


class ParseTreeFolder(ParseFile):

    def __init__(self):
        super()

    def parse_folder(self, path_folder, targetfilename):
        import os
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(path_folder):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.lower() == targetfilename]
        self.listOfFiles = listOfFiles


    def print_listofiles(self):
        # Print the files
        for elem in self.listOfFiles:
            print(elem)

    def instantiate_list(self):

        self.Parameter = []
        self.Folder = []
        self.Value = []
        print("Parameter, Folder, Value lists instantiated")

    def append_values(self, param, skipfoot=43, mode = 3):
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
        import pandas as pd
        import numpy as np

        Parameterdf=pd.DataFrame(self.Parameter)
        Valuedf=pd.DataFrame(self.Value)
        Folderdf=pd.DataFrame(self.Folder)

        self.finaldf = pd.concat([Parameterdf, Folderdf, Valuedf], axis=1)
        colname = ['parameter'] +['path_'+str(i) for i in range(0,self.mode+1)]+ ['mu.vect', '50%', '2.5%','97.5%' ]
        self.finaldf.columns = colname

    def save_finaldf(self, FileSaveName):
        import pandas as pd
        self.finaldf.to_csv(FileSaveName,index=False, header=True)
        print('saved file {}'.format(FileSaveName))
