import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('GLqpdYi7lxaY65JjYV1ea_1q1LEdBE6h4qLdJN8vs28f')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://stream.watsonplatform.net/speech-to-text/api')


class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))


myRecognizeCallback = MyRecognizeCallback()

with open(join(dirname(__file__), '../../data/active-listening/216.22/', '211565170421539231567025556.wav'), 'rb') \
        as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/wav',
        recognize_callback=myRecognizeCallback,
        model='en-US_NarrowbandModel',
        inactivity_timeout=400,
        timestamps=True,
        speaker_labels=True,
        profanity_filter=False,
        smart_formatting=True,
        audio_metrics=True,
        redaction=False)

