import pandas as pd


df = pd.read_table("bilan.txt", skiprows=3,  skipfooter =43, engine = 'python', delimiter='\s+')

df.head()
df.tail()







"C:\\Users\\Xavier\\Thèse\\EXP 2017\\Suivi EXP\\AVRIL18\\PHEN\\inter\\Total weight GR\\bilan.txt".split('\\')

import numpy as np
np.array("C:\\Users\\Xavier\\Thèse\\EXP 2017\\Suivi EXP\\AVRIL18\\PHEN\\inter\\Total weight GR\\bilan.txt".split('\\'))[-4:-1]
