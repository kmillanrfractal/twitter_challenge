from pyspark.sql import SparkSession
from typing import List, Tuple
from collections import defaultdict

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    spark = SparkSession.builder.appName("Q3_Time_Optimized").getOrCreate()
    df = spark.read.json(file_path)
    
    df.createOrReplaceTempView("tweets")
    query = """
        SELECT explode(split(content, ' ')) as word
        FROM tweets
        WHERE content LIKE '%@%'
    """
    mentions_df = spark.sql(query)
    
    mentions_df.createOrReplaceTempView("mentions")
    query = """
        SELECT word, COUNT(*) as mention_count
        FROM mentions
        WHERE word LIKE '@%'
        GROUP BY word
        ORDER BY mention_count DESC
        LIMIT 10
    """
    top_mentions = spark.sql(query).collect()
    result = [(row['word'][1:], row['mention_count']) for row in top_mentions]

    spark.stop()
    return result
