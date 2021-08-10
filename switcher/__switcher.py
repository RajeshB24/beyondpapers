
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from ..regressors import tensorflow_AnnRegressor 
from sklearn.cluster import KMeans
import copy


class Switcher:
    
    def __init__(self,
                 base_model=tensorflow_AnnRegressor(),
                 meta_learner = RandomForestClassifier(),
                 split=4, switch=20,
                 base_learner_initialize=False,
                 split_group=None,
                 split_learn_mode = 'pre-post',
                 split_weights=np.nan,
                 split_learners=np.nan,
                 random_state=100,
                 recommendations = True
                
                 ):
        '''
        split_learn_mode = default 'post', mention any on of 'post',  'during', 'pre-post', 'pre-during' 
        '''
        self.base_model=base_model
        self.split = split
        self.switch = switch
        self.split_weights = split_weights
        self.split_learners = split_learners
        self.meta_learner = meta_learner
        self.random_state=random_state
        self.split_group = split_group
        self.split_learn_mode= split_learn_mode
        self.base_learner_initialize=base_learner_initialize
        self.recommendations = recommendations
        
    def fit(self,X,y):
        
        np.random.seed(self.random_state)
        base_model=self.base_model
        meta_learner = self.meta_learner
        split_group = self.split_group
        ## Initial Selections
        split=self.split 
        switch=self.switch
    
        
        
        #########  Random Intial Splitter ########
        ##### Only if split Index is provided ####
        if self.split_group is None:

            if self.recommendations == True :
                print(f"Recommendation : Data will be randomly split into {split} splits. Alternatively split_group can initialized with any Clustering Model or Tree Model with index of leaf as split.Check out options in beyond_papers.split_intialzers.\n\nNote: Split Initializers are required only for Train Data and meta leaner will automatically split Test Data.")

            idx  = np.arange(X.shape[0])
            np.random.shuffle(idx)
            idx_splits = np.array_split(idx,split)
            split_group = np.zeros(X.shape[0])
            for i in range(split):
                split_group[idx_splits[i]]=i
        else:
            self.split = split
            split = len(set(split_group))
            
            

        
        split_learners = [None]*split
        
        y_pred_splits = np.zeros(X.shape[0]*split).reshape(X.shape[0],split)
        split_list=np.unique(split_group).astype(int).tolist()
        
        ##### Pre  Switch  Split Learner #########
        if self.split_learn_mode in ['pre-post','pre-during']:
            if len(split_list)>1:
                    meta_learner.fit(X,split_group)
                    split_group=meta_learner.predict(X)

        #### Initialize Base Learner
        if self.base_learner_initialize==True:
            initialize_learner = copy.deepcopy(base_model)
            initialize_learner.fit(X,y)
            intial_weights = initialize_learner.weights
            split_weights = [intial_weights]*split
        else:
            split_weights = [np.nan]*split

        ##### Switch Cycle #####
        
        for n_switch in range(switch): 
            split_list=np.unique(split_group).astype(int).tolist()
           

            
            ### Run base Model for Each Split ####

            for i_split,split_val in enumerate(split_list):
                
                #### Iterative learning of Base Model per Split ####
                
                #### Create new instance of base model with same parameters and updated weights for a split
               
                if split_learners[i_split] is None:
                    learner = copy.deepcopy(base_model)
                    
                    
                    if self.base_learner_initialize==True:
                        learner.weights = split_weights[i_split]
                else:
                    learner = split_learners[i_split]
                    
                    
                X_split=X[np.where(split_group==split_val)]
                y_split=y[np.where(split_group==split_val)]
                
                learner.fit(X_split,y_split)
            
                split_learners[i_split]=learner 
                
                
            
          
            
            ###### Switch Observations #####
           ## Switch obs to its best predictor 
            
            for col in range(y_pred_splits.shape[1]):
                
                y_pred_splits[:,col]=split_learners[col].predict(X).reshape(-1)
                
                
                         
            abs_error=abs(y.reshape(X.shape[0],1) - y_pred_splits)
            split_group=np.argmin(abs_error, axis=1)
                
            split_list=np.unique(split_group).astype(int).tolist()

            ##### During Switches Split Learner #########
            if  self.split_learn_mode in ['during','pre-during']:
                if  len(split_list)>1:
                    meta_learner.fit(X,split_group)
                    split_group=meta_learner.predict(X) 
                    split_list=np.unique(split_group).astype(int).tolist()
              
          
       ##### Post Switch Split Learner #########
        if  self.split_learn_mode in ['post','pre-post']:
            if  len(split_list)>1:
                meta_learner.fit(X,split_group)
                split_group=meta_learner.predict(X) 
      
        self.split_weights=split_weights
        self.split_learners=split_learners
        self.meta_learner=meta_learner
        self.split_group=split_group 
        
    def predict(self,X):
        
        split_group = self.meta_learner.predict(X)
        
        split_learners = self.split_learners
        split_group_unique=np.unique(split_group).astype(int).tolist()
        
        split_group_list=[np.where(split_group==i) for i in split_group_unique ]
       
        sort_index = np.argsort(np.hstack(split_group_list))
        
        
        
        ypred=[split_learners[i].predict(X[np.where(split_group==i)]).reshape(-1) for i in split_group_unique ]
        
           
        ypred = np.hstack(ypred)
        ypred = ypred[sort_index]
        ypred=ypred.reshape(-1)
        return ypred

