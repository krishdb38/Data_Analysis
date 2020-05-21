"""
Persist this RDD with the default storage level (Memory_Only).
You can also check  if RDD  cached or not
"""
from pyspark import SparkContext

sc = SparkContext("local", "Cache app")

words = sc.parallelize(
    ["scala",
    "java",
    "akka",
    "pyspark",
    "pyspark and spark"
    ]
)
words.cache()
caching = words.persist().is_cached

print("**"*20)
print("Words got chached %s"%(caching))