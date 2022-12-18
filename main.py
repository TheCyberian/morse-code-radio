import morse_code
import subprocess
from pyfiglet import figlet_format
from termcolor import colored

def main():
    banner = figlet_format('Morse code Radio')
    print(colored(banner, 'green'))
    try:
        frequency = float(input('> enter the FM frequency for transmission here: '))       
        message = str(input('> enter the message for transmission here: '))
        result = morse_code.encode(message)
        print(result)
        morse_code.generate_morse_code_wav(message)    
    except ValueError:
       print("Not a valid value! Exiting.")
       exit(1)
    
    try:
       repeat = int(input('> enter the number of times transmission repeats (default (or 0) is infinite): '))
    except ValueError:
       print("No or wrong value was provided! Taking default value")
       repeat = 0

    print(repeat)
    if not repeat:
        subprocess.run(['sudo', './fm_transmitter', '-f', str(frequency), 'output.wav', '-r'])
    else:
        for i in range(repeat):
            subprocess.run(['sudo', './fm_transmitter', '-f', str(frequency), 'output.wav'])


if __name__ == '__main__':
    main()
