#   ___       ____ _____ 
#  / _ \__  _| ___|___ / 
# | | | \ \/ /___ \ |_ \ 
# | |_| |>  < ___) |__) |
#  \___//_/\_\____/____/
#
# Param-Fuzzer -> By 0x53.
# Twitter: @0x53oficial
# GitHub: https://github.com/0x53oficial/
# Website: https://0x53.me/

try:
    import requests, argparse;
except ImportError:
    print("[Error] - An error ocurred in importing of the modules!");
    exit();

session = requests.session();

parser = argparse.ArgumentParser(description='Param-Fuzzer by 0x53 | Script to found params in Web Services.');
parser.add_argument('--version', action='version', version='Param-Fuzzer 1.0.0');
parser.add_argument('--wordlist','-w', action='store', dest='wordlist', help='Set the Wordlist.', required=True)
parser.add_argument('--target','-t', action='store', dest='target', help='Set the target.', required=True)
parser.add_argument('--value', '-v', action='store', dest="value", default='1337', help='Set the default value of the param in request.')
arguments = parser.parse_args();

def doRequest(target):
    try:
        return len((session.get(target)).content);
    except:
        print('[Error] - An error ocurred in the communication with target. Check and something try again!');
        exit();

def fuzz():
    try:
        wordlist = open(arguments.wordlist, 'r', errors='ignore');
    except:
        print('[Error] - No such file: ' + arguments.wordlist);
        exit();

    default = doRequest(arguments.target + "?paramfuzzertestdefaultvalue=1");

    for param in wordlist.read().splitlines():
        target = arguments.target + '?' + param + '=' + arguments.value;
        
        if doRequest(target) != default:
            print('[+] Possible Param Found: ' + target);

    print("\n[*] Ended - See u again :)");

fuzz(); 