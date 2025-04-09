import logging 
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression



class Model(ABC):
    """Abstract base class for all models"""

    @abstractmethod
    def train(self, X_train, y_train):
        pass

class LinearRegression(Model):
    """Linear Regression Model"""

    def train(self, X_train, y_train, **kwargs):
        """Train the model on the training data"""

        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            return reg
        except Exception as e:
            logging.error("Error training the model: {}".format(e)) 
            raise e

        
    
    
