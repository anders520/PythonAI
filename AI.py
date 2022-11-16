import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        
        if name is not None:
            self.__name = name

        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        sentence = "My name is " + self.__name
        self.say(sentence)

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("Say something")
        with self.m as source:
            audio = self.r.listen(source)
        print("Got it")

        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="en-us")
            sentence = "Got it, you said " + phrase
            self.say(sentence)
        except e as error:
            print("Sorry, didn't catch that ",e)
            self.say("Sorry, didn't catch that ")
        print("You said", phrase)