from audio_transcription import get_transcription_from_audio
from timebudget import timebudget



with timebudget("transcription time"):
    segments, segments_text = get_transcription_from_audio("./audio/audio.mp3")


for s in segments_text:
    print(s)

