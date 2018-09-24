#!/usr/bin/env python

# Mike Basdeo - 2018

import socket
import argparse
import re
import sys
from argparse import RawTextHelpFormatter

url_regex = "^((http?):\/)?\/?([^:\/\s\?]+)(\/get\?[^:]+)?"

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, int(port)))

    sock.send(message.encode())
    response = sock.recv(len(message), socket.MSG_WAITALL)
    if(args.verbose):
        sys.stdout.write(response.decode("utf-8"))
    print(sock.recv(4096).decode("utf-8"))

# Create Parser to pull out url from the command line
parser = argparse.ArgumentParser(description='Mike Basdeo - 26788815 \r\nhttpc is a curl-like application but supports HTTP protocol only', add_help=False, formatter_class=RawTextHelpFormatter)
parser.add_argument('--help', action='help', help='show this help message and exit')

parser.add_argument('mode', choices=['get','post'], help="Executes a HTTP GET or POST request for a given URL with inline data")

#positional requirement (mandatory no dash)
parser.add_argument('url', action="store", help="mandatory uniform resource locator to perform requet on")

#Data Command (optional)
parser.add_argument('-d', dest="data", action="store", metavar="inline-data", help="associates inline data to the body HTTP POST")
#Header Command (optional)
parser.add_argument('-h', dest="header", action="store", metavar="inline-data", help="associates headers to HTTP Request with the format")

#Read From File Command (optional)
parser.add_argument('-f', dest="file", action="store", metavar="inline-data", help="associates the content of a file to the body HTTP POST")

#Verbose Command (optional)
parser.add_argument('-v','--verbose', action="store_true")

args = parser.parse_args()

#chop up the found url using regex
matcher = re.search(url_regex, args.url)

server = matcher.group(3)

query_param = ''
if(matcher.group(4)):
    query_param = matcher.group(4)
port = 80

#Get Request
if(args.mode == 'get'):
    message  = 'GET /'+query_param+' HTTP/1.1\r\n'
    message += 'Host:' +server+':'+str(port)+'\r\n'
    message += 'Connection: close\r\n'
    message += '\r\n'
    connect()

#Post Request
if(args.mode == 'post'):
    if(args.data):
        data = args.data
    if (args.file):
        with open (args.file, "r") as myfile:
            data=myfile.read()
    
    print(data)
    data_bytes = data.encode()
  
    message  = 'POST /post HTTP/1.1\r\n'
    message += 'Content-length:'+str(len(data_bytes))+'\r\n'
    message += 'Host:' +server+':'+str(port)+'\r\n'
    message += 'Connection: close\r\n\r\n'
    message += data+'\r\n'
    connect()



