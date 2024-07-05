from pyspark.sql import SparkSession
from typing import List, Tuple
from collections import defaultdict
import emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    spark = SparkSession.builder.appName("Q2_Memory_Optimized").getOrCreate()
    df = spark.read.json(file_path)
    
    emoji_counts = defaultdict(int)
    for row in df.rdd.toLocalIterator():
        for char in row['content']:
            if char in emoji.EMOJI_DATA:
                emoji_counts[char] += 1
    
    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    spark.stop()
    return top_emojis
