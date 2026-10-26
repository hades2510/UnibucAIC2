from pyspark.sql import SparkSession
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())

df = spark.range(1_000_000)
df.printSchema()
df.show(50)
print(df.count())
