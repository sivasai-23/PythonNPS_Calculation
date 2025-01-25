# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
#Import Numpy

import numpy as np # linear algebra

# In[2]:
score = np.loadtxt('/kaggle/input/survey-data-from-user/survey-Data-User.txt', dtype = int)
#Load Survey data and convert it into int data type and store it to variable 'score'
score

# In[3]:

score.ndim #it will provide the dimension of an array

# In[4]:

score.shape #It will return the no.of elements in the each dimension

# In[5]:

score.dtype #Type of the data (integer, float, Python object, etc.)

# In[6]:

np.min(score), np.max(score), round(np.mean(score), 2) #Min, Max and Mean..etc

# In[7]:

# nps = %promoters - %detractors
#NPS Formula

# In[8]:

score <= 6 # detractors condition

# In[9]:

score >= 9  #promoters condition

# In[10]:

# Get Len of Promoters & Detracters
nuof_promoters = len(score[score >= 9 ])
nuof_detracters = len(score[score <= 6])

# In[11]:

total_responses = score.shape[0] # total number of responses
total_responses

# In[12]:

percof_promoters = (nuof_promoters/total_responses)*100
percof_promoters #% Of Promoters

# In[13]:

percof_detracters = (nuof_detracters/total_responses)*100
percof_detracters #% Of Detracters

# In[14]:

nps = percof_promoters - percof_detracters
nps #NPS Score  - 23.783413296778622

# In[15]:

round(nps, 2) #Round Fun()  - 23.78%

# In[16]:

#I hope you find these resources helpful:)