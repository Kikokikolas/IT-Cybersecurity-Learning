# DNS

The **Domain Name System (DNS)** translates domain names into IP addresses.

```text
example.com -> 93.184.215.32
```

Computers communicate using IP addresses, but IP addresses are difficult for
people to memorise. DNS lets us use names such as `google.com` instead.

## What Happens When You Visit a Website

Suppose you enter:

```text
https://www.example.com
```

Before the browser can send the `GET /` request, it must discover the IP address
for `www.example.com`.

```text
User
	|
	| enters www.example.com
	v
Browser
	|
	| "What is the IP address of www.example.com?"
	v
DNS resolver
	|
	| finds the answer
	v
IP address: 93.184.216.34
	|
	v
Browser
	|
	| HTTPS/HTTP request
	v
Web server
	|
	v
Webpage
```

In short:

- **DNS**: Where is the server?
- **HTTP/HTTPS**: Send me the webpage or data.