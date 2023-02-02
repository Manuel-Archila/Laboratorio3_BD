from pymongo import MongoClient
import pandas as pd
import math

client = MongoClient("mongodb+srv://MongolianosBD2:mongolianos11@cluster0.8fvvazr.mongodb.net/?retryWrites=true&w=majority")

db = client.laboratorio3

wines = db.wines

dataframe = pd.read_csv('winemag-data.csv')

#dataframe['Unnamed: 0'] = dataframe['Unnamed: 0'].replace([])

dataframe = dataframe.rename(columns={"Unnamed: 0": "_id"})

data = []

for index, row in dataframe.iterrows():
    document = {}
    for col in dataframe.columns:
        if not isinstance(row[col], str):
            if not math.isnan(row[col]):
                document[col] = row[col]
        else:
            document[col] = row[col]
    data.append(document)

wines.insert_many(data)
