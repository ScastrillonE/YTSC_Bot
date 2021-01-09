from youtube_dl import YoutubeDL



def get_audio(music_url,name_user):
    try:
        """
            Get info music
        """
        video_info =YoutubeDL().extract_info(
        url= f"{music_url}",download=False)

        """
            Create name for music file and folder with name user
        """
        filename = f"{name_user}/{video_info['title']}.mp3"


        options={
        'format': 'bestaudio/best',
            'outtmpl':filename,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

        with YoutubeDL(options) as ydl:
            ydl.download([video_info["webpage_url"]])
        
        return filename
    except:
        return "fail"