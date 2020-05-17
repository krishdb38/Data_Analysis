from pyspark import SparkContext
sc = SparkContext("local" , "local app")
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
counts = words.count()
print("*"*20)
print("Number of elements in RDD --> %i"%(counts))
# Elements are 8
print("*"*20)