# DNS

DNS translates a domain name into an IP address

Example:

example.com -> 93.184.215.32

Computers communicate with IP addresses but IP addresses are hard to memorize so humans prefer things like google.com etc.

What happens when you type a website

Suppose you enter:

https://www.example.com

Before the browser can send:

GET /

it first needs to know where www.example.com is

User
 │
 │ enters www.example.com
 ▼
Browser
 │
 │ "What is the IP of www.example.com?"
 ▼
DNS Resolver
 │
 │ finds the answer
 ▼
IP address
 │
 │ 93.184.216.34
 ▼
Browser
 │
 │ Now I know where to connect
 ▼
Web Server
 │
 │ HTTPS / HTTP request
 ▼
Webpage

DNS -> where is the server?
HTTP / HTTPS -> give me the webpage/data