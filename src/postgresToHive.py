from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local").appName("MiniProj").enableHiveSupport().getOrCreate()

df = spark.read.format("jdbc").option("url", "jdbc:postgresql://18.132.73.146:5432/testdb") \
    .option("driver", "org.postgresql.Driver").option("dbtable", "UKCityMaster") \
    .option("user", "consultants").option("password", "WelcomeItc@2022").load()
df.printSchema()



sorted_df.write.mode("overwrite").saveAsTable("mucteba.UKCityMaster")
print("Successfully Load to Hive")

# spark-submit --master local[*] --jars /var/lib/jenkins/workspace/nagaranipysparkdryrun/lib/postgresql-42.5.3.jar src/FirstLoadPostgressToHive.py