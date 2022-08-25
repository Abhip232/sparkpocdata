from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
#creating SparkSession object
data="D:/spark/drivers/bank-full.csv"
df=spark.read.format("csv").option("header","true").option("sep",";").option("inferSchema","true").load(data)
df.show()
df.createOrReplaceTempView("bankdata")
res = spark.sql("select * from bankdata limit 5")
res.show()
#ad1 = df.where((col("age")>60) & (col("job")=="management"))
#ad1.show(5)

#df.createOrReplaceTempView('bankdata')
#res = spark.sql("select * from bankdata where age>60 and balance>2000")
#res.show(5)

#sep option used to specify delimiter
#by default spark every field consider as string, but i want to change columns appropriate datatype like int, double, string, use inforschema, true option
#if u not mention like this 1000+1000 ... if int .. 2000 if string, u ll get 10001000

#data processing programming friendly
#res=df.where(col("age")>90)
#res=df.select(col("age"),col("marital"), col("balance")).where((col("age")>60) & (col("marital")!="married"))
#res=df.where((col("age")>60) | (col("marital")=="married") & (col("balance")>=40000))
#res=df.where(((col("age")>60) | (col("marital")=="married")) & (col("balance")>=40000))
res1=df.groupBy(col("marital")).agg(sum(col("balance")).alias("smb")).orderBy(col("smb").desc())
res1.show()
#res=df.groupBy(col("marital")).count()
#res=df.groupBy(col("marital")).agg(count("*").alias("cnt"),sum(col("balance")).alias("smb"))
    #where(col("balance")>avg(col("balance")))