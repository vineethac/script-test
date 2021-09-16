'''
Usage: python3 dns_check.py --dns=<fqdn> --time=<time_in_seconds>
Example1: python3 dns_check.py --dns=example.com --time=60
Example2: python3 dns_check.py --dns=example.com --time=60 > dns_output.txt &
'''

import socket
import sys
import time
import datetime 
from optparse import OptionParser

# hostname = sys.argv[1]
# seconds = sys.argv[2]
 
parser = OptionParser()

parser.add_option("--dns",
                  dest = "hostname",
                  type = 'string')
parser.add_option("--time",
                  dest = "seconds",
                  type = 'int')
  
(options, args) = parser.parse_args()

# IP lookup from hostname
def dns_to_ip(hostname, seconds):
    start_time = time.time()
    IST = pytz.timezone('Asia/Kolkata')
    while True:
        
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        if elapsed_time > seconds:
            break

        else:
            try:
                ip = socket.gethostbyname(hostname)
                print(f'{datetime.datetime.now(IST)} DNS {hostname} IP Address is {ip}')
            except socket.gaierror as e:
                print(f'{datetime.datetime.now(IST)} Unable to resolve hostname! Error is {e}.')

        time.sleep(1)

dns_to_ip(options.hostname, options.seconds)
