# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Overview
# MAGIC 
# MAGIC This notebook will show you how to create and query a table or DataFrame that you uploaded to DBFS. [DBFS](https://docs.databricks.com/user-guide/dbfs-databricks-file-system.html) is a Databricks File System that allows you to store data for querying inside of Databricks. This notebook assumes that you have a file already inside of DBFS that you would like to read from.
# MAGIC 
# MAGIC This notebook is written in **Python** so the default cell type is Python. However, you can use different languages by using the `%LANGUAGE` syntax. Python, Scala, SQL, and R are all supported.

# COMMAND ----------

# File location and type
data = "/FileStore/tables/employees-2.csv"
df = spark.read.format("csv").option("header","true").option("inferSchema","true").option("sep",",").load(data).drop("COMMISSION_PCT")
df.show()






# COMMAND ----------

from pyspark.sql import *
from pyspark.sql.functions import *
res1 = df.withColumn("HIRE_DATE",to_date(col("HIRE_DATE"),"dd-MMM-yy"))
res1.show()
win = Window.partitionBy("JOB_ID").orderBy(col("SALARY").desc())
res = res1.withColumn("drnk",dense_rank().over(win)).withColumn("rnk",rank().over(win))
#.withColumn("prnk",percent_rank().over(win)).withColumn("ntl",ntile(4).over(win))
#.where(col("drnk")>1)
res.show(50)




# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC /* Query the created temp table in a SQL cell */
# MAGIC 
# MAGIC select * from `employees-2_csv`

# COMMAND ----------

# With this registered as a temp view, it will only be available to this particular notebook. If you'd like other users to be able to query this table, you can also create a table from the DataFrame.
# Once saved, this table will persist across cluster restarts as well as allow various users across different notebooks to query this data.
# To do so, choose your table name and uncomment the bottom line.

permanent_table_name = "employees-2_csv"

# df.write.format("parquet").saveAsTable(permanent_table_name)
