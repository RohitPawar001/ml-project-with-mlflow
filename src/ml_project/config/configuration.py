from ml_project.constants import *
from ml_project.utils.comman import read_yaml, create_directories
from ml_project.entity.config_entity import DataIngestionConfig
from pathlib import Path

class ConfigurationManager:
    def __init__(self, config_filepath:Path, params_filepath, schema_filepath):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config['artifacts_root']])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        
        create_directories([config['root_dir']])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            source_URL=config['source_URL'],  
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )
        
        return data_ingestion_config