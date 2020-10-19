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

path = "C:\\Users\\Xavier\\FORMANRISK\\data\\FORMANRISKNEW\\forman_suite.csv"
path = "C:\\Users\\Xavier\\FORMANRISK\\data\\FORMANRISK\\Formannew.csv"
df=pd.read_csv(path, sep=',')
df.head()


df.groupby(['Campaign_name', 'Sampling_location', 'Species', 'Treatment', 'Sample_ref_2'])\
.agg({'Sample_ref_1':'count', 'Sample_ref_2':'count'})\
.rename(columns={'Sample_ref_1':'Sample_ref_1_new','Sample_ref_2':'Sample_ref_2_new'}) \
.reset_index()

df1=df.groupby(['Campaign_name', 'Sampling_location', 'Species', 'Treatment','Sample_ref_1'])\
.agg({'Sample_ref_1':'count'}).rename(columns={'Sample_ref_1':'count_sample_ref_1'})

df2=df.groupby(['Campaign_name', 'Sampling_location', 'Species', 'Treatment', 'Sample_ref_2'])\
.agg({'Sample_ref_2':'count'}).rename(columns={'Sample_ref_2':'count_sample_ref_2'})



dfsynth = df.groupby(['Campaign_name', 'Sampling_location', 'Species', 'Treatment', 'Sample_ref_1'])\
.agg({'Sample_ref_2':'count'}).rename(columns={'Sample_ref_2':'count_sample_ref_2'}).reset_index()
dfsynth.head()


def my_cool_func(x):
    #print (x)
    return (x.max() - x.min()) / 2

df.groupby(['Campaign_name', 'Sampling_location', 'Species', 'Treatment', 'Sample_ref_1'])['Sample_ref_2'].value_counts().rename(columns={'Sample_ref_2':'count_sample_ref_2'}).reset_index()

pb = []
for camp in df['Campaign_name'].unique():
    for loc in df['Sampling_location'].unique():
        for sp in df['Species'].unique():
            for tr in df['Treatment'].unique():
                for cav in df['Sample_ref_2'].unique():
                    nval = len(df.loc[(df['Campaign_name']==camp) & (df['Sampling_location']==loc) & (df['Species']==sp) & (df['Treatment']==tr) & (df['Sample_ref_2']==cav),'Sample_ref_1'].unique().tolist())
                    # print(nval)
                    if nval >1:
                        pb.append([camp,loc,sp,tr,cav,nval])


pb

df['REP']=1

for n in pb:
        print(df.loc[(df['Campaign_name']==n[0]) & (df['Sampling_location']==n[1]) & (df['Species']==n[2]) & (df['Treatment']==n[3]) & (df['Sample_ref_2']==n[4]),['Sample_ref_1','Sample_ref_2']])

df.loc[df['Sampling_location']=='lm','Sample_ref_1'].unique()
df['Sample_ref_2'].unique()

for n in pb:
    print(df[(df['Campaign_name']==n[0]) & (df['Sampling_location']==n[1]) & (df['Species']==n[2]) & (df['Treatment']==n[3]) & (df['Sample_ref_2']==n[4])]['Sample_ref_1'].unique().tolist())

for n in pb:
    cavit_number = df[(df['Campaign_name']==n[0]) & (df['Sampling_location']==n[1]) & (df['Species']==n[2]) & (df['Treatment']==n[3]) & (df['Sample_ref_2']==n[4])]['Sample_ref_1'].unique().tolist()
    tree_number = df[(df['Campaign_name']==n[0]) & (df['Sampling_location']==n[1]) & (df['Species']==n[2]) & (df['Treatment']==n[3]) & (df['Sample_ref_2']==n[4])]['Sample_ref_2'].unique().tolist()
    print('''
         ------------------
         description

         campaign: {}
         site: {}
         species: {}
         treament: {}
         sample ref 1 (cavit number): {}
         sample ref 2 (tree number): {}
          '''.format(n[0],n[1],n[2],n[3],cavit_number, tree_number))

          input
          repet = 1
          for ca in cavit_number:
              df.loc['sample ref 1]'==ca,'REP']=repet
              repet += 1


['a', 'b'] in ['a','b', 'c']

set(['a', 'b']).intersection(['a','b', 'c'])
