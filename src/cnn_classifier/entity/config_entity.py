from dataclasses import dataclass
from pathlib import Path

# Creating entity - entity is the return type of the function 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URl: str
    local_data_file: Path
    unzip_dir: Path