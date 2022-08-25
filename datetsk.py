from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
sc = spark.sparkContext
data="D:/datasets/donations.csv"
df=spark.read.format("csv").option("header","true").option("inferSchema","true").load(data)
df.show()
def dd(days):
       year=days//365
       mt=(days-year*365)//30
       day= (days - mt*30 - year * 365)
       full_date="{}-years {}-months {}-days".format(year,mt,day)
       return full_date

uf = udf(dd)

res=df.withColumn("dt",to_date(col("dt"),"d-M-yyyy"))\
.withColumn("today",current_date())\
.withColumn("dtdiff",datediff(col("today"),col("dt")))\
.withColumn("dayffi",uf(col("dtdiff")))
res.show(truncate=False)
'''
def daystoyrmndays(nums):
    yrs = int(nums / 365)
    mon = int((nums % 365) / 30)
    days = int((nums % 365) % 30)
    result = yrs, "years" , mon , "months" , days, "days"
    st = ''.join(map(str, result))
    return st

udffunc = udf(daystoyrmndays)
.withColumn("daystoyrmon", udffunc(col("dtdiff")))
'''
