import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            
            ingestion_path = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            if not os.path.exists(ingestion_path):
                raise FileNotFoundError(f"The path {ingestion_path} does not exist.")
            
            
            validation_path = os.path.join("artifacts", "data_validation")
            if not os.path.exists(validation_path):
                os.makedirs(validation_path)  

            all_files = os.listdir(ingestion_path)
            
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                else:
                    validation_status = True
                
                status_file_path = os.path.join(validation_path, os.path.basename(self.config.STATUS_FILE))
                with open(status_file_path, 'w') as f:
                    f.write(f"validation status: {validation_status}")
            
            return validation_status
        
        except Exception as e:
            raise e

