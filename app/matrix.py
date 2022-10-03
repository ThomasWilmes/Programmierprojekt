# Now, we create user-item matrix using scipy csr matrix
from scipy.sparse import csr_matrix
import numpy as np
import pandas as pd
  
def create_matrix(df):
      
    N = len(df['Cust_Id'].unique())
    M = len(df['Movie'].unique())
      
    # Map Ids to indices
    user_mapper = dict(zip(np.unique(df["Cust_Id"]), list(range(N))))
    movie_mapper = dict(zip(np.unique(df["Movie"]), list(range(M))))
      
    # Map indices to IDs
    user_inv_mapper = dict(zip(list(range(N)), np.unique(df["Cust_Id"])))
    movie_inv_mapper = dict(zip(list(range(M)), np.unique(df["Movie"])))
      
    user_index = [user_mapper[i] for i in df['Cust_Id']]
    movie_index = [movie_mapper[i] for i in df['Movie']]
  
    X = csr_matrix((df["Rating"], (movie_index, user_index)), shape=(M, N))
      
    return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper