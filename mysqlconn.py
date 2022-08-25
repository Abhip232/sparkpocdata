from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
sc = spark.sparkContext
host="jdbc:mysql://mydatabase.cfakdqfg4tra.ap-south-1.rds.amazonaws.com:3306/abhi"
uname="myuser"
pwd="password"

df=spark.read.format("jdbc").option("url",host)\
    .option("dbtable","emp").option("user",uname).option("password",pwd)\
    .option("driver","com.mysql.jdbc.Driver").load()
df.show()
res = df.fillna(0)
res.show()

res1= df.na.fill(200,["comm","mgr"]).withColumn("comm", col("comm").cast(IntegerType()))\
    .withColumn("mgr", col("mgr").cast(IntegerType()))

res2 = df.withColumn("hiredate",date_format(col("hiredate"),"yyyy/MMM/dd"))

res.write.mode("overwrite").format("jdbc").option("url",host).option("user","myuser").option("password","password")\
    .option("dbtable","empclean").option("driver","com.mysql.jdbc.Driver").save()
res2.show()
res2.printSchema()

res1.show()
res1.printSchema()