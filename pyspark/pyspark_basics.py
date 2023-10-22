from pyspark import SparkContext

# RDD
# DATAFRAME
sc = SparkContext("local","Transformaton demo") # represents spark cluster connection and can be used for creating spark RDDs and broacasting the variable
# on the cluster
words_list = sc.parallelize(
    ["pyspark",
     "interview",
     "questions"]
)
filtered_words = words_list.filter(lambda x: 'interview' in x)
# transformation - create a new RDD for these operations # resilient distributed datasets.
filtered = filtered_words.collect()
print(filtered)

# actions
counts = filtered_words.count()
print(counts)
