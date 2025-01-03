from ml_project.config.configuration import ConfigurationManager
from ml_project.components.model_evaluation import ModelEvaluation
from ml_project import logger
from pathlib import Path


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingConfigPipeline:
    def __init__(self):
        pass
    
    def main(self):
        CONFIG_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\config\config.yaml")
        PARAMS_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\params.yaml")
        SCHEMA_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\schema.yaml")
            
        config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH)
        
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelEvaluationTrainingConfigPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\n x***********x")
    except Exception as e:
        logger.exception(e)
        raise e