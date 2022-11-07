import get_json

import pandas as pd

# json = get_json.jsonpV2("/StatisticsService.getSummaryMonthList?page=1&num=50&sort=amount&asc=1&node=adr_hk")
json = get_json.jsonpV2("/StatisticsService.getVolumeRiseConList?page=1&num=200&sort=changes_con&asc=0&node=adr_hk")

dt = pd.read_json(json)
print(dt)
