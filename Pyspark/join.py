"""
It returns RDD with a pair of elements with the matching
keys and all the values for the particular key.
In the following example, there are two pair of elements in two 
differents in two different RDDs. 
After joining these two RDDs, We get an RDD with elements having 
matching keys and their values
"""

from pyspark import SparkContext
sc = SparkContext("local", "join app")
x = sc.parallelize([("spark", 1), ("Hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])

joined = x.join(y)
final = joined.collect()

print("/n","***"*20)
print("Joined RDD",final)