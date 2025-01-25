
import random
from random import randint
import PySimpleGUI as sg

adjectives = {
    "slimy", "moist", "funky", "slippery", "distended",
    "crusty", "blownout", "floppy", "dusty", "leaky"
}

nouns = {
    "vulva", "penis", "ballonknot", "foreskin", "tiddies",
    "taint", "vag", "butthole", "grundel", "weener"
}

special = {
    "!", "@", "#", "$", "%", "^", "&", "*"
}

def genpwd():
    adj = random.choice(list(adjectives))
    sp = random.choice(list(special))
    noun = random.choice(list(nouns))
    num = str(randint(100,999))
    return adj + sp + noun.capitalize() + num

#set theme
sg.theme('DarkGray13')

layout = [
    [sg.Text("Dirty Password Generator", font=('Helvetica', 20))],
    [sg.Text("Your Generated Password:", font=('Helvetica', 12))],
    [sg.Text('', size=(30,1), key='-PASSWORD-', font=('Helvetica', 14))],
    [sg.Button("Generate Password", key='-GENERATE-', size=(15,1))],
    [sg.Button("Copy to Clipboard", key='-COPY-', size=(15,1))],
    [sg.Button("Exit", size=(15,1))]
]

# Create the Window with finalize=True
window = sg.Window("Password Generator", layout, size=(400,250),
                  element_justification='center', finalize=True)

# Generate and display initial password
current_password = genpwd()
window['-PASSWORD-'].update(current_password)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '-GENERATE-':
        current_password = genpwd()
        window['-PASSWORD-'].update(current_password)

    if event == '-COPY-':
        sg.clipboard_set(current_password)
        sg.popup("Password copied to clipboard!", auto_close=True, auto_close_duration=1)

window.close()
