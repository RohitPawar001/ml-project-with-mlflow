from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_transformation import DataTransformation
from ml_project import logger
from pathlib import Path


STAGE_NAME = "data transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("D:\\software\\python_vs\\ml_project_with_mlflow\\artifacts\\data_validation\\status.txt") , "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                CONFIG_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\config\config.yaml")
                PARAMS_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\params.yaml")
                SCHEMA_FILE_PATH = Path(r"D:\software\python_vs\ml_project_with_mlflow\schema.yaml")
                
                config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH)                
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("your data schema is not valid")
        except Exception as e:
            print(e)
            
            
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\n x***********x")
    except Exception as e:
        logger.exception(e)
        raise e