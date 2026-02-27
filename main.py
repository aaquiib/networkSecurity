from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

from network_security.components.data_ingestion import DataIngestion
from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingPipelineconfig=TrainingPipelineConfig()
        dataingestionconfig= DataIngestionConfig(trainingPipelineconfig)
        DataIngestion=DataIngestion(dataingestionconfig)

        logging.info("initiate data ingestion")

        dataingestionartifact=DataIngestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("data ingestion completed")

    except Exception as e:
        raise NetworkSecurityException(e,sys)
