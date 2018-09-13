# HTTP-Client-Library
Implementation of GET and HTTP POST requests similar to cURL, using TCP Sockets directly. 


## Command Examples
### Get
./httpc.py --get http://httpbin.org/get?course=networking"&"assignment=1
### Get (Verbose)
./httpc.py --get -v http://httpbin.org/get?course=networking"&"assignment=1
### Post
./httpc.py --post -d "hello_world" http://httpbin.org/post
### Post (Verbose)
./httpc.py --post -v -d "hello_world" http://httpbin.org/post
