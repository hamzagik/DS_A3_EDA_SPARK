from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc

# Initialize Spark Session
spark = SparkSession.builder.appName("Netflix EDA").getOrCreate()

# Load Datasets
credits_df = spark.read.csv("/app/credits.csv", header=True, inferSchema=True)
titles_df = spark.read.csv("/app/titles.csv", header=True, inferSchema=True)

# Show schemas
print("Credits DataFrame Schema:")
credits_df.printSchema()

print("Titles DataFrame Schema:")
titles_df.printSchema()

# Count the number of movies and TV shows
print("Count of Movies and TV Shows:")
titles_df.groupBy("type").count().show()

# Count titles by release year
print("Titles Count by Release Year:")
titles_df.withColumn("release_year", col("release_year").cast("int")) \
  .groupBy("release_year").count().orderBy(desc("release_year")).show()

# Most popular genres
print("Most Popular Genres:")
titles_df.select("genres").groupBy("genres").count().orderBy(desc("count")).show(10)

# Top 10 highest-rated titles by IMDb score
print("Top 10 Highest-Rated Titles by IMDb Score:")
titles_df.orderBy(desc("imdb_score")).select("title", "imdb_score", "type").show(10)

# Most frequent roles in credits
print("Most Frequent Roles in Credits:")
credits_df.groupBy("role").count().orderBy(desc("count")).show(10)

# Stop Spark Session
spark.stop()
