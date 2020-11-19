#! /usr/bin/env python3

import os
import requests
import json

path = "/data/feedback"
# List all .txt files under /data/feedback directory that contains the actual feedback
file_list = os.listdir(path)


for filename in file_list:
    data_dict = {}
    fp = open(path + "/" + filename)
    data = fp.read()
    data = data.split('\n')

    # creating dictionary
    data_dict = {"title": data[0], "name": data[1], "date": data[2], "feedback": data[3]}

    # Use the Python requests module to post the dictionary to the company's website.
    response = requests.post("http://34.68.241.255/feedback/", json=data_dict)

    #print the status_code and text of the response objects to check out what's going on
    print(response)
    print(response.text)