## INTRO

Hello there,

I am the CEO and one of the co-founders of futurevera.thm. In Futurevera, we believe that the future is in space. We do a lot of space research and write blogs about it. We used to help students with space questions, but we are rebuilding our support.

Recently blackhat hackers approached us saying they could takeover and are asking us for a big ransom. Please help us to find what they can takeover.

Our website is located at https://futurevera.thm

Im gona startu to look for pages that shouldnt be in the url, after if i dont discover nothing im going to look for vulnaribilities in the code, btw i already did

 nmap -sV 10.130.144.236
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-10-11 22:42 WEST
Nmap scan report for futurevera.thm (10.130.144.236)
Host is up (0.12s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http     Apache httpd 2.4.41 ((Ubuntu))
443/tcp open  ssl/http Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.23 seconds
kiko@kiko-IdeaPad-Slim-3-15ARP10:~$ 

so we have ssh to explore to.

## FIRST STEP


to explore differente URLS we going to use ffuf

ffuf -u https://futurevera.thm/FUZZ -w ~/Desktop/Tools/SecLists/Discovery/Web-Content/common.txt -k

this is -u the URL that we gona test and -w the file we gona use

ffuf -u https://futurevera.thm/FUZZ -w ~/Desktop/Tools/SecLists/Discovery/Web-Content/common.txt -k -o resultados.html -of html this command saves the file in our folder, -of html defines HTML format so its easier to read

we found this 
![alt text](image.png)

But none of them have what we are looking for

I just realised that we tried directories, with the ffuf but the description of the challenge is challenge revolves around subdomain enumeration LOLLLLL

We going to try subdomains support.futurevera.thm, ... blog.futurevera.th... till we find some to explore

A domain is a name such as futurevera.thm. A subdomain is a name beneath that domain, such as blog.futurevera.thm, and may point to the same server or a different one.
In https://blog.futurevera.thm/posts, blog.futurevera.thm is the hostname and /posts is the path. The hostname identifies the site to contact, while the path identifies a resource within that site.
Therefore, blog.futurevera.thm and futurevera.thm/blog are different: the first uses a subdomain, while the second uses a path on the main domain. A URL path does not necessarily correspond to a physical folder on the server.

So now we going to do ffuf on the subdomain

ffuf -u https://futurevera.thm/ -H "Host: FUZZ.futurevera.thm" -w ~/Desktop/Tools/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -k -ac -o subdominios.html -of html

-H "Host: FUZZ.futurevera.thm" this time we use this for subdomain

### Why the report was empty: HTTP 421

This command tests virtual hosts on the same server by changing the HTTP `Host` header. It does not look up DNS records for each subdomain.

With HTTPS, the original command uses two names:

- `-u https://futurevera.thm/` sets the TLS server name (SNI) to `futurevera.thm`.
- `-H "Host: FUZZ.futurevera.thm"` requests a name such as `blog.futurevera.thm` inside that connection.

In our manual test, the server rejected this mismatch with `421 Misdirected Request`. The default ffuf status matcher does not include 421, so these responses would not appear in the report. An empty report does not prove that no subdomains exist.

To include all HTTP response codes, including 421, add `-mc all`. Remove `-ac` as well so automatic calibration does not filter these responses:

```bash
ffuf -u https://futurevera.thm/ -H "Host: FUZZ.futurevera.thm" -w ~/Desktop/Tools/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -k -mc all -o subdominios.html -of html
```

- `-mc all` includes every HTTP status code in the results; connection errors are not HTTP responses.
- Removing `-ac` disables automatic calibration and may produce many repeated results.
- A **421 response alone does not confirm that a subdomain exists**. This command makes the rejected requests visible; it does not fix the HTTPS name mismatch.
- The command runs a new scan and writes `subdominios.html` in the current directory, replacing the previous report if it has the same name.

### Next step after HTTP 421: request the blog directly with curl

After the 421 error, we used `curl` to request the blog directly over **HTTPS**:

```bash
curl -vk --connect-timeout 10 --max-time 20 --resolve blog.futurevera.thm:443:10.128.134.95 https://blog.futurevera.thm/
```

We changed two things:

- In the URL, we used `https://blog.futurevera.thm/` so the connection requested the blog from the start.
- With `--resolve`, we told curl to connect to `10.128.134.95` for `blog.futurevera.thm` on port 443, without editing `/etc/hosts`.

Both the HTTPS server name (SNI) and the HTTP Host header now used `blog.futurevera.thm`. The names matched, so the server accepted the request and returned the blog page.

This returned **200 OK**, a certificate with `CN=blog.futurevera.thm`, and a page titled **FutureVera - Blogs**. The blog site was confirmed, but no takeover vulnerability has been identified yet.

The IP `10.128.134.95` was used in this successful test. Check the current lab IP before repeating it, because restarting the machine may change its IP.

Next, inspect the blog's `about.html` and `post.html` pages and test `support.futurevera.thm` using the same matching-name approach.

So now taht we know that blog.futurevera.thm exists we go explore it

## SECOND STEP

When we did ffuf -u https://futurevera.thm/ -H "Host: FUZZ.futurevera.thm" -w ~/Desktop/Tools/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -k -ac -o subdominios.html -of html we wanted to know if the server runned another machines. A server with a single IP can host many websites.

After doing this occured a problem, in HTTPS, the name of the site is also delivred when it starts a secure connection, before the request of the page. The command was only altering the name of the request.

So we connected but requesting the page it didnt show, in the manual test the server showed that with the 421, because we not only have that but we dont have a IP associated with the blog page.

Then to test the blog.futurevera.thm page

Just for resume. In HTTPS the sequency of connection is:

1) Connect to the server - to the IP and port of the web server
2) Prepare the secure connection (TLS) - the client indicates the site name by SNI, receives the certificate and negotiate the encryption.

SIN - Server Name Indication - The name of the site that the client says when starting the HTTP connection

3) Sends the HTTP request in that secure connection, requests the page and indicates again the site on the header Host
4) Recevies the answerr- like 200 OK and the HTML

In the test, we send futurever.thm on step 2 and blog.futurevera.thm on step 3. The server received it and denied it with 421

So then i did curl -vk --connect-timeout 10 --max-time 20 --resolve blog.futurevera.thm:433:10.128.134.95 https://blog.futurevera.thm/

We used `curl` to test the connection and `--resolve` to map `blog.futurevera.thm` to the machine’s IP for that command, because we had not added the subdomain to `/etc/hosts`. Using `https://blog.futurevera.thm/` as the URL ensured that the blog’s hostname was used both when establishing the HTTPS connection (SNI) and when sending the HTTP request (`Host`).

-v is verbose shows deaitls of the connection, of the certificate and answers and questions
-k ignores the validation of the certifi
--max-time 20 limitates the operation to 20 seconds

After we run the command we receive 200 OK and the page FutureVera-Blogs. This confirmed the page. Unfortonately we explored the code of the page and nothing interesting was there so we moved on to ther other 421 we receive on the support.futurevere.thm

## THIRD STEP

curl -vk --connection-timeout 10 --max-time 20 --resolve support.futurevera.thm:433:10-128.134.95 https://suport.futurevera.thm/

We also receive 200 OK and the title of the page. The page didnt have much information so we explored the HTTPS certificate

Basically when we open a https://support.futurever.thm. before requesting the page

1) Browser start the connection indicates the website name by the SNI
2) The server shows the certificate
3) The browser verifies if the certificate is valid to the name if its in expiration date and if it trust on how sign it
4) If its all ok, concludes connection and browser sends the HTTP

The certificate can have 

SAN - Subject Alternative Name - Lists the names of sites covered by the certificate
Public Key - Helps to verificate if the server has the private key
Emissor - Identifies who sign the certificate.
Expirate data - Indicates when the certificate is no longer valid

We used openssl s_client -connect 10.128.134.95:443 -servername support.futurevera.thm </dev/null 2>/dev/null | openssl x509 -noout -subject -ext subjectAltName  to see the data from the certificate

openssl s_client connects to the server and gets the supoort certificate
openssl x509 reads the certificate and show is primal identity (subject) and additional names (SAN)

We run this line and we got
subject=C = US, ST = Oregon, L = Portland, O = Futurevera, OU = Thm, CN = support.futurevera.thm
X509v3 Subject Alternative Name:
    DNS:secrethelpdesk934752.support.futurevera.thm

    | Field | Value | Meaning |
|---|---|---|
| `C` | US | Country |
| `ST` | Oregon | State or region |
| `L` | Portland | Locality |
| `O` | Futurevera | Organization |
| `OU` | Thm | Organizational unit |
| `CN` | support.futurevera.thm | Certificate’s common name |
| `Subject Alternative Name` | secrethelpdesk934752.support.futurevera.thm | Additional hostname covered by the certificate |

So we found a secret subdomain secrethelpdesk934752.support.futurevera.thm

We did curl -v -i --connect-timeout 10 --max-time 20 --resolve secrethelpdesk934752.support.futurevera.thm:433:10.128.134.95 http://secrethelpdesk934752.support.futurevera.thm/

We did this and just received the normal futurevera page so then we tried port 80 the http one
curl -v -i --connect-timeout 10 --max-time 20 -resolve secrethelpdesk934752.support.futurevera.thm:433:10.128.134.95 http://secrethelpdesk934752.support.futurevera.thm/

The response was this : 
HTTP/1.1 302 Found
Date: Sun, 11 Oct 2026 23:06:14 GMT
Server: Apache/2.4.41 (Ubuntu)
Location: http://flag{beea0d6edfcee06a59b83fb50ae81b2f}.s3-website-us-west-3.amazonaws.com/
Content-Length: 0
Content-Type: text/html; charset=UTF-8

This is was our flag

By the way i need to review codes, like 302 is termporary redirect

# DONE



Important

| Part | Meaning |
|---|---|
| **`HTTP/1.1`** | The HTTP version used for the response. |
| **`302 Found`** | The status code and its description. Here, it indicates a temporary redirect. |
| **`Date`** | The time the server says it generated the response, rather than exactly when you received it. |
| **`Server: Apache/2.4.41 (Ubuntu)`** | The server advertises Apache as its web-server software, with an Ubuntu label. This is reported information, not proof of the actual software or OS. |
| **`Location`** | The address the server wants the client to visit next. **This is where we found the flag.** |
| **`Content-Length: 0`** | The response body contains zero bytes. We still received the headers. |
| **`Content-Type: text/html`** | Describes the body as HTML text. In this response, the body was empty. |
| **`charset=UTF-8`** | Declares UTF-8 as the character encoding, telling the client how to interpret the body’s bytes as text. |

