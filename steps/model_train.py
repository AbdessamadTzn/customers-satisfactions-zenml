import logging
from zenml import step 
import pandas as pd 

@step 
def train_model(df: pd.DataFrame) -> None:
    """
    Train the model on th ingested data

    Args:
        df (pd.DataFrame): The ingested data
    """
    pass 