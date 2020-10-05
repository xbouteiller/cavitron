import os
import re

root = "C:/Users/Xavier/CavitClean/test"

lpd = []

for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))


for path, subdirs, files in os.walk(root):
    tlpd = []
    for s in subdirs:
        print(os.listdir(os.path.join(path, s)))


lpd = []
for path, subdirs, files in os.walk(root):
    for s in subdirs:
        [lpd.append(os.listdir(os.path.join(path, s)))]
    print(lpd)



testre = ['184.csv', '189.2.csv', 'append.csv', '182.a.csv', 'a.48.csv', '184.txt', '184.2.txt', 'aa.aa.csv']

import re

[i for i in testre if re.search(r'^\d+\.csv|\d+\.\d+\.csv',i)]




#######################################################################################
def listdir_fullpath(path, s):
    d=os.path.join(path, s)
    return [os.path.join(d, f) for f in os.listdir(d)]


root = "C:\\Users\\Xavier\\CavitClean\\test"
lpd = []
for path, subdirs, files in os.walk(root):
    for s in subdirs:
        lpd.append(listdir_fullpath(path, s))
print(lpd)

#######################################################################################


['a', 'b', 'c'][True, False, True]

num_col= ['a', 'b', 'c']
check_num=[True, False, True]
[print('col {} is Numeric'.format(i)) if j else print('col {} is not Numeric'.format(i)) for i, j in zip(num_col, check_num) ]

import os
import re

def listdir_fullpath(path, s):
    d=os.path.join(path, s)
    return [os.path.join(d, f) for f in os.listdir(d) if re.search(r'^\d+\.csv|\d+\.\d+\.csv',f)]

root = "F:\\FORMANRISK"
lpd = []
for path, subdirs, files in os.walk(root):
    for s in subdirs:
        lpd.append(listdir_fullpath(path, s))
print(lpd)

















[i for i in lpd[0] if re.search(r'^\d+\.csv|\d+\.\d+\.csv',i)]
