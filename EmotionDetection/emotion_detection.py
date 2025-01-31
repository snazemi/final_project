import requests, json

def emotion_detector(text_to_analyze):

    # entering the API call details as per Task 2 details
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    # make the POST call and receive response
    response = requests.post(URL, json=input_json, headers=headers)
    formatted_response = ''

    # extract the set of emotions from response
    if response.status_code == 200:
        json_response = json.loads(response.text)
        formatted_response = {
            'anger': json_response["emotionPredictions"][0]["emotion"]["anger"],
            'disgust': json_response["emotionPredictions"][0]["emotion"]["disgust"],
            'fear': json_response["emotionPredictions"][0]["emotion"]["fear"],
            'joy': json_response["emotionPredictions"][0]["emotion"]["joy"],
            'sadness': json_response["emotionPredictions"][0]["emotion"]["sadness"],
            'dominant_emotion': ''
        }


        # calculate and set the dominant_emotion
        highest_emotion = 0
        for emotion_name in formatted_response.keys():
            if(isinstance(formatted_response[emotion_name], float)):
                if highest_emotion < formatted_response[emotion_name]:
                    highest_emotion = formatted_response[emotion_name]
                    formatted_response["dominant_emotion"] = emotion_name


    return formatted_response
