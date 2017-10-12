#!/usr/bin/python3
import json
import os.path

tweets = []

with open('./file.json', mode='r', encoding='utf-8') as fo:
    f = json.load(fo)

for x in f:
    print(x)
