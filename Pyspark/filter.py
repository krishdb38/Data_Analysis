"""
A new RDD is returned containing the elements, which
satisfies the function inside the filter,
In the following example,
We filter out the strings containg 'spark'
"""

from pyspark import SparkContext
sc = SparkContext("local" , "Filter app")
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

words_filter = words.filter(lambda x : "spark" in x)
filtered = words_filter.collect()
print("***"*20)
print("Filtered RDD -->%s"%(filtered))