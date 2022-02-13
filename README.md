# Xerrion TTS Service
A text-to-speech service that I created over the weekend.
The goal was to challenge me to become more familiar with the AWS services.

The function itself takes two methods GET and POST.  
If you post to the function, it will return a JSON object with status code 200 and a base64 encoded string of the audio bytes stream.
