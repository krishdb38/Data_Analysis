"""
A new RDD is returned by applying a function to each element
in the RDD.In the following example,
we form a key value pair and map every string with a value 1
"""

from pyspark import SparkContext
sc = SparkContext("local", "Map app")
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

words_map = words.map(lambda x: (x,1))
mapping = words_map.collect()
print('Key value pair  %s'%(mapping))