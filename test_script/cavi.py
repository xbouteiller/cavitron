path='C:\\Users\\Xavier\\FORMANRISK\\data\\FORMANRISKNEW'
import os
import pandas as pd

def _detect_cavisoft(p, s):
    import pandas as pd
    import re
    import os
    d=os.path.join(p, s)

    return [os.path.join(d, f) for f in os.listdir(d) if \
    f.endswith('.csv') and (re.search(r'CAVISOFT|cavisoft', pd.read_csv(os.path.join(d, f),sep=",",nrows=0).columns[0]) and\
     re.search(r'^((?!append).)*$',f.lower())) ]


for pa, subdirs, files in os.walk(path):
    for s in subdirs:
        for f in os.listdir(os.path.join(pa, s)):
            # print(pa, s, f)
            # print(pd.read_csv(os.path.join(pa, s, f),sep=",",nrows=0).columns[0])
            print(f.endswith('.csv'))

for pa, subdirs, files in os.walk(path):
    for s in subdirs:
        print(_detect_cavisoft(p=pa, s=s))
