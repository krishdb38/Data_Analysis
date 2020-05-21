"""
the element RDD is returned. In the following example
we are importing add package from the operator and applying 
it on "numm" to carry out a simple addition operation

"""
from pyspark import SparkContext
from operator import add

sc = SparkContext("local", "Reduce app")
nums = sc.parallelize([1,2,3,4,5])
adding = nums.reduce(add)

print("***"*20)
print("Addition ", adding)
print("***"*20)