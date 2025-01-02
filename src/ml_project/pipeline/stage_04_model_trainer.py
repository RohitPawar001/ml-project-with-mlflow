from ml_project.config.configuration import ConfigurationManager
from ml_project.components.model_trainer import ModelTrainer
from ml_project import logger
from pathlib import Path


STAGE_NAME = "Model Training Stage"

class ModelTraningPipeline:
    def __init__(self):
        pass
    
    def main(self):
        CONFIG_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\config\config.yaml")
        PARAMS_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\params.yaml")
        SCHEMA_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\schema.yaml")
            
        config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH)
        
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelTraningPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\n x***********x")
    except Exception as e:
        logger.exception(e)
        raise e