import pyttsx3

engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 3)  # Volume (0.0 to 1.0)

# Speak text
engine.say("Hello i am shayan hassan i am learning python")

# Play the speech
engine.runAndWait()
