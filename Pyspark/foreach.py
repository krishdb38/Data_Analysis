#!bin/python3
"""
Returns only those elements which meet the condition of the 
Function inside foreach.
In the following example, we call aprint function in foreach,
which prints all the elemens in the RDD
"""

from pyspark import SparkContext
sc = SparkContext("local" , "ForEach app")
words = sc.parallelize(
    ["scala",
    "java",
    "hadoop",
    "akka",
    "spark Vs hadoop",
    "pyspark",
    "pyspark and spark"]
)
def f(x):
    print(x)

fore = words.foreach(f)
print(fore)