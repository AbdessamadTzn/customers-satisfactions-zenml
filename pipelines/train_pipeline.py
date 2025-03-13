from zenml import piplines
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df 
from steps.model_train import train_model
from steps.model_evaluation import model_evaluate


@piplines()
def training_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    model_evaluate(df)


