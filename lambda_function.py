import json
from base64 import b64encode

import boto3
from botocore import exceptions

polly = boto3.client("polly")


def lambda_handler(event, context):
    """Lambda function handler to convert text to speech.
    It takes the following parameters: inputText, voiceId, and textType.

    :param event: The event passed to the lambda function.
    :param context: The context passed from the lambda function.
    :return: The response from the Polly API.
    """
    # Get the parameters from the event
    input_text = event["inputText"]
    voice_id = event["voiceId"]
    selected_interpreter = event["textType"]
    types_of_interpretation = ["ssml", "text"]
    output_text = None

    try:
        """Check if the selected interpreter is valid and is in the list of types
        and decide what type of text to use. Otherwise raise a ValueError
        """
        if selected_interpreter in types_of_interpretation:
            if selected_interpreter == "ssml":
                output_text = (
                    f"<speak><phoneme alphabet='ipa' ph='{input_text}' /></speak>"
                )
            elif selected_interpreter == "text":
                output_text = input_text
        else:
            raise ValueError("Selected interpreter is not valid")
    except ValueError as ve:
        return {"statusCode": 400, "error": str(ve)}

    try:
        # Early return if the input text or voice id is empty
        if not input_text:
            raise ValueError("Missing inputText")
        if not voice_id:
            raise ValueError("Missing voiceId")

        # Synthesize speech from input text
        speech = polly.synthesize_speech(
            OutputFormat="ogg_vorbis",
            TextType=selected_interpreter,
            Text=output_text,
            VoiceId=voice_id,
        )
    # Handle exceptions
    except exceptions.ClientError as ce:
        return {"statusCode": 400, "error": str(ce)}
    except ValueError as ve:
        return {"statusCode": 400, "error": str(ve)}

    # Return the content type and the base64-encoded audio stream as a string in the body of the response
    response = {
        "statusCode": 200,
        "contentType": speech["ContentType"],
        "body": "base64," + str(b64encode(speech["AudioStream"].read()), "utf-8"),
    }

    # Return the response
    return response
