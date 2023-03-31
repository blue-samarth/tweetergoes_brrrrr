# tweetergoes_brrrrr


This Python code uses the Tweepy library to search Twitter for tweets containing a specific hashtag (#crypto) and extracts various details of those tweets, including their ID, text, number of likes, number of retweets, and number of quote tweets. The extracted data is then saved to a CSV file named "tweets.csv".

The code first loads the Twitter authentication credentials from a YAML configuration file named "config.yaml" using the PyYAML library. It then sets up an OAuthHandler object with the consumer key and secret from the configuration, and sets the access token and secret for the authorized user.

Next, the code sets up the Tweepy API object using the previously configured auth object. It sets the wait_on_rate_limit parameter to True to ensure that the API client waits for the rate limits to reset if the limit is reached, and the wait_on_rate_limit_notify parameter to True to enable notifications when the client is waiting for the rate limits to reset.

The code then sets up the search query for the hashtag and opens a CSV file named "tweets.csv" in write mode to save the extracted data. It uses the csv.writer() function to create a CSV writer object and writes the header row to the CSV file.

Finally, the code uses the tweepy.Cursor() function to extract the tweets and their details, and writes each row of tweet data to the CSV file. The CSV file is then closed.



This code reads in a CSV file with tweet data, concatenates all tweet descriptions into a single string, and then uses OpenAI's text summarization API to summarize the tweets. The summarized news story is then extracted from the API response and printed to the console. Note that in order to use the OpenAI API, you will need to set your API key in the openai.api_key variable.


The news_converter_brrrrr module is imported, which contains the news_story variable that was created in the previous script.

The requests and json modules are imported, which are needed for making HTTP requests and parsing JSON responses.

The PIL (Python Imaging Library) module is imported, which is needed for working with images.

The API endpoint and API key are defined.

The prompt for the image is set to the news story.

The request parameters are set, including the model to use, the prompt, the number of images to generate, the size of the images, and the response format (URL).

The API request is sent using the requests.post() method.

The URL of the generated image is extracted from the API response using the json.loads() method to parse the JSON content.

The image is not downloaded or displayed in this script, but code to do so is commented out at the bottom.


It imports necessary modules, including gTTS for converting text to an audio clip, moviepy.editor for working with video clips, requests for making HTTP requests, news_converter_brrrrr which contains the news_story variable with the text of the news story, and img_creater_brrrrr which contains the image_url variable with the URL of the image related to the news story.

It defines the text and image_url variables using the news story and image URL from the imported modules.

It uses gTTS to convert the text variable to an audio clip in mp3 format, and saves it to a file called audio.mp3.

It loads the audio.mp3 file and creates an audio clip with it.

It loads the image from the image_url variable and creates a video clip with it. The image is resized to a height of 720 pixels.

It combines the audio and image clips into a final clip using CompositeVideoClip.

It sets the duration of the final clip to match the duration of the audio clip.

It writes the final clip to a file called output.mp4 using the write_videofile method.
