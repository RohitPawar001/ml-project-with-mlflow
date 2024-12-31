from src.ml_project import logger
from src.ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.info(e)