from pyspark import SparkContext
sc = SparkContext("local" , "Collect app")
words = sc.parallelize(
    ["scala",
    "java",
    "hadoop",
    "spark",
    "akka",
    "spark vs hadoop",
    "pyspark",
    "pyspark and spark"]
)

col1 = words.collect()
print("\n\n","**"*20)
print("Elemets in RDD %s"%col1)
print("\n\n","**"*20)