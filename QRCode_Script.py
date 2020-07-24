#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyqrcode
import png
from pyqrcode import QRCode


# In[10]:


print('Please Enter Website Name')
website_name = str(input())
print('Please Enter Website URL')
website_url = str(input())
QRstr = website_url
url = pyqrcode.create(QRstr)
url.png('./QR Codes/'+website_name+'.png',scale=8)
print('QR Code Generated')


# In[ ]:




