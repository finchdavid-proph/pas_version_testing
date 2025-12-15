from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from iterator_test.config.ConfigStore import *
from iterator_test.functions import *
from prophecy.utils import *
from iterator_test.graph import *

def pipeline(spark: SparkSession) -> None:
    df_iterator_input = iterator_input(spark)
    TableIterator_1(Config.TableIterator_1).apply(spark, df_iterator_input)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("iterator_test").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/iterator_test")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/iterator_test", config = Config)(pipeline)

if __name__ == "__main__":
    main()
