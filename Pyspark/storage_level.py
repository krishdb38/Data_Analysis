"""
StorageLevel decides how RDD should be stored.
In Apache Spark, StorageLevel decides whether RDD should be stored 
in Memory or should it be stored over the disk,
or both.
It also decides whether to serialize RDD and
 whether to replicate RDD partitions

class pyspark.StorageLevel(useDisk,\
            useMemory, useOffHeap, deserialized, replication = 1)

Now, to decide the storage of RDD, there are different storage levels, which are given below −

DISK_ONLY = StorageLevel(True, False, False, False, 1)
DISK_ONLY_2 = StorageLevel(True, False, False, False, 2)
MEMORY_AND_DISK = StorageLevel(True, True, False, False, 1)
MEMORY_AND_DISK_2 = StorageLevel(True, True, False, False, 2)
MEMORY_AND_DISK_SER = StorageLevel(True, True, False, False, 1)
MEMORY_AND_DISK_SER_2 = StorageLevel(True, True, False, False, 2)
MEMORY_ONLY = StorageLevel(False, True, False, False, 1)
MEMORY_ONLY_2 = StorageLevel(False, True, False, False, 2)
MEMORY_ONLY_SER = StorageLevel(False, True, False, False, 1)
MEMORY_ONLY_SER_2 = StorageLevel(False, True, False, False, 2)
OFF_HEAP = StorageLevel(True, True, True, False, 1)

"""
from pyspark import SparkContext
import pyspark

sc = SparkContext("local", "storagelevel app")

rdd1 = sc.parallelize([1, 2])
rdd1.persist(pyspark.StorageLevel.MEMORY_AND_DISK_2)
rdd1.getStorageLevel()
print(rdd1.getStorageLevel())