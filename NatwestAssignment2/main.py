import os
import csv
import glob
import pandas as pd
from contextlib import redirect_stderr

from sqlalchemy import column

def dataValidation(directory):#directory refers to the folder name
    # directory='/home/bhagyashri/Desktop/mainfolder'
    os.chdir(directory)#changing the current working directory to access the csv files

    FileList = glob.glob('*.csv')#creating a list of all csv files

    for i in FileList:#looping through csv files list
        target_file=directory+'/'+i
        
        df=pd.read_csv(target_file,on_bad_lines='skip')#removing rows with invalid columns
        
        df.dropna(how='any', inplace=True)#removing rows with null/empty/nan/nat values

        df.drop_duplicates(inplace = True)#removing all duplicates

        key_columns=[key for key in df.keys()]#getting key columns    [don't forget len]
        print("Key Columns:\n")
        for key in key_columns:
            print(key)

        columns_count=len(df.columns)#getting number of columns    [don't forget len]
        print("Number of Columns:",columns_count)

        rows_count=len(df)#getting number of rows-This the the count after filteing invalid and unnnecessary rows
        print("Number of Rows:",rows_count)

        datatypes=df.dtypes#getting datatype of each column-This the the count after filteing invalid and unnnecessary columns
        print(datatypes)

        df.to_csv(target_file,index=False)#UPDATE : writing updated and validated data to the same file(over-write)


#####################################################EXTRA########################################################
#USING CSV MODULE
def CSV(target_file):
    with open(target_file, 'r') as readFile:
        reader = csv.reader(readFile)

        #NUMBER OF COLUMNS BEFORE
        NOC_before=len(next(reader))
        print("Number of Columns:",NOC_before)

        #NUMBER OF ROWS BEFORE
        NOR_before=len(list(reader))
        print("Number of Rows:",NOR_before)

        lencols=NOC_before
        lines = list()

        values_to_check=[" ",'NULL','NaN',""]
        for row in reader:
            if len(row)==lencols:#only appending rows with valid number of columns
                if set(row).isdisjoint(set(values_to_check))==True:#null/empty/nan/nat values
                    lines.append(row)
        with open(target_file, 'w') as writeFile:#writing the updated data to the same file
                writer = csv.writer(writeFile)
                writer.writerows(lines)


#####################################################EXTRA########################################################
#storing errors-skipped lines for each file 
def errorEncounter(target_file):
    import pandas as pd
    with open('error_messages.txt', 'w') as h:
        with redirect_stderr(h):
                df = pd.read_csv(filepath_or_buffer=target_file,
                        sep=',',            
                        encoding='latin-1',
                        skip_blank_lines=True,
                        on_bad_lines='warn',
                        engine='python',
                        )

#NULL COLUMNS INFO
def nullColumns(df):
    null_columns=df.columns[df.isnull().any()]
    print(df[null_columns].isnull().sum())

    #DISPLAYING ALL THE COLUMNS OF THE ROWS HAVING NULL VALUES
    print(df[df.isnull().any(axis=1)][null_columns].to_string())
