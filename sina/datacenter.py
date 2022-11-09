import get_data
import json
import pandas as pd

# json = get_data.volumeRise()
#
# dt = pd.read_json(json)
# print(dt)

jss = get_data.minline('sh601155')
js = json.loads(jss)
dta = js['result']['data']
dt = pd.read_table(dta)
print(dt)
