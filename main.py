import sys
import os
src_path = "D:\\software\\python_vs\\ml_project_with_mlflow\\src"
sys.path.append(os.path.abspath(src_path))
print("Current sys.path:", sys.path)
from ml_project.utils import comman
print("Imports successful")


from src.ml_project import logger
from src.ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ml_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.ml_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.info(e)
    
    
    
    
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e