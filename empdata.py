from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
sc = spark.sparkContext
data="D:\spark\employees.csv"

df=spark.read.format("csv").option("header","true").option("inferSchema","true")\
    .option("sep",",").load(data)
df.show()

df1 = df.withColumn("HIRE_DATE",to_date(col("HIRE_DATE"),"d-MMM-yy")).drop("COMMISSION_PCT")
df1.show()

#res = df1.withColumn("fullname",concat_ws(" ",df1.FIRST_NAME,df1.LAST_NAME))
#res.show()
res1=df1.where((col("SALARY")>10000) & (col("DEPARTMENT_ID")>20))
res1.show()