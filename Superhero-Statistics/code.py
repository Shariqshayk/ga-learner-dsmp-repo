# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data= pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count= data['Gender'].value_counts()
plt.bar(gender_count.index, gender_count)
plt.show()




# --------------
#Code starts here
alignment= data['Alignment'].value_counts()
alignment.plot(kind='bar',label='Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df= data[['Strength','Combat']]
sc_covariance= sc_df.cov().iloc[0,1]
sc_strength= sc_df['Strength'].std()
sc_combat= sc_df['Combat'].std()
sc_pearson= sc_covariance/(sc_strength*sc_combat)
print(sc_covariance)


ic_df= data[['Intelligence','Combat']]
ic_covariance= ic_df.cov().iloc[0,1]
ic_intelligence= ic_df['Intelligence'].std()
ic_combat= ic_df['Combat'].std()
ic_pearson= ic_covariance/(ic_intelligence*ic_combat)
print(ic_covariance)



# --------------
#Code starts here
total_high= data['Total'].quantile(0.99)
super_best= data[data['Total']>total_high]
super_best_names= list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

ax_1.boxplot(super_best['Intelligence'])

ax_1.set(title='Intelligence')

ax_2.boxplot(super_best['Speed'])

ax_2.set(title='Speed')

ax_3.boxplot(super_best['Power'])

ax_3.set(title='Power')

#Code ends here   


