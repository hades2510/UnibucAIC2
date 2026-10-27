from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())

df = spark.range(1_000_000)
print(df.rdd.getNumPartitions())
df.groupBy((F.col("id") % 5).alias("bucket")) \
  .count().explain()

#count=df.groupBy((F.col("id") % 5).alias("bucket")).count()
#count.show()
