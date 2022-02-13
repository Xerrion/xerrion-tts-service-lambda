# Xerrion TTS Service
A text-to-speech service that I created over the weekend.
The goal was to challenge me to become more familiar with the AWS services.

The function itself takes two methods GET and POST.  
If you post to the function, it will return a JSON object with status code 200 and a base64 encoded string of the audio bytes stream.


## Licenses

- The Lambda function code itself is released under the MIT license
- The boto3 package which is used extensively in the code, is released under the [Apache 2.0 License](https://aws.amazon.com/apache-2-0/).
