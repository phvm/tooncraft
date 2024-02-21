import elevenlabs
import time

#elevenlabs.set_api_key("my-api-key")

speech = "Áudio teste"
voiceId = "Antoni" 

audio = elevenlabs.generate(
    text = speech,
    voice = voiceId
)

hora = time.strftime("%Y%m%d-%H%M%S")
filename = "./audios_elevenlabs/" + voiceId + "_" + hora + ".mp3"
print("salvando", filename)
elevenlabs.save(audio=audio,  
        filename=filename
        )