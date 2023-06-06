import pyspark

sc = pyspark.SparkContext()

text_file = sc.textFile("database.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

for x in counts.collect():
    print(x)