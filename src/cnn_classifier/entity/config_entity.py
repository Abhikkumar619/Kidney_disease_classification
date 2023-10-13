from dataclasses import dataclass
from pathlib import Path

# Creating entity - entity is the return type of the function 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URl: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path

    params_image_size: list
    params_include_top: bool
    params_weight : str
    params_classes: int
    params_learning_rate: int


@dataclass(frozen=True)
class ModelTrainingConfig: 
    root_dir: Path
    trained_model_path: Path
    params_augmentation: bool
    params_image_size: list
    params_epochs: int
    params_batch_size: int
    training_data: Path
    final_model_train: Path

@dataclass(frozen=True)
class EvaluationConfig: 
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int


    