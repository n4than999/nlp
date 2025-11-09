import pyttsx3

def speak(text):
    """Fungsi untuk membuat asisten berbicara"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # Kecepatan bicara
    engine.setProperty('volume', 1.0)  # Volume 0.0 - 1.0

    voices = engine.getProperty('voices')
    # Pilih suara (0: laki-laki, 1: perempuan — tergantung OS)
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()
