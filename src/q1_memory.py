from pyspark.sql import SparkSession
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    spark = SparkSession.builder.appName("Q1_Memory_Optimized").getOrCreate()
    df = spark.read.json(file_path)

    date_counts = defaultdict(int)
    user_counts = defaultdict(lambda: defaultdict(int))
    
    for row in df.collect():
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S%z').date()
        date_counts[date] += 1
        user_counts[date][row['user']['username']] += 1
    
    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    result = []
    for date, _ in top_dates:
        top_user = max(user_counts[date].items(), key=lambda x: x[1])[0]
        result.append((date, top_user))

    spark.stop()
    return result
