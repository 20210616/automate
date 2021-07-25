# 隨機模組
import random
# 隨機選取
# data = random.sample([1,5,6,10,20], 3)
# print(data)
# 隨機調換順序
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)
# 隨機取得亂數
# data = random.random() #0~1之間的隨機亂數
# print(data)
# data = random.uniform(1,100)
# print(data)
# 平均數100，標準差10，得到的資料多數在90~110 之間
# data = random.normalvariate(100, 10)
# print(data)

# 統計模組
import statistics as stat
print(stat.mean([1,4,5,8]))
print(stat.median([1,2,3,4,5,8,100]))
print(stat.stdev([1,2,3,4,5,8,100]))
print(stat.stdev([1,2,3,4,5,8,10]))