import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclasses

@dataclasses
class DataIngestionConfig:
    train_data_path: str=os.path('artifacts',"train.csv")
    test_data_path: str=os.path('artifacts',"train.csv")
    raw_data_path: str=os.path('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")

        try:
            df = pd.read_csv('C:\Users\AYOADE ADEYEMI\Documents\Projects_ML\notebook\modern_teen_mental_health_main.csv')
            logging.info(" Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            #os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Spilit Intiatated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion
            