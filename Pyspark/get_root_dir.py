""""
In Apache Spark, you can upload your files using sc.addFile (sc is your default SparkContext) and get the path on a worker using SparkFiles.get. Thus, SparkFiles resolve the paths to files added through SparkContext.addFile().

SparkFiles contain the following classmethods −

get(filename)
getrootdirectory()


"""
from pyspark import SparkContext
from pyspark import SparkFiles

finddistance = "./datas/text_count.txt"
finddistancename = "text_count.txt"

sc = SparkContext("local", "SparkFile App")
print("***"*20)
print("Absolute Path %s"%SparkFiles.get(finddistancename))