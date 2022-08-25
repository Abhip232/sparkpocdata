from pyspark.sql import *
from pyspark.sql.functions import *
spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()

data = "D:/spark/drivers/asl.csv"
sc=spark.sparkContext
sc.setLogLevel("ERROR")
aslrdd=sc.textFile(data)

res = aslrdd.filter(lambda x: "hyd" in x)
res1 = aslrdd.map(lambda x:x.split(",")).filter(lambda x: "hyd" in x[2])
for i in res.collect():
    print(i)

for j in res1.collect():
    print(j)