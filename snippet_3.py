from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())

df = spark.range(1_000_000)
df.printSchema()

result = (df
    .withColumn("customer_id", F.col("id") % 10000)
    .filter(F.col("customer_id") < 5000)
    .select("id", "customer_id")
)

result.printSchema()
result.show(5)
print(result.count())
