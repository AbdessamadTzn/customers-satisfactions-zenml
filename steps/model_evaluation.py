import logging
from zenml import step 
import pandas as pd 


@step
def model_evaluate(df: pd.DataFrame)->None:
    """
    Evaluation of the model

    Args:
        df (pdf.DataFrame): The ingested data
    """