from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
sc = spark.sparkContext
data="D:/datasets/us-500.csv"
df=spark.read.format("csv").option("header","True")\
    .option("inferSchema","True").option("sep",",").load(data)

import re
cols=[re.sub('[^a-zA-Z0-9]',"",c) for c in df.columns]
ndf=df.toDF(*cols)
ndf.show(10,truncate=False)
df.printSchema()

host="jdbc:mysql://mydatabase.cfakdqfg4tra.ap-south-1.rds.amazonaws.com:3306/abhi"
uname="myuser"
pwd="password"

ndf.write.mode("overwrite").format("jdbc").option("url",host)\
    .option("dbtable","record").option("user",uname).option("password",pwd)\
    .option("driver","com.mysql.cj.jdbc.Driver").save()