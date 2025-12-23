import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommend.settings'
django.setup()
import pandas as pd


import csv
csv_file_path = 'flipkart_com-ecommerce_sample.csv'


with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)


