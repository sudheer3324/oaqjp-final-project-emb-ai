import requests


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the input text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(
        url, json=payload, headers=headers, timeout=30
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response.raise_for_status()
    result = response.json()
    emotions = result["emotionPredictions"][0]["emotion"]

    scores = {
        key: emotions[key]
        for key in ("anger", "disgust", "fear", "joy", "sadness")
    }
    scores["dominant_emotion"] = max(
        ("anger", "disgust", "fear", "joy", "sadness"),
        key=lambda key: scores[key],
    )

    return scores
