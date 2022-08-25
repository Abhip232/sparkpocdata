from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()


data="D:\\spark\\drivers\\us-500.csv"
df=spark.read.format("csv").option("header","true").option("inferSchema","true").load(data)
#ndf=df.groupBy(df.state).agg(count("*").alias("cnt")).orderBy(col("cnt").desc())
ndf=df.withColumn("fullname", concat_ws(" ",df.first_name, df.last_name))\
    .withColumn("phone1",regexp_replace(col("phone1"),"-","").cast(LongType()))\
    .withColumn("phone2",regexp_replace(col("phone2"),"-","").cast(LongType()))\
    .drop("email","web","city","country","address")\
    .withColumnRenamed("first_name","fname").withColumnRenamed("last_name","lname")

#withColumnRenamed used to rename onecolumn at a time
#withColumn used to add a new column (if column not exists) or update (if already column exists)
#lit(value) used to add something dummy value
#drop (columns) ... delete unnecessary clumns.
ndf.show()
ndf.printSchema()