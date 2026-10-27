from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())
from pyspark.sql.types import (
    StructType, StructField, LongType,
    StringType, DoubleType
)

schema = StructType([
    StructField("customer_id", LongType(), False),
    StructField("segment", StringType(), True),
    StructField("score", DoubleType(), True)
])
