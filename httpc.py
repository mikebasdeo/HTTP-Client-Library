#!/usr/bin/env python

# Mike Basdeo - 2018

import socket
import argparse
import re
import sys

url_regex = "^((http?):\/)?\/?([^:\/\s\?]+)(\/get\?[^:]+)?"

# Create Parser to pull out url from the command line
parser = argparse.ArgumentParser(description='Mike Basdeo - 26788815 - COMP445 - Fall 2018 Lab Assignment #1')

#positional requirement (no dash)
parser.add_argument('url', action="store")

#Get Command (optional)
parser.add_argument('-g','--get', action="store_true")

#Post Command (optional)
parser.add_argument('-p','--post', action="store_true")

#Data Command (optional)
parser.add_argument('-d', dest="data", action="store", metavar="inline-data", help="Associates an inline data to the body HTTP POST")

#Verbose Command (optional)
parser.add_argument('-v','--verbose', action="store_true")

args = parser.parse_args()

#chop up the found url
matcher = re.search(url_regex, args.url)

#print("Group 1",matcher.group(1))
#print("Group 2",matcher.group(2))
#print("Group 3",matcher.group(3))
#print("Group 4",matcher.group(4))
server = matcher.group(3)

query_param = ''
if(matcher.group(4)):
    query_param = matcher.group(4)
port = 80

#Get Request
if(args.get):
    message  = 'GET /'+query_param+' HTTP/1.1\r\n'
    message += 'Host:' +server+':'+str(port)+'\r\n'
    message += 'Connection: close\r\n'
    message += '\r\n'

#Post Request
if(args.post):
    data = args.data
    data_bytes = data.encode()
    message  = 'POST /post HTTP/1.1\r\n'
    message += 'Content-length:'+str(len(data_bytes))+'\r\n'
    message += 'Host:' +server+':'+str(port)+'\r\n'
    message += 'Connection: close\r\n\r\n'
    message += args.data+'\r\n'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, int(port)))

sock.send(message.encode())
response = sock.recv(len(message), socket.MSG_WAITALL)
if(args.verbose):
    sys.stdout.write(response.decode("utf-8"))
print(sock.recv(4096).decode("utf-8"))


