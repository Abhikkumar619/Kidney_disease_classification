from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.components.prepare_model import PrepareBaseModel
from src.cnn_classifier import logger

STAGE_NAME="PREPAREBASE MODEL"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            prepare_base_model_config=config.get_prepare_base_model()
            prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>started {STAGE_NAME} sucessfully>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        obj=PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>completed {STAGE_NAME} Sucessfully >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    except Exception as e: 
        raise e





