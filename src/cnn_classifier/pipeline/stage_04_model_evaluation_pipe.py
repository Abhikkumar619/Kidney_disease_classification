from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.components.model_evaluation import Evalutaion
from src.cnn_classifier import logger

STAGE_NAME="MODEL EVALUATION"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            config=ConfigurationManager()
            model_evaluation_config=config.get_evaluation_config()
            evaluation=Evalutaion(config=model_evaluation_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
        except Exception as e: 
            raise e
if __name__ == '__main__':
    try: 
        logger(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} STARTED >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
    except Exception as e: 
        raise e