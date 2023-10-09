import os
import zipfile
import gdown
from cnn_classifier.utils.common import get_size
from src.cnn_classifier.entity.config_entity import DataIngestionConfig
from src.cnn_classifier import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config=config

        """
        Fetch data from url
        """
    def download_data(self):
        try: 
            url=self.config.source_URl
            zip_download_dir=self.config.local_data_file
            logger.info(f"URL: {url} zip_download_dir: {zip_download_dir}")
            download_id=url.split("/")[-2]
            os.makedirs(self.config.root_dir, exist_ok=True)
            prefix='https://drive.google.com/uc?/export=download&id='+download_id
            gdown.download(prefix, zip_download_dir)
            logger.info(f"Download_prefix : {prefix} and download sucessfully happen")
        except Exception as e: 
            raise e


    def unzip_dir(self):
        """
        Unzip the dataset directories.
        """
        try:
            unzip_path=self.config.root_dir
            with zipfile.ZipFile(self.config.local_data_file,'r') as zip:
                zip.extractall(unzip_path)
                
        except  Exception as e:
            raise e
            
       