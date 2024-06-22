from audio_transcription import get_transcription_from_audio
from timebudget import timebudget
from record_voice import record_voice
import os
import pyaudio
import wave
from faster_whisper import WhisperModel
from record_voice import *
import keyboard
from llm_response import *
##Push-to-talk


count = 0
frames = []
format = pyaudio.paInt16
channels = 1
rate = 16000
chunks = 1024

while True:

    if keyboard.is_pressed('F1') and count == 0:
        print("Start recording")
        audio = pyaudio.PyAudio()
        stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunks)
        count = 1
    if keyboard.is_pressed('F1') == True and count == 1:
        print("recording...")
        stream, audio, rate, channels, format, frames = push_to_talk_start(stream, audio, frames)
        count = 1
    if keyboard.is_pressed('F1') == False and count == 1:
        print("stopping recording")
        push_to_talk_end("./audio/recording.wav", stream, audio, rate, channels, format, frames)
        count = 0
        transcription = get_transcription_from_audio("./audio/recording.wav",model_size = "medium.en")
        print(transcription)
        response = get_llm_response(transcription)
        create_audio_file(response["choices"][0]["message"]["content"],"./audio/response.wav")
        play_audio("./audio/response.wav")
        frames = []

total_transcription = ""

#real-time
# try:
#     while True:
#         record_voice("./audio/recording.wav", chunk_record_time=1)
        

        
#         t = get_transcription_from_audio("./audio/recording.wav",model_size = "base")
#         total_transcription += t


#         os.remove("./audio/recording.wav")
#         print(t)
#         count += 1
# except KeyboardInterrupt:
#     print("Transcription: ", total_transcription)