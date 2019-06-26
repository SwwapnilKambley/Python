import os
import glob
import pandas as pd 

#SPECIFY DIRECTORY / PATH TO ALL CSV

os.chdir("D:\PythonCSV\\")

#DEFINE EXTENSION(CSV/JSON)
extension = 'csv'

#FOR ALL THE FILES 
files = [i for i in glob.glob('*.{}'.format(extension))]

#CREATE A DATAFRAME
df = pd.DataFrame()

#LOOP TO APPEND ALL CSV I
for file in  files:
    df_n =  pd.read_csv(file)
    
    df = df.append(df_n, ignore_index=True, sort=False)

#EXPORT THE CSV

export_csv = df.to_csv("D:\\PythonCSV\\combined.csv", index = None, encoding='utf-8-sig')

