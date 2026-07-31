import speech_recognition as sr
import cohere
import edge_tts
import asyncio
import pygame
import io

# ==========================================
# 1. Configuration
# ==========================================

# Initialize Cohere Client
COHERE_API_KEY = 'YOUR_COHERE_API_KEY'  # Replace with your actual Cohere API key
co = cohere.Client(COHERE_API_KEY)


# Initialize Speech-to-Text Recognizer
recognizer = sr.Recognizer()

# ==========================================
# 2. Core Functions
# ==========================================

def listen_to_user():
    """Captures audio from the microphone and converts it using Local Whisper."""
    with sr.Microphone() as source:

        recognizer.pause_threshold = 3.0
        
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=60)
            print("[⏳] Processing...")
            
            text = recognizer.recognize_whisper(audio, language="english")
            return text
            
        except sr.WaitTimeoutError:
            print("[❌] Listening timed out. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("[❌] Sorry, I didn't catch that.")
            return None
        except Exception as e:
            print(f"[❌] An unexpected error occurred: {e}")
            return None

def ask_cohere(prompt):
    """Sends the text prompt to Cohere and returns the response."""
    try:
        print("[🧠] Thinking...")
        response = co.chat(
            message=prompt,
            model="command-r-08-2024" 
        )
        return response.text
    except Exception as e:
        print(f"[❌] Error communicating with Cohere: {e}")
        return "I'm having trouble connecting to my brain right now."


def speak_text(text, print_text=False):
    """Converts text to speech using edge-tts and plays it."""
    if print_text:
        print(text)

    audio_bytes = io.BytesIO()
    
    async def fetch_audio():
        communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes.write(chunk["data"])
                
    asyncio.run(fetch_audio())
    

    audio_bytes.seek(0)
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio_bytes)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    # 5. Clean up the mixer
    pygame.mixer.quit()

# ==========================================
# 3. Main Loop
# ==========================================

def main():
    print("Cohere Voice Assistant Started")
    print("Press Ctrl+C to exit.")
    
    while True:
        # Step 1: Speech-to-Text
        print("[🎤] Listening! Say something...")
        user_input = listen_to_user()
        
        if user_input:
            print(f"\n[👤] You said: {user_input}")

            print(user_input.lower().strip(" .!?"))
            # Allow user to quit via voice command
            if user_input.lower().strip(" .!?") in ["quit", "exit", "stop", "goodbye"]:
                speak_text("Goodbye! Shutting down.", print_text=True)
                break
            
            # Step 2: Text-to-Cohere
            ai_response = ask_cohere(user_input)
            
            # Step 3: Text-to-Speech
            if ai_response:
                print(f"[🤖] Cohere says: {ai_response}")
                speak_text(ai_response)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[🛑] Program terminated by user.")