import logging
from zenml import step
import pandas as pd 


@step 
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    pass 