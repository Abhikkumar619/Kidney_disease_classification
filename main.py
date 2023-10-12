from src.cnn_classifier.pipeline.stage_01_data_ingestion_pipe import DataIngestionTrainingPipeline
from src.cnn_classifier import logger
from src.cnn_classifier.pipeline.stage_02_prepare_base_mode_pipe import PrepareBaseModelPipeline
from src.cnn_classifier.pipeline.stage_03_model_training_pipe import ModelTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME="PREPAREBASE MODEL"

try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} Started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    obj=PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME= "Model Training"

try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} Completed >>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
    raise e