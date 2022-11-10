import speech_recognition as sr

recognizer = sr.Recognizer()

# print microphone list
# print(sr.Microphone.list_microphone_names())

with sr.Microphone() as microphone:
    recognizer.adjust_for_ambient_noise(microphone)
    print("Pode falar que eu vou gravar")
    audio = recognizer.listen(microphone)
    text = recognizer.recognize_google(audio, language='pt-BR')
    print(text)