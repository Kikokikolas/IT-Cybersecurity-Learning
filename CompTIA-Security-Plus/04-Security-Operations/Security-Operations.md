DOMAIN 4 — SECURITY OPERATIONS
4.1 — Apply common security techniques to computing resources

This section is basically:

How do I make devices, servers, applications, networks, mobile devices, cloud systems, etc. more secure?

SECURE BASELINE

A secure baseline is a standard secure configuration that systems are expected to follow.

Imagine a company has 500 Windows computers.

Instead of configuring every computer differently, the company creates a standard.

Example:

Firewall = enabled
Disk encryption = enabled
Guest account = disabled
Minimum password length = 14
Automatic updates = enabled
Unused ports = closed
USB storage = restricted

That is the company's:

SECURE BASELINE

The usual lifecycle is:

Establish
   ↓
Deploy
   ↓
Maintain
Establish

Decide what the secure configuration should be.

Deploy

Apply it to systems.

Maintain

Keep checking that the systems still comply.

CONFIGURATION DRIFT

Imagine the baseline says:

Firewall = ON
SMBv1 = OFF

Three months later:

Computer 27:
Firewall = OFF
SMBv1 = ON

The system has moved away from the approved configuration.

That is:

Configuration drift

HARDENING

Hardening means:

Reducing the attack surface of a system.

The basic idea is:

If I do not need something, disable/remove/block it.

For example, a web server only needs:

HTTPS 443
SSH 22

But it also has:

FTP 21
Telnet 23
HTTP 80
SMB 445

If those services are unnecessary:

disable FTP
disable Telnet
close port 80
block SMB

This is hardening.

Other hardening examples:

uninstall unnecessary software;
disable unnecessary accounts;
change default passwords;
disable unused services;
close unnecessary ports;
install updates;
enable encryption;
configure firewall rules;
apply least privilege.
Exam memory

Hardening = remove unnecessary attack opportunities.

MOBILE DEVICE SECURITY

Mobile devices create additional risks because:

they are easily lost;
they connect to public Wi-Fi;
users install applications;
they may contain company information;
Bluetooth/NFC can introduce risks.

Controls include:

Screen lock
PIN/password
Biometric authentication
Encryption
Remote wipe
Application control
Containerization
MDM
MDM — MOBILE DEVICE MANAGEMENT

MDM allows an organization to centrally control mobile devices.

An administrator can:

enforce encryption
require PINs
install applications
remove applications
disable cameras
disable Bluetooth
restrict USB
remote lock
remote wipe
verify compliance
Example

An employee loses a company smartphone.

Best action:

Remote wipe through MDM

BYOD

Bring Your Own Device

Employee owns the device.

Example:

Employee uses their personal iPhone for company email.

Advantages:

cheaper for company;
employees already know their devices.

Problems:

company has less control;
personal and corporate data are mixed;
privacy issues.
COPE

Corporate-Owned, Personally Enabled

The organization owns the device but allows personal use.

Example:

Company gives employee an iPhone that can also be used privately.

Company has much more control than with BYOD.

CYOD

Choose Your Own Device

The employee chooses from a list of approved devices.

Example:

You may choose:

iPhone
Samsung Galaxy
Google Pixel

But only approved models.

WIRELESS SITE SURVEY

A wireless site survey examines the physical environment before or after installing Wi-Fi.

It helps determine:

access point placement;
signal strength;
interference;
dead zones;
channel usage.
Exam question

A company wants to determine the optimal placement of wireless access points.

Answer:

Wireless site survey

HEAT MAP

A heat map visually shows wireless signal strength.

It helps identify:

Strong signal
Medium signal
Weak signal
Dead zones
WPA3

WPA3 is a modern Wi-Fi security standard.

If the question asks:

Which provides stronger modern wireless security?

Think:

WPA3

802.1X

802.1X provides:

Port-based network access control

Before a user/device receives network access, it must authenticate.

Common architecture:

Supplicant
    ↓


Authenticator
    ↓
Authentication server

Example:

Laptop
↓
Switch / Access Point
↓
RADIUS
RADIUS

Remote Authentication Dial-In User Service

RADIUS provides centralized authentication and is commonly used with:

enterprise Wi-Fi;
VPN;
802.1X;
network devices.

Example:

User connects to corporate Wi-Fi
        ↓
Access Point
        ↓
RADIUS server
        ↓
Credentials checked
        ↓
Access allowed/denied

Important:

RADIUS does not encrypt Wi-Fi traffic itself.

WPA2/WPA3 handles wireless security.

RADIUS helps with authentication/AAA.

APPLICATION SECURITY
Input validation

Applications should never blindly trust user input.

Suppose an application expects:

Age: 25

But attacker enters malicious SQL/code.

Input validation checks whether the data matches the expected format.

It can help prevent:

SQL injection;
command injection;
XSS;
malformed input attacks.

Memory:

Never trust user input.

SECURE COOKIES

Cookies may contain:

session identifiers
authentication tokens
preferences

Important cookie attributes:

Secure

Cookie is only transmitted over HTTPS.

HttpOnly

JavaScript cannot directly access the cookie.

Helps reduce cookie theft through some XSS attacks.

SameSite

Restricts when cookies are sent between websites.

Helps reduce CSRF attacks.

STATIC CODE ANALYSIS — SAST

Static analysis examines code:

without running it

Example:

SOURCE CODE
     ↓
SAST scanner
     ↓
Security weaknesses

Can identify:

insecure functions;
hardcoded credentials;
coding errors;
vulnerable patterns.

Memory:

STATIC = software is standing still

DYNAMIC ANALYSIS — DAST

Dynamic analysis examines:

a running application

Example:

Application running
       ↓
Security scanner sends requests
       ↓
Application behaviour observed

Memory:

DYNAMIC = application is doing something

CODE SIGNING

Code signing uses digital signatures to provide:

authenticity;
integrity.

It allows users to verify:

This software really came from this publisher.

and:

The software has not been modified since it was signed.

Important:

Code signing primarily gives:

Integrity + authenticity

Not confidentiality.

SANDBOXING

A sandbox is an isolated environment.

Suspicious code can be executed without exposing the real system.

Example:

Suspicious attachment
        ↓
Sandbox
        ↓
Execute safely
        ↓
Observe behaviour

Very useful for malware analysis.

4.2 — ASSET MANAGEMENT

Think about the lifecycle:

Acquire
↓
Assign
↓
Inventory
↓
Monitor
↓
Decommission
↓
Dispose
ACQUISITION / PROCUREMENT

Before purchasing hardware or software, organizations should consider security.

Examples:

Does the vendor provide security updates?
Is the product already end-of-life?
Does it support encryption?
Does it meet company security standards?
Does it meet regulatory requirements?
ASSET ASSIGNMENT

Every important asset should have an owner.

Example:

Asset: LAPTOP-203
Owner: John Smith
Department: Finance
Classification: Confidential

This provides:

accountability.

ASSET INVENTORY

An inventory records company assets.

Example:

220 laptops
40 servers
18 switches
320 smartphones
150 applications

Security principle:

You cannot protect assets you do not know exist.

ENUMERATION

Enumeration means systematically discovering resources.

Examples:

hosts
users
services
ports
shares
applications
network devices

Difference:

Inventory = list of known assets.

Enumeration = process used to discover them.

ASSET CLASSIFICATION

Assets may have different levels of sensitivity.

For example:

Public
Internal
Confidential
Restricted

More sensitive assets require stronger protection.

DECOMMISSIONING

When an asset is no longer required, it must be safely removed from service.

You should not simply:

throw a hard drive into the rubbish.

Data may still be recoverable.

SANITIZATION

Sanitization removes data so that it cannot easily be recovered.

Methods include:

secure erase
overwriting
cryptographic erase
CRYPTOGRAPHIC ERASURE

Suppose a disk is encrypted.

Instead of overwriting every byte:

destroy the encryption key.

Without the key, encrypted data becomes unusable.

PHYSICAL DESTRUCTION

Highly sensitive media may be physically destroyed.

Examples:

shredding
crushing
incineration
CERTIFICATE OF DESTRUCTION

A third-party disposal company may provide documentation proving that media was destroyed.

That is:

Certificate of destruction

DATA RETENTION

Retention tells an organization:

How long should we keep information?

Example:

Security logs → 1 year
Financial documents → 7 years
Temporary records → 30 days

Keeping data forever can increase:

storage costs;
legal exposure;
privacy risk;
breach impact.
4.3 — VULNERABILITY MANAGEMENT

Very important domain.

Think:

Discover
↓
Analyse
↓
Prioritize
↓
Remediate
↓
Validate
VULNERABILITY SCANNING

A vulnerability scanner looks for known weaknesses.

Examples:

missing patches
weak configurations
outdated software
open ports
known CVEs
weak TLS
default credentials

Typical tools include:

Nessus;
Qualys;
OpenVAS.
VULNERABILITY SCAN VS PENETRATION TEST

Know this extremely well.

Vulnerability Scan	Penetration Test
Finds vulnerabilities	Attempts to exploit vulnerabilities
Mostly automated	More human/manual
Broad	Deep
Identifies possible weakness	Demonstrates real impact
Usually less intrusive	May affect systems

Memory:

Scanner = "I think there is a door."

Pentester = "I opened the door and got inside."

AUTHENTICATED SCAN

Scanner is given credentials.

It can inspect the system from the inside.

Usually provides:

more accurate and detailed results.

UNAUTHENTICATED SCAN

Scanner behaves more like an external attacker.

It does not have credentials.

Useful for seeing:

what an outsider can discover.

AGENT-BASED SCAN

An agent is installed on the endpoint.

Advantages:

detailed information;
continuous monitoring;
works even when machine is not directly reachable.
AGENTLESS SCAN

Scanner connects remotely.

Advantages:

nothing installed;
easier deployment.

Disadvantage:

potentially less visibility.

PACKAGE MONITORING

Modern applications use third-party libraries.

Example:

Application
 ├── OpenSSL
 ├── Log4j
 ├── lodash
 └── React

Your own code may be safe, but one library could have a vulnerability.

Package/dependency monitoring checks those components.

THREAT INTELLIGENCE FEEDS

Threat feeds provide information about threats.

Examples:

Malicious IP addresses
Malicious domains
File hashes
Known malware
Indicators of compromise
New vulnerabilities
Attack campaigns

Sources can include:

OSINT

Open-source intelligence.

Publicly available information.

Proprietary intelligence

Commercial intelligence produced by security vendors.

Information-sharing organizations

Organizations share threat information with one another.

Dark web sources

May provide information on:

stolen credentials;
leaked databases;
criminal activity.
RESPONSIBLE DISCLOSURE

Researcher discovers a vulnerability.

Instead of immediately publishing it:

researcher informs the company and gives them time to fix it.

That is responsible disclosure.

BUG BOUNTY

Organizations reward researchers for responsibly finding vulnerabilities.

Example:

Find serious vulnerability
↓
Report it
↓
Company validates it
↓
Researcher receives payment/reward
CVE

Common Vulnerabilities and Exposures

CVE is an identifier.

Example:

CVE-2026-12345

Think:

CVE = Which vulnerability?

CVSS

Common Vulnerability Scoring System

Measures vulnerability severity.

Usually from:

0.0 → 10.0

Typical ranges:

0.1–3.9   Low
4.0–6.9   Medium
7.0–8.9   High
9.0–10.0  Critical

Think:

CVSS = How serious?

CVE VS CVSS

Extremely common exam distinction.

CVE → ID
CVSS → severity score
FALSE POSITIVE

Security system says:

THREAT!

But there is no threat.

Alert = YES
Attack = NO

False positive.

FALSE NEGATIVE

Security system says:

Everything is fine.

But there really is an attack.

Alert = NO
Attack = YES

False negative.

Generally more dangerous because:

the attacker remains undetected.

PRIORITIZING VULNERABILITIES

Do not automatically patch only according to CVSS.

Consider:

vulnerability severity;
exposure;
importance of the asset;
business impact;
exploit availability;
threat intelligence;
environmental factors.

Example:

Server A

CVSS = 10

But:

offline
isolated
no important information
Server B

CVSS = 8

But:

Internet-facing
customer database
critical business system

Server B might deserve attention first.

PATCHING

Best solution when available:

install the security patch.

But sometimes you cannot patch immediately.

SEGMENTATION

A vulnerable system can be isolated from other systems.

Example:

Legacy Server
      |
Firewall
      |
Restricted VLAN

This reduces exposure.

COMPENSATING CONTROL

You cannot implement the preferred security control.

So you implement another control to reduce the risk.

Example:

Legacy server cannot be patched.

Use:

network segmentation
firewall rules
strict ACL
monitoring
restricted access

These are compensating controls.

EXCEPTION / EXEMPTION

Sometimes a system cannot comply with a security requirement.

The organization formally approves an exception.

Important:

An exception is NOT simply ignoring security.

It should be:

documented;
justified;
approved;
periodically reviewed.
RESCANNING

After remediation:

scan again.

Why?

To verify the vulnerability has actually disappeared.

This is:

Validation of remediation

4.4 — SECURITY ALERTING AND MONITORING

This section contains several concepts you have already encountered in mock tests.

LOGS

Logs record activity.

Examples:

Authentication logs
successful login
failed login
account lockout
password change
Firewall logs
allowed traffic
blocked traffic
source IP
destination IP
ports
DNS logs
domain queried
computer making query
DNS response
Web server logs
source IP
HTTP request
URL
HTTP status code
timestamp
Application logs

Application-specific activity.

Endpoint logs

Activity from computers/endpoints.

SERVER LOGS VS NETWORK LOGS
Server logs

Come from servers.

Examples:

Windows Event Logs
Linux syslog
Apache logs
IIS logs
database logs
authentication logs
Network logs

Come from networking/security devices.

Examples:

Firewall logs
Router logs
Switch logs
IDS/IPS logs
VPN logs
NetFlow
DNS logs
LOG AGGREGATION

Instead of checking:

Firewall
Server
VPN
DNS
EDR
IDS

separately, send their logs to one place.

Firewall ─┐
Server ───┤
VPN ──────┤
DNS ──────┼──→ SIEM
EDR ──────┤
IDS ──────┘

That is log aggregation.

SIEM

Security Information and Event Management

SIEM:

collects logs
centralizes logs
searches logs
correlates events
detects suspicious patterns
creates alerts

Example:

03:01 Failed login
03:02 Failed login
03:03 Failed login
03:04 Successful login
03:06 10 GB of data uploaded

SIEM correlates the events and may generate:

Possible account compromise.

Memory:

SIEM = SEE what is happening

SOAR

Security Orchestration, Automation, and Response

SOAR automates actions between security tools.

Example:

SIEM alert
↓
SOAR receives alert
↓
Checks threat intelligence
↓
Blocks malicious IP
↓
Isolates endpoint
↓
Creates ticket
↓
Notifies analyst

Memory:

SIEM = detect/correlate

SOAR = automate/respond

SOAR can receive information from detection tools, but its key purpose is:

orchestration + automation + response.

ALERT TUNING

Imagine your SIEM produces:

30,000 alerts every day.

Most are false positives.

Security team adjusts:

thresholds;
rules;
exceptions;
severity;
correlation rules.

That is:

Alert tuning

ALERT FATIGUE

If analysts receive too many alerts:

they may stop taking them seriously.

This is alert fatigue.

Alert tuning helps reduce it.

QUARANTINE

Suspicious file/device is isolated so it cannot spread malware or communicate with other systems.

BENCHMARKS

Security benchmarks provide recommended secure configurations.

A famous example:

CIS Benchmarks.

SCAP

Security Content Automation Protocol

Used to standardize/automate security configuration and vulnerability information.

Think:

automated standardized security assessment.

SNMP

Simple Network Management Protocol

Used to monitor/manage network devices.

Examples:

routers
switches
printers
servers
SNMP TRAP

Normally monitoring software asks a device:

Are you okay?

A trap works differently.

The device itself says:

Something happened!

Example:

Switch interface fails
↓
Switch sends SNMP trap
↓
Monitoring server receives alert
NETFLOW

NetFlow provides metadata about network communication.

Example:

Source IP
Destination IP
Source port
Destination port
Protocol
Bytes transferred
Duration

Think:

Who communicated with whom, when, and how much?

PACKET CAPTURE

Captures actual packets.

Tools such as Wireshark can examine:

packet headers
protocol fields
payloads
network conversations

Difference:

NetFlow

Summary.

Packet capture

Detailed packets.

Memory:

NetFlow = phone bill

Packet capture = phone conversation

4.5 — MODIFY ENTERPRISE CAPABILITIES TO ENHANCE SECURITY
FIREWALL

Firewall applies rules to network traffic.

Example:

ALLOW TCP 443
DENY TCP 23
DENY ALL OTHER INBOUND
ACL — ACCESS CONTROL LIST

An ACL is a list of permit/deny rules.

Example:

permit 192.168.10.0/24 → server port 443
deny any → server port 22

Can exist on:

routers;
switches;
firewalls;
operating systems;
filesystems.
IDS

Intrusion Detection System

Detects suspicious activity.

Action:

alert.

Memory:

IDS = Detect

IPS

Intrusion Prevention System

Detects suspicious activity AND can block it.

Often placed inline.

Memory:

IPS = Prevent

IDS VS IPS
IDS → sees attacker
IPS → sees attacker + stops attacker
SIGNATURE-BASED DETECTION

Looks for known patterns.

Example:

Known malware byte pattern
Known exploit pattern
Known attack signature

Strength:

good at detecting known attacks.

Weakness:

may miss new/modified attacks.

BEHAVIOUR / ANOMALY-BASED DETECTION

Looks for abnormal behaviour.

Example:

Normal employee:

logs in 08:00
downloads 20 MB/day

Suddenly:

logs in 03:00
downloads 80 GB
connects from unknown country

That may be detected as anomalous.

WEB FILTERING

Controls which websites/users can access.

Can filter by:

URL;
reputation;
category;
content;
domain.

Example:

Malware sites → blocked
Gambling → blocked
Corporate websites → allowed
DNS FILTERING

Prevents clients from resolving malicious/unapproved domains.

Example:

malware-example.com
        ↓
DNS filter
        ↓
BLOCKED
DLP

Data Loss Prevention

DLP protects sensitive information from leaving the organization.

Can monitor:

email
USB
cloud uploads
printing
web uploads
file transfers

Example:

Employee tries emailing:

customers-credit-cards.xlsx

to personal Gmail.

DLP:

BLOCK.

Memory:

DLP = Don't Let data Pass

NETWORK ACCESS CONTROL — NAC

NAC decides whether a device should be allowed onto the network.

It may verify:

Is antivirus installed?
Is OS patched?
Is disk encrypted?
Is device company-owned?

Non-compliant device can be placed into:

quarantine network.

EDR

Endpoint Detection and Response

EDR focuses on endpoint security.

Endpoints include:

laptops
desktops
servers

EDR can:

monitor processes;
detect malware;
monitor files;
identify suspicious behaviour;
isolate computers;
kill processes;
collect forensic information.

Memory:

EDR = security focused on ENDPOINTS

XDR

Extended Detection and Response

XDR goes beyond endpoints.

It may combine information from:

EDR
email
cloud
network
identity
firewalls
servers

Memory:

EDR → endpoint
XDR → extended across many systems
FIM

File Integrity Monitoring

FIM detects changes to important files.

It commonly compares:

cryptographic hashes.

Example:

Original:

system32.dll
SHA-256 = ABC123

Later:

SHA-256 = XYZ987

FIM:

FILE CHANGED.

Memory:

FIM = Did this FILE change?

Important:

SOAR may automate responses after an alert.

But if the question specifically says:

Detect unauthorized modifications to critical system files.

Answer:

FIM

HIDS

Host-based Intrusion Detection System

Runs on an individual host.

Monitors:

logs;
files;
processes;
system activity.
NIDS

Network Intrusion Detection System

Monitors network traffic.

Think:

HIDS → Host
NIDS → Network
4.6 — IDENTITY AND ACCESS MANAGEMENT — IAM

This section is huge in Security+.

AAA MODEL

AAA means:

Authentication
Authorization
Accounting
AUTHENTICATION

Question:

Who are you?

Examples:

password
fingerprint
smart card
certificate
security key
AUTHORIZATION

Question:

What are you allowed to do?

Example:

Alice = read files
Bob = modify files
Admin = delete files
ACCOUNTING

Question:

What did you do?

Examples:

login time
logout time
commands executed
resources accessed

Memory:

Authentication → Who?
Authorization → What?
Accounting → What happened?
MFA

Multi-Factor Authentication

Must use two or more DIFFERENT factor types.

Factors:

Something you know
password
PIN
Something you have
smart card
phone
security key
token
Something you are
fingerprint
face
iris

Important:

Password + PIN is NOT true MFA.

Both are:

something you know.

TOTP

Time-based One-Time Password

Usually:

6-digit code
changes every 30 seconds

Example:

Authenticator applications.

HOTP

HMAC-based One-Time Password

Changes based on an event/counter rather than time.

PUSH AUTHENTICATION

User receives notification:

Approve this login?

Risk:

MFA fatigue / push bombing.

Attacker repeatedly sends prompts hoping user presses Accept.

PASSWORDLESS AUTHENTICATION

Can use:

FIDO2;
hardware security keys;
biometrics;
certificates.

Reduces dependence on passwords.

SSO

Single Sign-On

Authenticate once and access multiple systems.

Example:

Login once
↓
Email
HR system
Cloud storage
CRM

Advantages:

convenience;
fewer passwords.

Risk:

one compromised account may provide access to many systems.

LDAP

Lightweight Directory Access Protocol

LDAP is used to communicate with directory services.

Example:

Active Directory directory information.

Can query:

users
groups
computers
organizational units

Think:

LDAP = access/query a directory

SAML

Security Assertion Markup Language

Used mainly for federated authentication and SSO.

Common web scenario:

User
↓
Service Provider
↓
Identity Provider
↓
SAML assertion
↓
Access

Think:

SAML = web SSO / federation

SAML VS LDAP

Very important distinction.

LDAP

Talks to directory services.

SAML

Transfers authentication information between organizations/web services.

Memory:

LDAP → directory
SAML → SSO federation
OAUTH

OAuth focuses on:

delegated authorization.

Example:

An application asks:

Allow this app to access your Google Calendar?

You do not give the app your Google password.

OAuth provides limited delegated access.

Memory:

OAuth = authorization

OPENID CONNECT

Built on OAuth 2.0.

Adds:

authentication / identity.

Simplified:

OAuth → authorization
OIDC → authentication + identity
PROVISIONING

Creating user accounts/access.

Example:

New employee joins.

Create AD account
Create email
Assign groups
Give applications
Issue laptop
DEPROVISIONING

Employee leaves.

Remove:

accounts
tokens
VPN access
badges
application access
admin privileges

This should happen quickly.

PRIVILEGED ACCESS MANAGEMENT — PAM

Controls accounts with powerful permissions.

Examples:

domain administrator
root
database administrator
cloud administrator

PAM can provide:

credential vaulting;
temporary privileges;
session recording;
approval workflows.
JUST-IN-TIME PERMISSIONS

Instead of giving permanent admin rights:

give privilege only when required.

Example:

Developer needs admin for 1 hour
↓
Approved
↓
Admin rights activated
↓
1 hour later
↓
Rights removed

This reduces risk.

LEAST PRIVILEGE

Give users:

only the permissions necessary to perform their job.

ROLE-BASED ACCESS CONTROL — RBAC

Permissions depend on job role.

Example:

HR role → employee records
Finance role → accounting system
IT Admin → administration tools
RULE-BASED ACCESS CONTROL

Access is based on rules.

Example:

Allow access only:
Monday-Friday
08:00-18:00
Corporate network only
ATTRIBUTE-BASED ACCESS CONTROL — ABAC

Uses attributes.

Examples:

user.department = Finance
device.compliant = true
location = Portugal
data.classification = confidential

Decision uses several attributes.

MANDATORY ACCESS CONTROL — MAC

Access is based on centrally defined security labels.

Example:

Top Secret
Secret
Confidential

User cannot decide permissions themselves.

Often associated with government/military environments.

DISCRETIONARY ACCESS CONTROL — DAC

Resource owner can decide who gets access.

Example:

You own a file and choose:

John = read
Mary = edit
4.7 — AUTOMATION AND ORCHESTRATION
AUTOMATION

A computer automatically performs a task.

Example:

Malware detected
↓
Automatically isolate endpoint
ORCHESTRATION

Coordinates multiple automated systems.

Example:

SIEM detects attack
↓
SOAR checks threat intelligence
↓
Firewall blocks IP
↓
EDR isolates computer
↓
Ticket created
↓
SOC notified

That coordination is orchestration.

PLAYBOOK

A predefined sequence of actions.

Example:

Phishing Playbook

1. Examine email
2. Extract URLs
3. Check reputation
4. Search other mailboxes
5. Delete malicious copies
6. Reset affected credentials
RUNBOOK

A detailed operational procedure explaining how to perform a task.

Simplified distinction:

Playbook = response strategy/workflow

Runbook = detailed operational instructions

Security+ sometimes uses the terms somewhat closely, so focus on context.

BENEFITS OF AUTOMATION
faster response;
fewer manual mistakes;
consistent actions;
scalable security;
reduced workload.
RISKS OF AUTOMATION

Bad automation can create problems extremely quickly.

Example:

Incorrect detection rule:

Google.com classified malicious
↓
SOAR automatically blocks it
↓
Entire organization loses access

Therefore automation requires:

testing;
monitoring;
approvals;
safeguards.
4.8 — INCIDENT RESPONSE

One of the most important sections.

A common incident response lifecycle:

Preparation
↓
Detection / Analysis
↓
Containment
↓
Eradication
↓
Recovery
↓
Lessons Learned
PREPARATION

Before an attack happens:

create incident response plan;
define teams;
establish communication;
prepare tools;
perform training;
maintain backups;
create playbooks.
DETECTION / ANALYSIS

Determine:

what happened;
which systems are affected;
how serious it is;
whether it is a real incident.

Sources:

SIEM
EDR
logs
IDS
users
threat intelligence
CONTAINMENT

Goal:

Stop the attack from spreading.

Examples:

isolate infected PC
disable account
block IP
disconnect server
segment network

Important:

Containment does NOT necessarily remove the malware.

It limits damage.

ERADICATION

Remove the cause.

Examples:

delete malware
remove persistence
patch vulnerability
disable malicious accounts
remove unauthorized software
RECOVERY

Return systems safely to normal operation.

Examples:

restore backups
rebuild systems
reconnect computers
monitor environment
LESSONS LEARNED

After the incident:

Ask:

What happened?
Why did it happen?
What worked?
What failed?
How can we prevent it?

Then improve:

policies;
controls;
procedures;
training.
ROOT CAUSE ANALYSIS

Find the underlying reason the incident occurred.

Example:

Malware infected laptop
↓
Why?
User opened malicious attachment
↓
Why did attachment reach user?
Email filter failed
↓
Why did malware execute?
Macros were permitted

Finding the root cause prevents recurrence.

INCIDENT RESPONSE PLAN

Defines how organization responds to security incidents.

Should include:

roles;
responsibilities;
communication;
escalation;
procedures;
reporting;
recovery.
BUSINESS CONTINUITY PLAN

Different concept.

Incident response:

How do we deal with the security incident?

Business continuity:

How do we keep the business operating?

DISASTER RECOVERY

Focuses on:

restoring IT systems and data after a disaster.

TABLETOP EXERCISE

People discuss how they would respond to an imaginary incident.

Example:

“Our ransomware attack begins at 10:00. What do you do?”

No actual systems need to be attacked.

Cheap and useful.

SIMULATION

More realistic exercise involving simulated technical activity.

4.9 — DATA SOURCES FOR INVESTIGATION

This is the forensic/log analysis part.

FIREWALL LOGS

Useful for seeing:

source IP
destination IP
ports
allowed connections
blocked connections
APPLICATION LOGS

Show events inside applications.

Examples:

failed authentication
application error
admin change
data access
ENDPOINT LOGS

Show events on computers.

Examples:

process execution
malware alerts
file changes
logins
USB devices
OS-SPECIFIC LOGS

Windows:

Event Viewer / Windows Event Logs

Linux:

syslog/journal logs

IDS/IPS LOGS

Can show:

attack signatures
source IP
destination
attack type
blocked/detected activity
NETWORK LOGS

Examples:

Router
Switch
Firewall
VPN
DNS
DHCP
NetFlow
METADATA

Metadata means:

data about data.

Example for a file:

Creation date
Modification date
Author
File size
Location

Example email metadata:

Sender
Recipient
Mail servers
Timestamps
Message ID
DIGITAL FORENSICS

Goal:

collect and analyse digital evidence.

ORDER OF VOLATILITY

Collect the most temporary information first.

For example:

CPU/cache
RAM
network connections
running processes
disk
backups

Why?

Because RAM disappears when power is removed.

FORENSIC IMAGE

A bit-for-bit copy of storage media.

Investigators normally analyse:

the forensic copy,

not the original drive.

HASHING

Before/after collecting evidence:

calculate hash

Example:

SHA-256 Original = ABC
SHA-256 Copy = ABC

Same hash supports evidence integrity.

CHAIN OF CUSTODY

Documents:

Who collected evidence?
When?
Where?
Who handled it?
Where was it stored?
Who transferred it?

Purpose:

prove evidence was properly controlled and not altered.

Very important for legal cases.