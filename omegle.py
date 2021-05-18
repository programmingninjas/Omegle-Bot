from python_omegle import InterestsChat
from python_omegle import ChatEvent
import time

chat = InterestsChat(['science','programming','coding','python','computer science','stem','anime'])  #Add any as you want
while True:
    chat.start()
    while True:
        event, argument = chat.get_event()
        if event == ChatEvent.CHAT_READY:
            common_interests = argument
            print("- Connected, common interests: {} ".format(*common_interests))
            break
    chat.start_typing()
    time.sleep(5)
    chat.send("Hey how are you")
    chat.start_typing()
    time.sleep(15)
    chat.send("Good to know")
    chat.start_typing()
    time.sleep(10)
    chat.send("i have a coding page on instagram its interesting make sure to check it out")
    chat.start_typing()
    time.sleep(3)
    chat.send('@programmingninjas')
    chat.start_typing()
    time.sleep(5)
    chat.send('sorry i gtg now take care goodbye')
    chat.start_typing()
    time.sleep(2)
    chat.disconnect()
