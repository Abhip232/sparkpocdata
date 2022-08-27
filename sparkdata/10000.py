from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
sc = spark.sparkContext

data="D:/datasets/10000Records.csv"
df=spark.read.format("csv").option("inferSchema","true").option("header","true").option("sep",",").load(data)
df.show()
import re
cols=[re.sub('[^0-9a-zA-Z]',"",c)for c in df.columns]
ndf=df.toDF(*cols)
#res=ndf.withColumnRenamed("DateofBirth","dob").withColumn("today", current_date()).where(col("Gender")=="F")
res=ndf.withColumn("DateofBirth",to_date(col("DateofBirth"),"M/d/yyyy"))\
    .withColumn("today",current_date()).withColumn("diff",datediff(col("DateofBirth"),col("today")))
res.printSchema()
res.show()

