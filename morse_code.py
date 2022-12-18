from playsound import playsound
from time import sleep
from pydub import AudioSegment
# Dictionary representing the international morse code
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': ' '}

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def encode(message):
    cipher = ''
    for letter in message.upper():
        if letter.isalnum():
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '/ '
    return cipher


def decode(message):
    symbols = message.split()
    decipher = [REVERSE_MORSE_CODE_DICT[s] if (
        s != '/') else ' ' for s in symbols]
    return ''.join(decipher)


def play_morse_code(message):
    for character in encode(message.upper()):
        if character == '.':
            playsound('sounds/dit.wav')
            sleep(0.2)
        if character == '-':
            playsound('sounds/dah.wav')
            sleep(0.2)
        if character == ' ' or character == '/':
            sleep(0.32)


def generate_morse_code_wav(message):
    dah = AudioSegment.from_wav('sounds/dah.wav')
    dit = AudioSegment.from_wav('sounds/dit.wav')
    space_05 = AudioSegment.from_wav('sounds/silent_quarter-second.wav')
    space_10 = AudioSegment.from_wav('sounds/silent_half-second.wav')

    combined = AudioSegment.empty()
    for character in encode(message.upper()):
        if character == '.':
            combined += (dit + space_05)
        if character == '-':
            combined += (dah + space_05)
        if character == ' ' or character == '/':
            combined += space_10
    combined.export("output.wav", format="wav")
