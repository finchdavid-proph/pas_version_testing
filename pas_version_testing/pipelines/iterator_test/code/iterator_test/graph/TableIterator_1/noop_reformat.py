from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from iterator_test.functions import *

def noop_reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(expr(Config.logic).alias("logic_string_test"))
