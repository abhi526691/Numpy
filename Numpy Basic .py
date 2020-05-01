#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Creating a one dimensional Array

# In[2]:


np.array([1, 2, 3])


# Creating Two dimensional Array

# In[4]:


np.array([(1, 2, 3), (4, 5, 6)])


# creating an array of zeros

# In[5]:


np.zeros(3)


# Creating a multidimensional array of zeros

# In[7]:


np.zeros((3, 4))


# creating an array of ones

# In[8]:


np.ones(3)


# creating a multidimensional array of ones

# In[9]:


np.ones((3, 4))


# creating an identity matrix

# In[10]:


np.eye(5)


# Creating an array of equally divided number

# In[14]:


np.linspace(0, 100, 5)


# creating an array of numbers between certain range

# In[15]:


np.arange(0, 10)


# In[16]:


np.arange(0, 10, 3)


# creating an array of particular number

# In[17]:


np.full((2, 3), 8)


# creating an array of particular size where number ranging between 0 and 1

# In[18]:


np.random.rand(4, 5)


# creating an array of particular size where number ranging from 0 to 100

# In[19]:


np.random.rand(4, 5) * 100


# generating a random number from 0 to particular number

# In[23]:


np.random.randint(10)


# generating a random number in an array

# In[25]:


k = np.random.randint(10, size=(2,3))
k


# finding the size of the array

# In[26]:


k.size


# finding the shape of the array

# In[27]:


k.shape


# checking the data type of the array

# In[28]:


k.dtype


# converting array into particular data type

# In[30]:


k.astype('int32')


# converting array into list

# In[31]:


k.tolist()


# to check the info of any keyword

# In[32]:


np.info(np.eye)


# In[35]:


np.info(k.tolist())


# creating a new array from existing array

# In[36]:


newk = np.copy(k)


# In[37]:


newk


# In[38]:


newk.sort()


# In[39]:


newk


# converting a 2D array into 1D array

# In[43]:


newk.flatten()


# finding transpose of an array

# In[46]:


newk.T


# Reshaping an array

# In[59]:


newk.reshape(3,2)


# In[60]:


newk


# appending new array in the existing one

# In[81]:


np.append(newk, [[5, 6, 7]])


# In[82]:


newwk = np.array([2, 3, 4])


# In[89]:


newk[1,2]


# In[90]:


newk[newk<8]


# to calculate mean of the array

# In[91]:


np.mean(newk)


# to calculate sum of the array

# In[92]:


np.sum(newk)


# to calculate minimum of array

# In[93]:


np.min(newk)


# to calculate maximum of the array

# In[94]:


np.max(newk)


# to calculate variance of the array

# In[95]:


np.var(newk)


# to calculate the standard deviation of the array

# In[96]:


np.std(newk)

