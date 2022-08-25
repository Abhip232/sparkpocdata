from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
sc =  spark.sparkContext

df1 = "D:/datasets/OfficeDataProject.csv"
nfs1= spark.read.format("csv").option("header","true").option("inferSchema","true").load(df1)
nfs1.show()
res3 = nfs1.withColumn("fname",split(col("employee_name")," ").getItem(0))\
    .withColumn("lname",split(col("employee_name")," ").getItem(1))
res3.show()
res = nfs1.where((col("age")>40) & (col("bonus")>1400) & (col("department")=="Accounts"))
res.show(10)
res1 = nfs1.where((col("age")>40) | (col("bonus")>1400) | (col("department")=="Accounts"))

nfs1.createOrReplaceTempView("officedata")
t1 = spark.sql("select * from officedata where age > 40 and bonus>1800")
t1.show(10)