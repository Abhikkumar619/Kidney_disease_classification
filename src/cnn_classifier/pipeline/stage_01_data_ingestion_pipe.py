from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.components.data_ingestion import DataIngestion
from  src.cnn_classifier import logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def main(self):

        try: 
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_dir()

        except Exception as e: 
            raise e



if __name__ == '__main__':
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    except Exception as e: 
        logger.exception(e)
        raise e




