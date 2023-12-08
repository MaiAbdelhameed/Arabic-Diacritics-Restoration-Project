#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import pyarabic.araby as araby
from pyarabic.araby import strip_tashkeel, is_arabicrange, strip_diacritics


# In[3]:


def remove_non_arabic_char(text):
    regex = re.compile('[^؀-ۿ ]')
    result = regex.sub('', text)
    return result


# In[4]:


def remove_diacritics(text):
    stripped = araby.strip_diacritics(text)
    diacritics_dic = [{i: char} for i,char in enumerate(text) if char not in stripped]
    return stripped, diacritics_dic


# In[5]:


def create_py():
    get_ipython().system('jupyter nbconvert --to script preprocessing_utils.ipynb')


# In[6]:


if __name__ == '__main__':
    create_py()


# In[ ]:




