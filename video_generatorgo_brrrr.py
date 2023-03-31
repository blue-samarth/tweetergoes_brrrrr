from gtts import gTTS
from moviepy.editor import *
import requests
import news_converter_brrrrr
import img_creater_brrrr

# Define the text and image to use in the video
text = news_converter_brrrrr.news_story
image_url = img_creater_brrrr.image_url

# Convert the text to an audio clip in mp3 format using gTTS
tts = gTTS(text)
tts.save("audio.mp3")

# Load the audio clip and create a clip with it
audio_clip = AudioFileClip("audio.mp3")

# Load the image and create a clip with it
response = requests.get(image_url)
image_clip = ImageClip(response.content).resize(height=720)

# Combine the audio and image clips
final_clip = CompositeVideoClip([image_clip.set_duration(audio_clip.duration), audio_clip.set_position((0,0))])

# Set the duration of the video to match the audio clip duration
final_clip = final_clip.set_duration(audio_clip.duration)

# Write the final clip to a file
final_clip.write_videofile("output.mp4", fps=24)
