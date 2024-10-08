# # Although I have src here then also I am calling this MlOpsProject directly, why ??
# # Because I have initialised my logging funcionality in the __init__ constructor of the MlOpsProject folder ,so I don't need to call the src separately.

# import sys
# import os

# # Add the src directory to the Python path
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# from MlOpsProject import logger

# def some_function():
#     logger.info("This is an informational message; only for custom logging")
#     logger.warning("This is a warning message.")
#     logger.error("This is an error message.")

# # Call the function to see logging in action
# some_function()

# # when you run this main.py file you will see the logs in the terminal as well as in the logs file.



## Stage 1 - Data Ingestion
from MlOpsProject import logger
from MlOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MlOpsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MlOpsProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MlOpsProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


# Stage 2 - Data Validation

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()  # Changed variable name for clarity
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# Stage 3 - Data Transformation
STAGE_NAME = "Data Transformation stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


# Stage 4 - Model Training
STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer= ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e