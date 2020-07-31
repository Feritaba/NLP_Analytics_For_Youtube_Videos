# NLP_Analytics_For_Youtube_Videos

My project will help social media influencers working on social media to generate a better content related to their area, in order to gain more followers or viewers. The goal of this project is to help influencers as an advisor what area they should focus on for content generation. I will analyze the oral content spoken in their videos. In the end this application will present them diagrams and descriptive visualization of the words they used and engagement they got. I want to specialize this application for people who speak English or Persian.

## Steps:

1. Initiate OAuth flow and exchange user token.
2. Query Youtube API and gather video links and information. [*In Progress*]
3. Download audio of the video and prepare for text extraction.
4. Use cloud Speech-to-text Google API to extract the transcripts. [*In Progress*]
5. Clean the extracted transcript and calculate NLP artifacts.
6. Exploratory data analysis on the created data set


### 2- Query Youtube API and gather video links and information.

- GetVideoList.py & GetVideo_withJSONKey.py

Choosing the most important social media 'Youtube' for the first steps. 'GetVideoList.py' returns the list of the videos of a channel. I was experimenting with OAuth flow. This is only for helping me to explore Youtube API.

### 4. Use cloud Speech-to-text Google API to extract the transcripts. [*In Progress*]

- sampleSpeech2Text.py

This file converts local audio files to transcripts using Google API.
