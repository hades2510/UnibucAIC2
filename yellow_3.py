from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())


df = spark.read.parquet(
"yellow_tripdata_2025-01.parquet"
)

