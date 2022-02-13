# Xerrion TTS Service
A service I created over the weekend to challenge myself to become more familiar with AWS services.

The function itself takes to methods GET and POST.  
If you post to the function, it will return a JSON object with status code 200 and a base64 encoded string of the audio file.