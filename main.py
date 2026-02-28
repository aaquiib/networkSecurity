from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation

from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.config_entity import DataValidationConfig
from network_security.entity.config_entity import DataTransformationConfig
from network_security.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config= DataIngestionConfig(training_pipeline_config)
        DataIngestion_obj=DataIngestion(data_ingestion_config)
        logging.info("data ingestion started")
        data_ingestion_artifact=DataIngestion_obj.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logging.info("data ingestion completed")

        print('-'*40)

        data_validation_config=DataValidationConfig(training_pipeline_config)
        DataValidation_obj= DataValidation(data_ingestion_artifact, data_validation_config)
        logging.info("data validation started")
        data_validation_artifact= DataValidation_obj.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("data validation completed")

        print('-'*40)

        data_transformation_config= DataTransformationConfig(training_pipeline_config)
        DataTransformation_obj= DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("data transformation started")
        data_transformation_artifact= DataTransformation_obj.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation completed")


    except Exception as e:
        raise NetworkSecurityException(e,sys)
