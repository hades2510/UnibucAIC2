from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())

tx = (spark.range(1_000_000)
    .withColumnRenamed("id", "transaction_id")
    .withColumn("customer_id",
        (F.rand(42) * 10_000).cast("int"))
    .withColumn("amount",
        F.round(F.rand(43) * 500 + 1, 2))
)

tx.show(10);
