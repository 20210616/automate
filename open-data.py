# 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") # 取得台灣大學網站的原始碼(HTML、CSS、js)
# print(data) 
# 串接、擷取公開資料

import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/c31fecc4-466f-4940-8f2a-012d072df0a6?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理  json 資料格式
# 將公司名稱列表出來
clist=data["result"]["results"]
with open("data1.txt", "w", encoding="utf-8") as file:
    for fruit in clist:
        file.write(fruit["活動項目"]+"\n")