#7. Create Data Frame from Excel sheet using Pandas and Perform Operations on DataFrames

import pandas as pd
df=pd.read_excel('SampleWork.xlsx')
print(df)
#Opearation
print(f'head() function::\n {df.head(2)}')
print(f'tail() function::\n {df.tail(2)}')
print('Accessing row::\n',df.loc[2])

