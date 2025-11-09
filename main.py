from speak import speak
from listen import listen
import time

def main():
    speak("Halo, saya asisten pribadimu. Siap mendengarkan.")
    time.sleep(1)

    while True:
        text = listen()

        if "selesai" in text or "keluar" in text:
            speak("Baik, sampai jumpa!")
            break

        elif "halo" in text:
            speak("Halo juga! Senang mendengarmu.")

        elif "cuaca" in text:
            speak("Saat ini cuaca cerah dan menyenangkan.")

        elif "musik" in text:
            speak("Baik, saya akan memutar musik favoritmu nanti.")

        elif "apa kabar" in text:
            speak("Saya baik, terima kasih! Kamu sendiri bagaimana?")

        elif text.strip() == "":
            continue

        else:
            speak("Hmm, saya belum mengerti maksudmu.")

if __name__ == "__main__":
    main()
