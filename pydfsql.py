from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()

data = "D:/spark/drivers/asl.csv"
sc=spark.sparkContext
#sc.setLogLevel("ERROR")
aslrdd=sc.textFile(data)

res2 = aslrdd.filter(lambda x:"age" not in x).map(lambda x:x.split(",")).toDF(["name","age","city"])
res2.show()
res2.createOrReplaceTempView("asl")
res1 = spark.sql("select * from asl where city='blr'")
res1.show()