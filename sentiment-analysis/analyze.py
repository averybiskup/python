import json
import os
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions


with open('secret.json') as secret:
    data = json.load(secret)
    KEY = data['key']

def process(text, key=KEY):
    naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey=key,
        url='https://gateway.watsonplatform.net/natural-language-understanding/api')

        # t = 'IBM is an American multinational technology company '
        # 'headquartered in Armonk, New York, United States, '
        # 'with operations in over 170 countries.'

    t = text

    try:
        response = naturalLanguageUnderstanding.analyze(text=t,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
            limit=2))).get_result()
    except:
        return False

    print(json.dumps(response, indent=2))
    return (json.dumps(response, indent=2))

process('IBM watson is an actual piece of shit. I hate it a lot.')
