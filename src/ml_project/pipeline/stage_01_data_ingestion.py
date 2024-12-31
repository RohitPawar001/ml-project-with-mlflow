from pathlib import Path
from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_ingestion import DataIngestion
from ml_project import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            CONFIG_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\config\config.yaml")
            PARAMS_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\params.yaml")
            SCHEMA_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\schema.yaml")
            
            config_manager = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH)
            data_ingestion_config = config_manager.get_data_ingestion_config()
            print("DataIngestionConfig created successfully:", data_ingestion_config)
            
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.exception("Data ingestion failed")
            raise e
            
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e