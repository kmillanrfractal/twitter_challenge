from pyspark.sql import SparkSession
from typing import List, Tuple
from collections import defaultdict

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    spark = SparkSession.builder.appName("Q3_Memory_Optimized").getOrCreate()
    df = spark.read.json(file_path)
    
    mentions = defaultdict(int)
    for row in df.rdd.toLocalIterator():
        for word in row['content'].split():
            if word.startswith('@'):
                mentions[word[1:]] += 1
    
    top_mentions = sorted(mentions.items(), key=lambda x: x[1], reverse=True)[:10]

    spark.stop()
    return top_mentions
