import speech_recognition as sr
from pprint import pprint

r = sr.Recognizer()                 # Recognizer-Instanz versucht Speache zu erkennen
with sr.Microphone() as source:     # Mit dem Mikrofon als Quelle
    print("Text einsrepchen: \n")
    r.adjust_for_ambient_noise(source, duration=0.8)
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    eingesprochener_Text = r.recognize_google(audio,language="DE-de", show_all=True) # show_all gibt alle möglich verstandenen Ergebenisse zurück
    print("Google Speech Recognition hat verstanden: \"" + r.recognize_google(audio,language="DE-de") + "\"")
    # pprint(eingesprochener_Text)
except sr.UnknownValueError:
    print("Google Speech Recognition konnte nichts verstehen.")
except sr.RequestError as e:
    print("Konnte keine Ergebnisse von Google Speech Recognition service liefern; {0}".format(e))

# recognize speech using Houndify
# HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
# HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
# try:
#     print("Houndify verstand:")
#     print(r.recognize_houndify(audio, client_id="1DEaYtAM4VVrjC6OW0sfCQ==", client_key="LGQL5WnTtIWeEgwlweQbMxZ0UQWi5zpyP-eHN6RPM9QccxFlXIS3ZFv0J4sUVoW5rAM_Mewar0t7ufIJH2n4zA==", show_all=True))
# except sr.UnknownValueError:
#     print("Houndify could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Houndify service; {0}".format(e))
