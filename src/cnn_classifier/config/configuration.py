from src.cnn_classifier.constants import *
from src.cnn_classifier.utils.common import create_directories , read_yaml
from src.cnn_classifier import logger
from src.cnn_classifier.entity.config_entity import DataIngestionConfig
from src.cnn_classifier.entity.config_entity import PrepareBaseModelConfig
from src.cnn_classifier.entity.config_entity import ModelTrainingConfig
import os
from src.cnn_classifier.entity.config_entity import EvaluationConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URl=config.source_URL, 
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_prepare_base_model(self)-> PrepareBaseModelConfig:

        config=self.config.prepare_base_model
        
        prepare_base_model=PrepareBaseModelConfig(
        root_dir=Path(config.root_dir), 
        base_model_path=Path(config.base_model_path),
        updated_base_model_path=Path(config.updated_base_model_path),
        


        params_image_size=self.params.IMAGE_SIZE,
        params_include_top=self.params.INCLUDE_TOP,
        params_weight=self.params.WEIGHTS,
        params_classes=self.params.CLASSES,
        params_learning_rate=self.params.LEARNING_RATE
        )
        return prepare_base_model
    
    
    def get_model_training_config(self)-> ModelTrainingConfig:
        
        # config_train=self.config.training
        params=self.params
        prepare_base_model=self.config.prepare_base_model
        training_data_path=os.path.join(self.config.data_ingestion.unzip_dir, "kidney-ct-scan-image")
        create_directories([self.config.training.root_dir])
        try: 
            model_training_config=ModelTrainingConfig(
                root_dir=Path(self.config.training.root_dir),
                trained_model_path=Path(prepare_base_model.updated_base_model_path),
                training_data=Path(training_data_path),
                final_model_train=Path(self.config.training.trained_model_path),
                
                
                params_augmentation= params.AUGMENTATION,
                params_batch_size=params.BATCH_SIZE,
                params_image_size=params.IMAGE_SIZE,
                params_epochs=params.EPOCHS
                )
            return model_training_config
        except Exception as e: 
            raise e
        
    def get_evaluation_config(self)-> EvaluationConfig:

        evaluation_config=EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/kidney-ct-scan-image",
            mlflow_uri="https://dagshub.com/Abhikkumar619/Kidney_disease_classification.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE

        ) 
        return evaluation_config
            
            
