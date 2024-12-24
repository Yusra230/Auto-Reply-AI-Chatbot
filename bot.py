import pyautogui
import pyperclip
import time
import google.generativeai as genai

geminiAPI = 'AIzaSyBeu-92hTKl192JmYkxHHwsUUs8vX0G1Pw'

def is_last_message_from_sender(chat_log, sender_name="Fatima"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    print(messages)
    if messages.startswith(sender_name):
        return True 
    return False

pyautogui.click(657, 876)
time.sleep(1)

while True:
    time.sleep(2)
    pyautogui.moveTo(603, 181)
    pyautogui.dragTo(825, 825 , duration=1.0,button='left')

    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(603, 181)
            
    chat_history=pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        genai.configure(api_key=geminiAPI)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"{chat_history}\nYou are a person named Yusra who speaks hindi as well as english. You are from Pakistan. You analyze chat history and response like Yusra. Output should be the next chat response dont include timings and name Yusra, reply concisely and reply like a human")
        print(response.text)
        reply = response.text
        pyperclip.copy(reply)

        pyautogui.click(791, 812)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')







