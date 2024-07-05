from pyspark.sql import SparkSession
from typing import List, Tuple
from datetime import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    spark = SparkSession.builder.appName("Q1_Time_Optimized").getOrCreate()
    df = spark.read.json(file_path)
    
    df.createOrReplaceTempView("tweets")
    query = """
        SELECT date, COUNT(*) as tweet_count
        FROM tweets
        GROUP BY date
        ORDER BY tweet_count DESC
        LIMIT 10
    """
    result = spark.sql(query).collect()
    top_dates = [(row['date'], row['tweet_count']) for row in result]

    # For each top date, find the user with the most tweets
    top_users = []
    for date, _ in top_dates:
        user_query = f"""
            SELECT user.username as username, COUNT(*) as tweet_count
            FROM tweets
            WHERE date = '{date}'
            GROUP BY user.username
            ORDER BY tweet_count DESC
            LIMIT 1
        """
        top_user = spark.sql(user_query).collect()[0]['username']
        top_users.append((date, top_user))

    spark.stop()
    return top_users
