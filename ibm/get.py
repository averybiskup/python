import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions

def process(key, text):
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

    return (json.dumps(response, indent=2))
