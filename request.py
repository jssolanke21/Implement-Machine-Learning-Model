# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:01:05 2019

@author: MANOJ
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())