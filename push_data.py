import sys
import os
import json

from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_DB_URL")
# print(MONGO_URI)

import certifi
ca= certifi.where()

import pandas as pd
import numpy as np
import pymongo
from network_security.exception.exception import CustomException
from network_security.logging.logger import logging

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            
            raise CustomException(e,sys)
        
    def csv_to_json(self,file_path: str):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records= list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)   

    def insert_to_mongo(self,records,database,collection):
        try:
            self.database= database
            self.collection= collection
            self.records= records

            self.mongo_client = pymongo.MongoClient(MONGO_URI)
            self.database= self.mongo_client[self.database]
            self.collection= self.database[self.collection] 
            self.collection.insert_many(self.records) 
            
            return len(self.records)

        except Exception as e:
            raise CustomException(e,sys) 

if __name__=='__main__':
    FILE_PATH = "Netword_data\\phisingData.csv"
    database= "AaquibDB"
    collection= "NetworkData"
    ETL_obj= NetworkDataExtract()
    records= ETL_obj.csv_to_json(FILE_PATH)
    number_of_records = ETL_obj.insert_to_mongo(records,database,collection)
    print(number_of_records)