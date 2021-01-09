import requests
import json
import configparser as cfg

class YTSC_Bot():

    def __init__(self,config):
        self.token = self.read_token_from_file(config)
        self.url_base = "https://api.telegram.org/bot{}".format(self.token)

    def get_updates(self, offset=None):
        url = self.url_base + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset+1)
        res = requests.get(url)
        print(self.token)
        return json.loads(res.content)

    def send_messages(self,msg,chat_id):
        url = self.url_base + "/sendmessage?text={}&chat_id={}".format(msg,chat_id)
        if msg is not None:
            requests.get(url)
    
    def send_audio(self,chat_id,audio_file):
        try:
            file = {'file1': open(f"{audio_file}","rb")}
            url = "https://api.telegram.org/bot1509289034:AAEJ1A88kj8YPmzIgOT3ld-fxgI4zwkcxYw/sendVoice?chat_id={}&voice={}".format(chat_id,audio_file)
            data = requests.post(url,files=file)
            print(data.content)
        except Exception as e:
            self.send_messages(e,chat_id)
        


    def read_token_from_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)

        return parser.get('creds','token')