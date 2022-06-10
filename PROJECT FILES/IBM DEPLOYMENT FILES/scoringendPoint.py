# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 11:29:54 2022

@author: ayush
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "qZ1L8puFkx5OiafXhv2t5HHXK-Roa3E2c7FbwRrnza6n"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields":[["f0","f1","f2","f3","f4","f5","f6"]],
"values":[[1,2,3,2,1,4,5]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/03741e21-6e84-48b6-8fe7-520288d195ad/predictions?version=2022-06-09', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
pred=response_scoring.json()
output=pred['predictions']
print(output)
outpt=pred['predictions'][0]['values'][0][0]
print(outpt)