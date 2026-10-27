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
tx.groupBy("category").count().show()
#tx.groupBy("category").count().sort("count").show()
