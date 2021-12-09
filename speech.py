import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()
['HDA Intel PCH: ALC272 Analog (hw:0,0)',
 'HDA Intel PCH: HDMI 0 (hw:0,3)',
 'sysdefault',
 'front',
 'surround40',
 'surround51',
 'surround71',
 'hdmi',
 'pulse',
 'dmix', 
 'default']

with mic as source:
     r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

r.recognize_google(audio)