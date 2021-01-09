from bot import YTSC_Bot 
from downloadYT import get_audio

bot = YTSC_Bot("config.cfg")
update_id=0

while True:
    print("...")
    updates = bot.get_updates(update_id)
    updates = updates["result"]

    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            
            from_ = item["message"]["from"]["id"]
            name = item["message"]["from"]["first_name"]

            audio = get_audio(message,name)
            
            if audio != "Fail":
                bot.send_audio(from_, audio)
            else:
                bot.send_messages("No pude obtener la cancion de esta url :c", from_)
            #bot.send_messages(validation_message(message),from_)
            

