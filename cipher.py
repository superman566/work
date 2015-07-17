import simplegui
import random

cipher = {}
letter = "abcdefjhefaldjfoiqajwfnsadkfkashjfuiq"

        
message = ""

#helping function
def init():
    letter_list = list(letter)
    random.shuffle(letter_list)
    for ch in letter_list:
        cipher[ch] = letter_list.pop()
    print cipher
    
def input_handle(text):
    global message
    message = text
    label.set_text(message)
   # print message

def encode():
    en_message = ""
    global cipher
    for ch in message:
        en_message += cipher[ch]
    print en_message    

def decode():
    de_message = ""
    global cipher
    for ch in message:
        for key in cipher:
            if ch == cipher[key]:
                de_message += key
    print de_message       
    
    

frame = simplegui.create_frame("Cipher", 2, 200,200)
frame.add_input("Message:", input_handle, 200)
label = frame.add_label("",200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)
init()
frame.start()