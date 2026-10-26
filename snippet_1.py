from pyspark.sql import SparkSession
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())
print(spark.version)
