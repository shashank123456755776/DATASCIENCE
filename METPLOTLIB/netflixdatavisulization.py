# LOADING THE DATASET
# CLEAN THE DATASET 
# UNDERSTANDING THE DATASET
# Indentify Questions To Answer 
# EDA(VISULAIZE THE DATASET)
# Save the Posts
import pandas as pd
import matplotlib.pyplot as plt
# LOAD THE DATESET 
data=pd.read_csv('netflix.csv')
 # clean the dataset 
data.dropna(subset=['show_id','type','title','director'])
type_count=data['type'].value_counts()
# visualize the data 
plt.bar(type_count.index,type_count.values,color=['cyan','magenta'])
plt.title('Number of Movies and Tv Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('netflix_type_distribution.png',dpi=305,bbox_inches='tight')
plt.show()