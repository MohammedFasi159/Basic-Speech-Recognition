import streamlit as st
import speech_recognition as sr
import pyttsx3

st.title("🎤 Simple Speech Recognition App")

st.write("Click below and speak a command. The app will recognize your speech and respond.")

if st.button("Start Listening"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak something!")
        audio = recognizer.listen(source, phrase_time_limit=5)
        st.success("Processing...")

    try:
        text = recognizer.recognize_google(audio)
        st.write(f"🗣 You said: **{text}**")

        if "hello" in text.lower():
            response = "Hello! How are you?"
        elif "time" in text.lower():
            import datetime
            response = f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        elif "your name" in text.lower():
            response = "I am your speech recognition assistant."
        else:
            response = "Sorry, I didn’t understand that."

        st.write(f"🤖 Response: **{response}**")

        # ✅ Safe TTS for Streamlit
        def speak(text):
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            engine.stop()

        speak(response)

    except sr.UnknownValueError:
        st.error("Sorry, I couldn’t understand your voice.")
    except sr.RequestError:
        st.error("Speech recognition service is unavailable right now.")


