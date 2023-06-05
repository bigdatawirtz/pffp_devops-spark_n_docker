import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('tepst') \
    .getOrCreate()

# After creating the SparkSession it's possible to access the web interface in localhost:4040

sc = spark.sparkContext

# insurance data
rdd = sc.textFile('insurance.csv')

# extract the value of charges
data_lines = rdd.filter(lambda line: 'age' not in line)
charges = data_lines.map(lambda line: line.split(',')[6])
charges_values = charges.map(lambda value: float(value))

# calculate the sum of charges from all insurances
charges_values.sum()
