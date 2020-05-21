"""
Accumulator variables are used for aggregating the information through
associative and commutative operations. For example,
You can use an accumulator for a sum operation or 
counters. The following code block has the details

class pyspark.Accumulator()
"""

from pyspark import SparkContext
sc = SparkContext("local", "Accumulator app")

num = sc.accumulator(10)
def f(x):
    global num
    num += x
rdd = sc.parallelize([20, 30, 40, 50])
rdd.foreach(f)

final = num.value
print("Accumulated value is %i" % (final))
print("***"*20)
