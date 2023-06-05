import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('tepst') \
    .getOrCreate()

# After creating the SparkSession it's possible to access the web interface in localhost:4040

sc = spark.sparkContext

rdd1 = sc.parallelize(range(100))
rdd1.collect()

rdd2 = rdd1.map(lambda x: 2*x)
rdd2.collect()

rdd3 = sc.parallelize([1, 1, 1, 2, 2])
rdd3.reduce(lambda a, b: a + b)

rdd1.count()

