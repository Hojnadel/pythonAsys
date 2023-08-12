#my_utils.py
from IPython import get_ipython

def clc():
    print("\014")
    
def clearAll():
    get_ipython().magic('reset -sf')
