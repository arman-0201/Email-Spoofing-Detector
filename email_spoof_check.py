from emailSpoofDetection import emailSpoofDetection
import sys
from termcolor import cprint, colored

    
try:
    file_path=sys.argv[1]

    emailDomain = input(colored('enter the email domain: ', 'yellow'))
    with open(file_path, 'r') as header:
        analysis = emailSpoofDetection(header, emailDomain)
        if analysis:
            print(' ')
            cprint('No spoofing detected!', 'yellow')
        else:
            print(' ')
            cprint('email spoofing detected!', 'red')

except FileNotFoundError:
    print(' ')
    cprint("file not found...", 'red')
except IndexError:
    print(' ')
    cprint('wrong parameters...', 'red')
except KeyboardInterrupt:
    print(' ')
    cprint('exiting...', 'red')
