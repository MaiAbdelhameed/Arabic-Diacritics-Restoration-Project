#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read_input(file_path) -> list:
    with open(file_path, 'r') as file:
    # Read the file line by line into a list
        return file.readlines()


# In[2]:


def create_py():
    get_ipython().system('jupyter nbconvert --to script input_utils.ipynb')


# In[3]:


if __name__ == '__main__':
    create_py()


# In[ ]:




