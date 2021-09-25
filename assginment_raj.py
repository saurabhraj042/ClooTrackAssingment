# Hash Map implementation.
class HashMap:
   def __init__(self):
        # Max size for the Hash Table
        self.max_size = int(1e5)

        # Initialize a Global Hash Table of max_size
        self.hash_map = [0] * self.max_size

        # Taking a prime number for Hash Function purpose
        self.prime_no = 799

    # Function that gets us the Key value for every User.
   def get_hash_key(self, username):
        key_value = 0
        size = len(username)

        for i in range(0, size):
            # Here ord() function gets us the ASCII value of current char.
            key_value = ((i * self.prime_no * ord(username[i])) + key_value) % self.max_size
        
        return key_value


    # Function to extract the username from the tweet
   def extract_user(self, tweet):
        user = ""
        for char in tweet:
            if char == ' ' : break
            user += char
        
        return user



# Function to get the list of Most Active Users.
def get_most_activeUsers(hashMapObj, tweets, maxNoOfTweets):
    most_active_users = set()

    for tweet in tweets:
        user_name = hashMapObj.extract_user(tweet)

        hash_key = hashMapObj.get_hash_key(user_name)

        no_of_tweetsByUser = hashMapObj.hash_map[hash_key]

        if maxNoOfTweets == no_of_tweetsByUser :
            most_active_users.add(user_name)
    
    return most_active_users


# Function to Update the hash table for each user.
def update_user_tweetCount(hashMapObj, tweet):
    user_name = hashMapObj.extract_user(tweet)
    hash_key = hashMapObj.get_hash_key(user_name)
    hashMapObj.hash_map[hash_key] += 1


# Gets the count of tweets posted by the most active user.
def get_max_noOfTweets(hashMapObj):
    no_tweets_posted = 0

    for no_tweets in hashMapObj.hash_map:
        no_tweets_posted = max(no_tweets_posted, no_tweets)
    
    return no_tweets_posted


# Helper function to take input of tweets.
def get_input_ofTweets(hashMapObj, tweets, noOfTweets):
    print("Start entering the tweets :")

    for j in range(0, noOfTweets):
        tweet = input()
       
        # Building my Hash Table
        update_user_tweetCount(hashMapObj, tweet)
        
        tweets.append(tweet)


"""""
Assignment: Find who tweeted the most

You will be given a list of tweets
Your program should find the user who has tweeted the most.
If multiple users are having the same number of tweets, then print all the users in alphabetical order of user names.

Sample :::

Input 
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6

Output
kohli 2
sachin 2
sehwag 2



"""""

# Taking input from the console the number of Test Cases
no_test_cases = int(input("Please Enter Number of Test cases :"))

# Taking input of Tweets from the console
for i in range(0, no_test_cases):
    no_of_tweets = int(input("Please Enter the Number of Tweets :"))
    new_hashMap = HashMap()
    tweets = []
    
    # Take input of Tweets.
    get_input_ofTweets(new_hashMap, tweets, no_of_tweets)
    
    # Sorting tweets beforehand to maintain the lexicographical order.
    tweets.sort()

    # Finding the Number of tweets posted by most active user.
    no_tweets_posted = get_max_noOfTweets(new_hashMap)
    
    # We iterate the tweets again to find the user with max number of tweets.
    most_active_users = get_most_activeUsers(new_hashMap, tweets, no_tweets_posted)

    # If there are multiple users who posted max number of tweets we print them.
    for user in most_active_users:
        print("%s %s" % (user, no_tweets_posted))

   

