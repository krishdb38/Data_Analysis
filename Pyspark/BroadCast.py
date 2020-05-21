"""
Broadcast variables are used to save the copy of data
across all odes. This variables is cached on all the machines
and not sent on machines with tasks.
The following code has the details on Broadcast class for PySpark
"""

from pyspark import SparkContext
sc = SparkContext("local", "Broadcast app")
words_new = sc.broadcast(["scala", "java", "hadoop", "spark", "akka"])
data = words_new.value

print("*"*20)
print("Stored data ", data)
print("*"*20)
elem = words_new.value[2]
print("Printing the Particular elements in RDD", elem)
print("*"*20)
