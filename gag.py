from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
'''
3 env
1) learning env ... ubuntu...spark-shell..1%
2) dev & testing env ..windows...pycharm/Eclipse/Intellij..94%
3) prod env .... cloud/linux .....maven/sbt/.py files ..5%
core components.. spark
second party tools..local system .. env .. spark-shell
third party tools.. intellij/pycharm 
context: a nutshell to create different apis 
sparkContext ...rdd api
sqlContext ....dataframe api
HiveContext ...to connect hive
SparkStreaming context ... to process streaming data
SparkSession Context .... unifying all contexts and all apis. dataset api
abstraction: a fundamental element to do anything called abstraction.
sql ... table, schema (columns) ...
java... JVM object ...
Spark ...Rdd ..
unable to understand 1,2,3,4..if convert 1,2,3,4 to rdd .. spark able to understand
spark able to understand only RDD. spark don't know anything.

Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.1.2
      /_/

Using Scala version 2.12.10 (Java HotSpot(TM) 64-Bit Server VM, Java 11.0.15)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 22/08/17 12:26:32 WARN ProcfsMetricsGetter: Exception when trying to compute pagesize, as a result reporting of ProcessTree metrics is stopped


scala>

scala> val  data=Array(1,3,5,2,6)
data: Array[Int] = Array(1, 3, 5, 2, 6)

scala> val drdd=sc.parallelize(data)
drdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[0] at parallelize at <console>:26

scala> drdd.map(x=>x*x).collect()
res0: Array[Int] = Array(1, 9, 25, 4, 36)
'''
sc = spark.sparkContext
data = [1,2,3,4,5,6]
drdd=sc.parallelize(data)



