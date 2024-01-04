## Clustering Tweets (from Twitter/X) using the k-means algorithm

### This assignment is a part of my assignments in CS 4375: Machine Learning

---

Twitter offers a platform for disseminating brief, concise communications. Frequently, these tweets exhibit considerable similarity, allowing them to be aggregated into distinct clusters. This aggregation of akin tweets facilitates the creation of a streamlined and structured synthesis of the original tweet data. Such a refined representation is immensely beneficial for various Twitter-centric applications, including but not limited to, (e.g., truth discovery, trend analysis, search ranking, etc.).

I created this program by:

- Used the Good Health dataset from UCI and performed the required pre-processing steps (removing Tweet ID & timestamp, removing any word that starts with the "@" symbol, removing any hashtag symbols, removing any URL, converting every word to lowercase)

- Performed K-means clustering on the resulting tweets using at least 5 different values of K & reported my results in a table.

How to run: This is a python code genertated with Google Colab Python notebooks. Ensure you are in the proper directory if using a terminal and run the following command: python kmeans-run.py

If you are running via an IDE, then make sure that Python is installed and simply press Run. 
IMPORTANT: Make sure that you have the goodhealth.txt file in the same directory as the .py file.

# Part 2

Libraries utilized:
re — Regular expression operations
