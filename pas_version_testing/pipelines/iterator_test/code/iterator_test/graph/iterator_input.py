from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from iterator_test.config.ConfigStore import *
from iterator_test.functions import *

def iterator_input(spark: SparkSession) -> DataFrame:
    return spark.read.table("`dfinch`.`premier_val_map`.`iterator_input`")
