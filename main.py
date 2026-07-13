from src.voice_utils import record_audio_on_keypress, speech_to_text, speak
from src.brain import get_response
import os

if __name__ == "__main__":
    while True:
        audio_file = record_audio_on_keypress()
        if audio_file is None: break
        
        user_text = speech_to_text(audio_file)
        if not user_text: continue
        
        reply = get_response(user_text)
        speak(reply)
        
        if os.path.exists(audio_file):
            os.remove(audio_file)