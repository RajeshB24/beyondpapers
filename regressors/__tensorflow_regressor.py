from tensorflow.keras import Sequential,activations,layers,callbacks,losses
import numpy as np
import tensorflow as tf



class tensorflow_AnnRegressor:
    def __init__(self,epochs=10,hidden_units=[120,120],activations=['relu','relu']
                 ,weights=np.nan,model=None):
        self.epochs = epochs
        self.hidden_units =hidden_units
        self.activations = activations
        self.weights = weights
        self.model = model
        
    
    def fit(self,X,y):
        
        hidden_units = self.hidden_units
        activations = self.activations
        weights = self.weights
        epochs = self.epochs
        model = self.model
        
        
        if model is None:
            ## Build Architecture
            model = Sequential([layers.InputLayer(input_shape=(X.shape[1],))])
            
            ## add hidden layers
            if hidden_units is not None: 
        
                for i in range(len(hidden_units)):
                    model.add(layers.Dense(hidden_units[i],activation=activations[i]))
            
            ## add output layer    
            model.add(layers.Dense(1))
        
            ## Compile 
            model.compile(optimizer='adam',loss=losses.mean_squared_error)
        
      
        ### Weight Initialise
        if weights is not np.nan:
          
            model.set_weights(weights)
        
            
        ### Train  
        
        model.fit(x=X,y=y,epochs=epochs,verbose=0)
        
        ### Weights
        
        weights = model.get_weights()
        
        self.weights=weights
        self.model = model
    
    def predict(self,X):
        model =self.model
        ypred = model.predict(X)
        ypred= ypred.reshape(ypred.shape[0])
        return ypred