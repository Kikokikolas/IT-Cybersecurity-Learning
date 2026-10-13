curl -vk --connect-timeout 10 --max-time 20 --resolve blog.futurevera.thm:443:10.128.134.95 https://blog.futurevera.thm/

curl does a connection to a server, -vk shows connection details and HTTP headers --resolve resolves the IP to the name -k skips certificate validation; it does not show details.

Hostname was found in DNS cache we putted in the command

* Connected to blog.futurevera.thm (10.128.134.95) port 443 we are connected to the https
 ALPN: curl offers h2,http/1.1 curl is saying the protocol to comunicate

 TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):

TLS handshake so the connection is secure


-k meant curl did not require a valid, trusted server certificate.

SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / X25519 / RSASSA-PSS SSL connection is using TLSv1.3
* ALPN: server accepted http/1.1
ALPN server accepted the client protocol

* Server certificate:
*  subject: C=US; ST=Oregon; L=Portland; O=Futurevera; OU=Thm; CN=blog.futurevera.thm
*  start date: Mar 13 10:22:57 2022 GMT
*  expire date: Mar 13 10:22:57 2023 GMT
*  issuer: C=US; ST=Oregon; L=Portland; O=Futurevera; OU=Thm; CN=blog.futurevera.thm
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* using HTTP/1.x

Server shows the information of the certificate

> GET / HTTP/1.1
> Host: blog.futurevera.thm
> User-Agent: curl/8.5.0
> Accept: */*

here we do a GET to receive the text/HTML
Host: identifies the requested site
User identiifes the clinet software: curl verison 8.5.0
Accept - the client acceyps any media type

* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
idk 

> is us
< is the server response

< HTTP/1.1 200 OK
< Date: Sun, 11 Oct 2026 22:47:53 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Last-Modified: Sun, 13 Mar 2022 08:26:19 GMT
< ETag: "efe-5da15516fc0c0"
< Accept-Ranges: bytes
< Content-Length: 3838
< Vary: Accept-Encoding
< Content-Type: text/html

The servers responds with 200 Ok so its going to show us the page
The date server we already talked about this
Last-Modified: When the server says the resource was last changed
ETag: A version identifier clients can use to check whether cached content is still current.
Accept reanges: The server supports requesting a portion of the resource by byte range, useful for resuming downloads.
COntent length is 3838 byes, Headers are not included
Vary - Caches must consider the request’s Accept-Encoding when choosing a stored response.
Contenty type already said it its gona show html text

<!DOCTYPE html> the html we using
html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>FutureVera - Blogs</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">FutureVera</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto py-4 py-lg-0">
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="post.html">Post</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Page Header-->
        <header class="masthead" style="background-image: url('assets/img/home-bg.jpg')">
            <div class="container position-relative px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <div class="site-heading">
                            <h1>FutureVera Blog</h1>
                            <span class="subheading">Blogging website for futurevera.thm</span>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- Main Content-->
        <div class="container px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-center">
                <div class="col-md-10 col-lg-8 col-xl-7">
                    <!-- Post preview-->
                    <div class="post-preview">
                        <a href="post.html">
                            <h2 class="post-title">Man must explore, and this is exploration at its greatest</h2>
                            <h3 class="post-subtitle">Problems look mighty small from 150 miles up</h3>
                        </a>
                        <p class="post-meta">
                            Posted by
                            <a href="#!">FutureVera</a>
                            on September 24, 2021
                        </p>
                    </div>
                    <!-- Divider-->
                    <hr class="my-4" />
                </div>
            </div>
        </div>
        <!-- Footer-->
        <footer class="border-top">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <div class="small text-center text-muted fst-italic">Copyright &copy;futurevera.thm</div>
                    </div>
                </div>
            </div>
        </footer>
	<!-- Theme is taken from https://startbootstrap.com -->
	<!-- Bootstrap core JS-->
        <script src="js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</html>
* Connection #0 to host blog.futurevera.thm left intact
 All the data shown

 curl -v --connection-timeout 10 --max-time 20 --resolve practice.example:443:192.0.2.10 https://practice.example