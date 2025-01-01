from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_validation import DataValidation
from ml_project import logger
from pathlib import Path

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try :
            CONFIG_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\config\config.yaml")
            PARAMS_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\params.yaml")
            SCHEMA_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\schema.yaml")
            
            config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH)
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>satage {STAGE_NAME} completed<<<<<<< \n\n x*************x")
    except Exception as e:
        logger.exception(e)