import whisper, pyaudio, wave, keyboard, edge_tts, asyncio, pygame, os, time

model = whisper.load_model("tiny.en")
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

def record_audio_on_keypress():
    # ... (Your original record_audio_on_keypress code) ...
    # Be sure to include all necessary imports and the logic here
    pass

def speech_to_text(audio_path):
    result = model.transcribe(audio_path, fp16=False)
    return result["text"].strip()

def speak(text):
    # ... (Your original speak code) ...
    pass