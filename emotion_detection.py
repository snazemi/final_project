import json, requests

def emotion_detector(text_to_analyze):
    """
    In the emotion_detection.py file, write the function to run emotion detection using the appropriate Emotion Detection function. Name this function emotion_detector.
    Note: Assume that that text to be analyzed is passed to the function as an argument and is stored in the variable text_to_analyze. The value being returned must be the text attribute of the response object as received from the Emotion Detection function.
    """

    # entering the API call details as per Task 2 details
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    # make the POST call and receive response
    response = requests.post(URL, json=input_json, headers=headers)

    return response.text
