from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


df = spark.createDataFrame(
    [(100,'sundar'),(200,'mary')], schema='id int, name string'
)
df.printSchema()
df.show()
