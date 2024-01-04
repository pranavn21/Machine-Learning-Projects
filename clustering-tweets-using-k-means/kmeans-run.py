import random as rd
import re
import math
import string


def clean_tweets(file):
    f = open(file, "r", encoding="utf8")
    tweets = list(f)
    tlist = []

    for i in range(len(tweets)):

        # remove \n  
        tweets[i] = tweets[i].strip('\n')

        # Remove the tweet id and timestamp
        tweets[i] = tweets[i][50:]

        # Remove word that starting with  @
        tweets[i] = " ".join(filter(lambda x: x[0] != '@', tweets[i].split()))

        # Remove any URL
        tweets[i] = re.sub(r"http\S+", "", tweets[i])
        tweets[i] = re.sub(r"www\S+", "", tweets[i])

        # remove colons from end
        tweets[i] = tweets[i].strip()
        tweet_len = len(tweets[i])
        if tweet_len > 0:
            if tweets[i][len(tweets[i]) - 1] == ':':
                tweets[i] = tweets[i][:len(tweets[i]) - 1]

        # Remove hash-tags
        tweets[i] = tweets[i].replace('#', '')

        # Convert to lowercase
        tweets[i] = tweets[i].lower()

        # convert each tweet to list
        tlist.append(tweets[i].split(' '))

    f.close()

    return tlist

def k_means(tweets, k, max_iterations=30):

    centroids = []

    # initialization, assign random tweets as centroids
    count = 0
    hash_map = dict()
    while count < k:
        rand_idx = rd.randint(0, len(tweets) - 1)
        if rand_idx not in hash_map:
            count += 1
            hash_map[rand_idx] = True
            centroids.append(tweets[rand_idx])

    iter_count = 0
    prev_centroids = []

    # run till converged or max iterations
    while (chk_conv(prev_centroids, centroids)) == False and (iter_count < max_iterations):

        print("running iteration " + str(iter_count))

        # assign tweets to the closest centroids
        clusters = assign_cluster(tweets, centroids)

        #  check convergence
        prev_centroids = centroids

        # update centroids
        centroids = update_centroids(clusters)
        iter_count = iter_count + 1

    if (iter_count == max_iterations):
        print("max iterations reached, K means not converged")
    else:
        print("converged")

    sse = getSSE(clusters)

    return clusters, sse

def chk_conv(prev_centroid, new_centroids):
    if len(prev_centroid) != len(new_centroids):
        return False

    # check duplication
    for x in range(len(new_centroids)):
        if " ".join(new_centroids[x]) != " ".join(prev_centroid[x]):
            return False
    return True

def assign_cluster(tweets, centroids):

    clusters = dict()

    for t in range(len(tweets)):
        min_dis = math.inf
        cluster_idx = -1;
        for x in range(len(centroids)):
            dis = jDist(centroids[x], tweets[t])

            if centroids[x] == tweets[t]:
                cluster_idx = x
                min_dis = 0
                break

            if dis < min_dis:
                cluster_idx = x
                min_dis = dis

        if min_dis == 1:
            cluster_idx = rd.randint(0, len(centroids) - 1)

        clusters.setdefault(cluster_idx, []).append([tweets[t]])
        last_tweet_idx = len(clusters.setdefault(cluster_idx, [])) - 1
        clusters.setdefault(cluster_idx, [])[last_tweet_idx].append(min_dis)

    return clusters

def update_centroids(clusters):

    centroids = []

    for i in range(len(clusters)):
        min_dis_sum = math.inf
        centroid_idx = -1

        # avoid redundant calculations
        min_dis_dp = []

        for t1 in range(len(clusters[i])):
            min_dis_dp.append([])
            dis_sum = 0
            # get distances for every pair
            for t2 in range(len(clusters[i])):
                if t1 != t2:
                    if t2 < t1:
                        dis = min_dis_dp[t2][t1]
                    else:
                        dis = jDist(clusters[i][t1][0], clusters[i][t2][0])

                    min_dis_dp[t1].append(dis)
                    dis_sum += dis
                else:
                    min_dis_dp[t1].append(0)

            if dis_sum < min_dis_sum:
                min_dis_sum = dis_sum
                centroid_idx = t1

        # append the selected tweet to the centroid list
        centroids.append(clusters[i][centroid_idx][0])

    return centroids


def jDist(tweet1, tweet2):
    return 1 - (len(set(tweet1).intersection(tweet2)) / len(set().union(tweet1, tweet2)))


def getSSE(clusters):

    sse = 0
    for i in range(len(clusters)):
        for t in range(len(clusters[i])):
            sse = sse + (clusters[i][t][1] * clusters[i][t][1])

    return sse


if __name__ == '__main__':
    tweets = clean_tweets("goodhealth.txt")

    for k in (3,5,7,8,10):
        print("Value of k ", k)
        clusters, sse = k_means(tweets, k)

        # for every cluster 'c', print size of each cluster
        for x in range(len(clusters)):
            print("Cluster ", x+1, " : " , len(clusters[x]) , " tweets")

        print("SSE : ", sse)
        print('\n')
        # next experiment
        k += 1