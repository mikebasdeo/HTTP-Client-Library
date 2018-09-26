# HTTP-Client-Library
Implementation of GET and HTTP POST requests similar to cURL, using TCP Sockets directly. 

## Command Examples
### Get
./httpc.py get http://httpbin.org/get?course=networking"&"assignment=1
### Get (Verbose)
./httpc.py get -v http://httpbin.org/get?course=networking"&"assignment=1
### Post
./httpc.py post -d "hello_world" http://httpbin.org/post
### Post (Verbose)
./httpc.py post -v -d "hello_world" http://httpbin.org/post

### Post with multiple inline headers
./httpc.py post -d "hello_world" -h Content-Type:application/json -h Content-length:10  http://httpbin.org/post

### Post that associates the content of a file to the body HTTP POST 
./httpc.py post -f "data.txt" -h Content-Type:application/json  http://httpbin.org/post

### Output response to file 
./httpc.py post -v -d "hello_world" -o "output.txt" http://httpbin.org/post

## For Demo
### Get
httpc get http://httpbin.org/get?course=networking"&"assignment=1
### Get (Verbose)
httpc get -v http://httpbin.org/get?course=networking"&"assignment=1
### Post
httpc post -d "hello_world" http://httpbin.org/post
### Post (Verbose)
httpc post -v -d "hello_world" http://httpbin.org/post

### Post with multiple inline headers
httpc post -d "hello_world" -h Content-Type:application/json -h Content-length:10  http://httpbin.org/post

### Post that associates the content of a file to the body HTTP POST 
httpc post -f "data.txt" -h Content-Type:application/json  http://httpbin.org/post

### Output response to file 
httpc post -v -d "hello_world" -o "output.txt" http://httpbin.org/post
