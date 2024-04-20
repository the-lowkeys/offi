# This module is to add and remove information in the csv file??????

import pandas as pd


def add_info():
        
    df = pd.read_csv('data.csv')
    pd.DataFrame(df, columns=['Filename', 'File Type', 'Description'])
    df['Filename'].astype('str')
    df['File Type'].astype('str')
    df['Description'].astype('str')
    df.to_csv('data.csv')
    

def remove_info(data):

    df = pd.read_csv(data)


add_info()