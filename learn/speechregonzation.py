import speech_recognition as sr

r=sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
with harvard as source:
    audio1 = r.record(source, duration=4)
    audio2 = r.record(source, duration=4)
with harvard as source:
    audio3 = r.record(source, offset=4.7, duration=3)

print(r.recognize_google(audio))
print(r.recognize_google(audio1))
print(r.recognize_google(audio2))
print(r.recognize_google(audio3))

