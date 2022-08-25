from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()

data = "D:/spark/drivers/asl.csv"
sc=spark.sparkContext

aslrdd=sc.textFile(data)

res = aslrdd.filter(lambda x: "hyd" in x)
res1 = aslrdd.map(lambda x:x.split(",")).filter(lambda x: "hyd" in x[2])
res2 = aslrdd.filter(lambda x:"age" not in x).map(lambda x:x.split(",")).filter(lambda x: int(x[1])>30)
res4 = aslrdd.filter(lambda x:"age" not in x).map(lambda x:x.split(","))

#for i in res.collect():
    #print(i)
#print('map and filter= ','\n')
#for j in res1.collect():
   # print(j)
#print('filter using remove header map and filter= ','\n')

for x in res2.collect():
    print(x)

#for y in res4.collect():
   # print(y)