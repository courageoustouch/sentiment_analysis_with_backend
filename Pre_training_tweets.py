from new_preprocessing import pre_process_tweets
from Training_dataset import cleaned_training_tweets

train_tweet_processor = pre_process_tweets()
preprocessed_training_tweets = train_tweet_processor.preprocessed_tweets(cleaned_training_tweets)



