from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = (SparkSession.builder
    .appName("IngAlgo-C4")
    .config("spark.log.level", "ERROR")
    .config("spark.ui.showConsoleProgress", "false")
    .master("local[*]")
    .getOrCreate())

tx = spark.range(100);

u = F.rand(seed=44)
tx = tx.withColumn("category",
    F.when(u < 0.60, "electronics")
     .when(u < 0.90, "clothing")
     .otherwise("books")
)

tx = tx.withColumn("amount",
    F.when(F.col("category") == "electronics",
           F.round(F.rand(45) * 900 + 100, 2))
     .when(F.col("category") == "clothing",
           F.round(F.rand(46) * 180 + 20, 2))
     .otherwise(F.round(F.rand(47) * 45 + 5, 2))
)

tx = tx.withColumn(
    "event_date",
    F.date_add(
        F.lit("2026-01-01").cast("date"),
        (F.rand(48) * 180).cast("int")
    )
)

tx = tx.withColumn("amount",
    F.when(F.rand(49) < 0.02,
           F.lit(None).cast("double"))
     .otherwise(F.col("amount"))
)

tx = tx.withColumn("customer_id", (F.rand()*10000).cast("int"));

customers = (spark.range(10_000)
    .withColumnRenamed("id", "customer_id")
    .withColumn("segment",
        F.when(F.col("customer_id") % 4 == 0,
               "premium").otherwise("standard"))
)

#tx.join(customers, "customer_id", "left").explain()
enriched = tx.join(customers, "customer_id", "left")

enriched.write.mode("overwrite").partitionBy("category").parquet("output/enriched")
