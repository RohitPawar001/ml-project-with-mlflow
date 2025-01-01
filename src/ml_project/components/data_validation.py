import os
import pandas as pd
from ml_project import logger
from ml_project.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            
            data = pd.read_csv("D:\\software\\python_vs\\ml_project_with_mlflow\\artifacts\\data_ingestion\\winequality-red.csv")
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema and col != "quality":
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")
                    break
                else:
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")

            return validation_status
        except Exception as e:
            logger.error(f"Error in validating columns: {e}")
            return False
