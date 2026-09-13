# Security

## Privacy and Security

The main purpose of security is to inspect whether the page is being delivered securely and to inspect things such as:

- HTTP status
- TLS/certificate information
- Insecure HTTP origins
- mixed content
- third-party cookie behaviour
- security details per origin

For example:

```text
https://example.com
        |
        v
Valid certificate
        |
        v
Encrypted TLS connection
        |
        v
Secure origin
```

The Security panel helps determine whether the browser is communicating
securely with the website and whether insecure resources are being loaded.

