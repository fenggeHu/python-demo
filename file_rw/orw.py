import os

root = "/Users/max/.tibet"
region = "us"
symbol = "AAPL"

filepath = f'{root}/{region}/features/{symbol}'
if not os.path.exists(filepath):
    os.makedirs(filepath)

filename = f'{filepath}/day.csv'

