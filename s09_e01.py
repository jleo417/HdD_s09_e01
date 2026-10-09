import numpy as np
import pandas as pd
A=np.array([1,2,3,4])
dsA=pd.Series(A).std()
T=pd.Dataframe(A)
print(A)
print(np.mean(A))
print(dsA)
T.to_excel('nota.xlsx',index=False)