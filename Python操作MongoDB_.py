import pymongo

#myclient = pymongo.MongoClient("mongodb://10.201.49.80:28018/")
#myclient = pymongo.MongoClient('mongodb://insread:insread#135pwd@10.201.49.80:28018/')

#指定数据库
myclient = pymongo.MongoClient('mongodb://insread:insread%23135pwd@10.201.49.80:28018/?authMechanism=DEFAULT&authSource=energy')

#获取数据库名字
dbs = myclient['energy']
#print(dbs)

#指定集合
collection = dbs['MeterValue4New']
#print(collection)

#查询数据
'''
result = collection.find_one({'sourceType':'rt_result15'})
print(result)
'''

results= collection.find({'sourceType':'rt_result15'})
print(results)
for result1 in results:
    print(result1)
