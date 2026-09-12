## 3.1 — Security Implications of Different Architecture Models

The official objectives include cloud, IaC, serverless, microservices, segmentation, SDN, on-premises, containers, virtualization, IoT, ICS/SCADA, RTOS, embedded systems, and high availability.

## Cloud Computing

Cloud computing means using computing resources provided remotely by a cloud provider.

Examples:

- Servers
- Storage
- Databases
- Applications
- Networking

Instead of buying all the hardware yourself:

Company
↓
Internet
↓
Cloud provider

Examples of cloud providers:

- AWS
- Microsoft Azure
- Google Cloud

## Shared Responsibility Model

This is extremely important.

When using cloud services:

- The cloud provider is responsible for some security.
- The customer is still responsible for other security.
- The responsibility changes depending on the service model.

### IaaS — Infrastructure as a Service

The cloud provider manages the physical infrastructure.

You manage much more of the software environment.

Example:

Cloud provider:

- Physical servers
- Storage
- Networking
- Virtualization

Customer:

- Operating system
- Applications
- Configurations
- Accounts
- Data

Examples include virtual machines in AWS/Azure.

Memory: IaaS gives you the most control — and more responsibility.

### PaaS — Platform as a Service

The provider manages more of the stack.

You mainly manage:

- Applications
- Data
- Users

The provider manages things such as:

- Operating system
- Runtime
- Infrastructure

Memory: PaaS = I build my app, provider manages the platform.

### SaaS — Software as a Service

The provider manages almost everything.

You simply use the application.

Examples:

- Microsoft 365
- Google Workspace
- Salesforce

But you are still normally responsible for things such as:

- User accounts
- Permissions
- MFA
- Data
- Configuration

Important exam point: moving something to the cloud does not remove your security responsibilities.

### Cloud Responsibility Memory

Think:

- IaaS → customer manages MOST
- PaaS → customer manages LESS
- SaaS → customer manages LEAST

But the customer normally still has responsibility for:

- Identity
- Access
- Data
- Configuration

## Hybrid Cloud

A hybrid environment combines:

- On-premises infrastructure
- Cloud infrastructure

Example:

- Company database → local data centre
- Web applications → Azure
- Backups → AWS

Benefits:

- Flexibility
- Gradual migration
- Keep sensitive resources locally

Problems:

- More complex security
- Identity synchronization
- Multiple networks
- Monitoring becomes harder
- More possible misconfigurations

## Third-Party Vendors

Using cloud means depending on another organization.

This introduces third-party risk.

Questions include:

- Can the provider secure our information?
- Where is our data stored?
- What happens if the provider goes offline?
- What happens if the provider is breached?

Remember: outsourcing a service does not mean outsourcing all responsibility.

## Infrastructure as Code (IaC)

IaC means infrastructure is created and configured using code rather than manually.

Instead of manually creating 50 servers:

- Administrator clicks Create VM
- Configure firewall
- Configure storage
- ...

You define it in a configuration.

Conceptually:

```text
server_count = 50
OS = Linux
firewall_port = 443
encryption = enabled
```

Then automation builds it.

Examples of IaC technologies include:

- Terraform
- CloudFormation
- Ansible

## Security Benefits of IaC

IaC provides:

- Consistency
- Repeatability
- Version control
- Automation

Every deployment follows the same configuration.

Can rebuild environments quickly.

Changes can be tracked.

Less manual configuration.

But there is a major risk: a bad configuration can also be automatically deployed everywhere.

Example:

Firewall rule accidentally says: ALLOW ANY → database.

IaC deploys it to 100 servers.

Automation makes good configuration faster, but automation also makes mistakes faster.

## Serverless Computing

Serverless does not mean there are no servers; servers still exist.

It means the customer does not manage them directly.

Example:

User request
↓
Cloud function executes
↓
Function finishes

Examples:

- AWS Lambda
- Azure Functions
- Google Cloud Functions

Benefits:

- Easy scaling
- Less infrastructure management
- Pay for execution
- Quick deployment

Security concerns:

- Insecure functions
- Excessive permissions
- Vulnerable dependencies
- Cloud misconfiguration
- Third-party risk

Memory: Serverless = provider manages the server infrastructure.

## Microservices

Traditional application: one giant application, often called a monolithic architecture.

Microservices split it into smaller independent services.

Example:

- Authentication Service
- Payment Service
- Inventory Service
- Shipping Service
- Customer Service

Benefits:

- Easier scaling
- Individual components can be updated independently
- Failures may be isolated

Security problems:

Many services communicate with each other, which means more:

- APIs
- Authentication
- Network connections
- Credentials
- Certificates

Therefore, there is a larger potential attack surface.

## Physical Isolation

Physical isolation means systems are separated physically.

The strongest example is an air-gapped network.

An air-gapped network has no normal connection to another network such as the Internet.

Example:

Internet

X

Secure military network

Advantages:

- Extremely difficult for remote attackers to reach

Problems:

- Difficult updates
- Difficult administration
- USB/removable devices may still introduce malware
- Expensive

Exam clue: “System must have maximum isolation from external networks.”

Think: air gap.

## Logical Segmentation

Logical segmentation separates systems using networking technologies rather than physically separate cables or equipment.

Examples:

- VLANs
- Subnets
- Firewall rules
- ACLs

Example:

- VLAN 10 → Employees
- VLAN 20 → Servers
- VLAN 30 → Guests
- VLAN 40 → IoT

Why?

If an attacker compromises the guest network, they should not automatically reach internal servers.

## Segmentation

Segmentation reduces lateral movement.

Lateral movement means:

Attacker compromises Computer A
↓
Moves to Computer B
↓
Moves to Server C
↓
Moves to Domain Controller

Segmentation creates barriers.

## Microsegmentation

Microsegmentation makes segmentation even more granular.

Instead of:

- Users network
- Servers network

You might have:

- Web Server → can only contact App Server
- App Server → can only contact Database
- Database → accepts only specific traffic

Very useful in Zero Trust environments.

## SDN — Software-Defined Networking

Traditional networking:

- Configure Router A
- Configure Router B
- Configure Switch A
- Configure Switch B

SDN separates the control plane from the data plane.

### Control Plane

Makes decisions. Example: where should this network traffic go?

### Data Plane

Actually forwards packets.

With SDN:

Central SDN Controller
↓
Switches
Routers
Network devices

Instead of manually configuring every device, software centrally manages the network.

Memory: SDN = centrally programmable networking.

## On-Premises

Infrastructure is physically located and controlled by the organization.

Example:

- Company building
- Server room
- Switches
- Storage
- Firewalls
- Servers

Advantages:

- Greater control
- Physical control
- Customization

Disadvantages:

- Expensive
- Organization handles hardware
- Organization handles maintenance
- Organization handles power/cooling
- Organization handles physical security

## Cloud vs On-Premises

| Cloud | On-premises |
|---|---|
| Provider owns much infrastructure | Company owns infrastructure |
| Easy scaling | Scaling requires hardware |
| Operational expense | Higher capital expense |
| Shared responsibility | Organization responsible for almost everything |
| Fast deployment | Usually slower |
| Third-party dependency | Greater direct control |

## Centralized vs Decentralized

### Centralized

Control and resources are concentrated in one place.

Example:

- Central authentication server
- Central SIEM
- Central management console

Advantages:

- Easier administration
- Consistent policies
- Easier monitoring

Problem: a central resource can become a single point of failure.

### Decentralized

Control and resources are distributed.

Advantages:

- More resilience
- Fewer single points of failure

Problems:

- Harder management
- Inconsistent configurations
- Harder monitoring

## Virtualization

Virtualization allows multiple virtual computers to share physical hardware.

Example:

Physical Server
↓
Hypervisor
├── VM1
├── VM2
└── VM3

### Hypervisor

The hypervisor manages virtual machines.

Two broad types:

#### Type 1

Runs directly on hardware.

Hardware
↓
Hypervisor
↓
VMs

Often used in data centres.

#### Type 2

Runs on top of an operating system.

Hardware
↓
Host OS
↓
Hypervisor
↓
VM

## Virtualization Security Risks

One major concept: VM escape.

An attacker escapes from a virtual machine and reaches the hypervisor or other VMs. That defeats isolation.

Another issue: resource reuse.

Sensitive information left in shared resources may become accessible.

## Containers

Containers isolate applications but usually share the host operating system kernel.

Conceptually:

Host OS
↓
Container Engine
├── Container A
├── Container B
└── Container C

Examples:

- Docker
- Kubernetes environments

## VM vs Container

### Virtual machine

Each VM has its own operating system.

### Container

Containers generally share the host OS kernel.

Therefore containers are usually:

- Smaller
- Faster
- More efficient

But isolation can be weaker than fully separate VMs.

Memory: VM virtualizes a computer; container isolates an application.

## IoT — Internet of Things

IoT devices include:

- Smart cameras
- Smart TVs
- Thermostats
- Smart locks
- Sensors
- Medical devices
- Smart appliances

Security problems:

- Default passwords
- Weak firmware
- Poor patch support
- Long lifespans
- Insecure protocols
- Limited computing resources

Best approach often includes:

- Network segmentation
- Change default passwords
- Patch firmware
- Disable unnecessary services
- Monitor traffic

## Embedded Systems

An embedded system performs a dedicated function inside another device.

Examples:

- Car control system
- Printer
- Medical device
- Industrial machinery
- Smart appliance

They often have:

- Limited resources
- Long lifecycle
- Difficulty patching

## RTOS — Real-Time Operating System

A real-time operating system is designed to respond within predictable timing constraints.

Examples:

- Airbag system
- Medical equipment
- Industrial robot
- Aircraft control

The important thing is response must happen at the correct time.

Security challenge: availability and timing may be more important than installing the latest patch immediately.

## ICS — Industrial Control System

ICS controls industrial equipment.

Examples:

- Manufacturing
- Power plants
- Water treatment
- Factories
- Oil pipelines

### SCADA

Supervisory Control and Data Acquisition.

SCADA is used to monitor and control industrial processes across potentially large geographic areas.

Conceptually:

Control Center
↓
Network
↓
PLC / Industrial Devices
↓
Physical equipment

Examples:

- Water systems
- Electrical grid
- Pipelines

## ICS/SCADA Security

Traditional IT priority might be:

- Confidentiality
- Integrity
- Availability

In industrial systems, availability and safety can be the highest priorities.

You cannot casually reboot a power plant.

Another issue: some industrial systems are decades old. Therefore:

- Patching may be difficult
- Legacy protocols may exist
- Systems may need segmentation

## High Availability

High availability means designing systems to continue operating even if something fails.

Example:

Server A fails
↓
Server B continues service

The goal is to minimize downtime.

## Architecture Considerations

CompTIA specifically expects you to consider factors such as:

- Availability
- Resilience
- Cost
- Scalability
- Recovery
- Patching
- Power
- Computing resources

lateral movement

Lateral movement means:

Attacker compromises Computer A
↓
Moves to Computer B
↓
Moves to Server C
↓
Moves to Domain Controller

Segmentation creates barriers.

MICROSEGMENTATION

Microsegmentation makes segmentation even more granular.

Instead of:

Users network
Servers network

you might have:

Web Server → can only contact App Server

App Server → can only contact Database

Database → accepts only specific traffic

Very useful in:

Zero Trust environments.

SDN — SOFTWARE-DEFINED NETWORKING

You have asked about this before.

Traditional networking:

Configure Router A
Configure Router B
Configure Switch A
Configure Switch B

SDN separates:

control plane

from:

data plane

CONTROL PLANE

Makes decisions.

Example:

Where should this network traffic go?

DATA PLANE

Actually forwards packets.

With SDN:

Central SDN Controller
      ↓
Switches
Routers
Network devices

Instead of manually configuring every device:

software centrally manages the network.

Memory:

SDN = centrally programmable networking

ON-PREMISES

Infrastructure physically located and controlled by the organization.

Example:

Company building

Server room
Switches
Storage
Firewalls
Servers

Advantages:

greater control;
physical control;
customization.

Disadvantages:

expensive;
organization handles hardware;
organization handles maintenance;
organization handles power/cooling;
organization handles physical security.
CLOUD VS ON-PREMISES
Cloud	On-premises
Provider owns much infrastructure	Company owns infrastructure
Easy scaling	Scaling requires hardware
Operational expense	Higher capital expense
Shared responsibility	Organization responsible for almost everything
Fast deployment	Usually slower
Third-party dependency	Greater direct control
CENTRALIZED VS DECENTRALIZED
Centralized

Control/resources are concentrated in one place.

Example:

Central authentication server
Central SIEM
Central management console

Advantages:

easier administration;
consistent policies;
easier monitoring.

Problem:

central resource can become a single point of failure.

Decentralized

Control/resources are distributed.

Advantages:

more resilience;
fewer single points of failure.

Problems:

harder management;
inconsistent configurations;
harder monitoring.
VIRTUALIZATION

Virtualization allows multiple virtual computers to share physical hardware.

Example:

Physical Server
     |
Hypervisor
 ┌───┼───┐
VM1 VM2 VM3
HYPERVISOR

The hypervisor manages virtual machines.

Two broad types:

Type 1

Runs directly on hardware.

Hardware
↓
Hypervisor
↓
VMs

Often used in data centres.

Type 2

Runs on top of an operating system.

Hardware
↓
Host OS
↓
Hypervisor
↓
VM
VIRTUALIZATION SECURITY RISKS

One major concept:

VM escape

Attacker escapes from a virtual machine and reaches:

hypervisor
or
other VMs

That defeats isolation.

Another issue:

resource reuse.

Sensitive information left in shared resources may become accessible.

CONTAINERS

Containers isolate applications but usually share the host operating system kernel.

Conceptually:

Host OS
   |
Container Engine
 ├ Container A
 ├ Container B
 └ Container C

Examples:

Docker
Kubernetes environments
VM VS CONTAINER

Very important.

Virtual machine

Each VM has:

its own operating system.

Container

Containers generally:

share the host OS kernel.

Therefore containers are usually:

smaller;
faster;
more efficient.

But isolation can be weaker than fully separate VMs.

Memory:

VM virtualizes a computer.

Container isolates an application.

IoT — INTERNET OF THINGS

IoT devices include:

smart cameras
smart TVs
thermostats
smart locks
sensors
medical devices
smart appliances

Security problems:

default passwords;
weak firmware;
poor patch support;
long lifespans;
insecure protocols;
limited computing resources.

Best approach often includes:

network segmentation
change default passwords
patch firmware
disable unnecessary services
monitor traffic
EMBEDDED SYSTEMS

An embedded system performs a dedicated function inside another device.

Examples:

car control system
printer
medical device
industrial machinery
smart appliance

They often have:

limited resources;
long lifecycle;
difficulty patching.
RTOS — REAL-TIME OPERATING SYSTEM

A Real-Time Operating System is designed to respond within predictable timing constraints.

Example:

Airbag system
Medical equipment
Industrial robot
Aircraft control

The important thing is:

Response must happen at the correct time.

Security challenge:

Availability and timing may be more important than installing the latest patch immediately.

ICS — INDUSTRIAL CONTROL SYSTEM

ICS controls industrial equipment.

Examples:

manufacturing
power plants
water treatment
factories
oil pipelines
SCADA

Supervisory Control and Data Acquisition

SCADA is used to monitor/control industrial processes across potentially large geographic areas.

Conceptually:

Control Center
     ↓
Network
     ↓
PLC / Industrial Devices
     ↓
Physical equipment

Examples:

water systems;
electrical grid;
pipelines.
ICS/SCADA SECURITY

Traditional IT priority might be:

Confidentiality
Integrity
Availability

In industrial systems:

Availability and safety can be the highest priorities.

You cannot casually reboot:

a power plant.

Another issue:

Some industrial systems are decades old.

Therefore:

patching may be difficult
legacy protocols may exist
systems may need segmentation
HIGH AVAILABILITY

High availability means designing systems to:

continue operating even if something fails.

Example:

Server A fails
↓
Server B continues service

The goal:

minimize downtime.

ARCHITECTURE CONSIDERATIONS

CompTIA specifically expects you to consider factors such as availability, resilience, cost, scalability, recovery, patching, power and computing resources.

AVAILABILITY

Can users access the system when needed?

Example:

99.9% uptime
99.99% uptime
RESILIENCE

Can the system:

survive a problem and continue/recover?

Availability is about:

staying accessible.

Resilience is broader:

withstand + recover from disruption.

SCALABILITY

Can the system grow?

Example:

Website currently supports:

1,000 users

Tomorrow it needs:

1,000,000 users

Cloud environments are often particularly scalable.

PATCH AVAILABILITY / INABILITY TO PATCH

Some systems cannot easily be patched.

Examples:

medical devices
industrial systems
legacy systems
embedded devices

If patching is impossible:

use compensating controls.

Examples:

segmentation
firewall restrictions
monitoring
isolation
3.2 — SECURE ENTERPRISE INFRASTRUCTURE

This is one of the most testable parts of Domain 3. It includes security zones, fail-open/fail-closed, appliances, 802.1X/EAP, WAF/UTM/NGFW, VPN, TLS, IPSec, SD-WAN and SASE.

SECURITY ZONES

Do not put everything in one network.

Example:

Internet
   |
Firewall
   |
DMZ
   |
Firewall
   |
Internal Network
   |
Critical Servers

Each zone has different trust levels.

DMZ / SCREENED SUBNET

A DMZ contains Internet-facing systems.

Example:

Internet
   |
Firewall
   |
DMZ
 ├ Web Server
 └ Mail Server
   |
Firewall
   |
Internal LAN

Why?

If attacker compromises web server:

attacker still has another security barrier before the internal network.

ATTACK SURFACE

Attack surface means:

all possible places an attacker could attack.

Examples:

open ports
applications
APIs
users
Wi-Fi
websites
services
cloud interfaces

Goal:

reduce attack surface.

Example:

20 unnecessary services
↓
disable 17
↓
smaller attack surface
FAIL-OPEN VS FAIL-CLOSED

This is very exam-worthy.

Imagine a security device fails.

What happens?

FAIL-OPEN

If the security device fails:

traffic/access continues.

Example:

Security device fails
↓
Door unlocks

Advantage:

availability.

Disadvantage:

weaker security.

Think:

Fail-open prioritizes availability.

FAIL-CLOSED

Security device fails:

access stops.

Example:

Security device fails
↓
Door remains locked

Advantage:

security.

Disadvantage:

availability may be affected.

Think:

Fail-closed prioritizes security.

SECURITY+ SCENARIO

Hospital life-support network:

availability might be extremely important.

Could choose fail-open depending on architecture.

High-security vault:

fail-closed likely makes more sense.

The answer depends on:

business requirement.

ACTIVE VS PASSIVE
Passive device

Observes traffic but does not directly modify it.

Example:

IDS.

Active device

Can directly interact with/block traffic.

Example:

IPS.

INLINE VS TAP/MONITOR
Inline

Traffic physically passes through device.

Internet
↓
IPS
↓
Server

Because traffic passes through it:

it can block traffic.

TAP/MONITOR

Device receives a copy of traffic.

Traffic
   ↓
Switch ───→ IDS
   ↓
Server

IDS sees traffic but does not normally directly block it.

Memory:

Inline = in the road.

Tap = watching the road.

JUMP SERVER

A jump server is a controlled system used to access sensitive systems.

Example:

Administrator
    ↓
Jump Server
    ↓
Critical Database

Instead of letting administrators connect directly to critical servers.

Benefits:

centralized control;
auditing;
limited entry point;
stronger authentication.

Memory:

Jump server = secure stepping stone.

PROXY SERVER

A proxy sits between client and destination.

User
↓
Proxy
↓
Internet

The website sees:

proxy address,

rather than necessarily the user's direct connection.

Can provide:

filtering
logging
caching
access control
privacy
FORWARD PROXY

Represents:

clients.

Internal Users
↓
Forward Proxy
↓
Internet
REVERSE PROXY

Represents:

servers.

Internet
↓
Reverse Proxy
↓
Web Servers

Can:

hide internal servers;
perform TLS termination;
filter requests;
balance traffic.
IDS VS IPS

We covered this before, but it appears here too.

IDS
Detect
Alert

Usually passive.

IPS
Detect
Block

Usually inline.

Memory:

IDS sees. IPS stops.

LOAD BALANCER

Distributes traffic among multiple servers.

Users
   ↓
Load Balancer
 ┌───┼───┐
Web1 Web2 Web3

Benefits:

performance;
scalability;
availability.

If one server fails:

Web2 DOWN

load balancer sends traffic to:

Web1 + Web3
802.1X

Provides:

port-based network access control.

User/device must authenticate before receiving network access.

Architecture:

Supplicant
↓
Authenticator
↓
Authentication Server

Example:

Laptop
↓
Switch
↓
RADIUS Server
EAP

Extensible Authentication Protocol

EAP is an authentication framework commonly used with:

802.1X
Wi-Fi Enterprise

EAP itself supports multiple authentication methods.

Examples include:

EAP-TLS
PEAP

Security+ memory:

802.1X controls network access.

EAP carries authentication methods.

RADIUS commonly validates credentials.

WAF — WEB APPLICATION FIREWALL

WAF protects:

web applications.

It operates mainly at:

Layer 7.

It can detect/block attacks such as:

SQL injection
XSS
malicious HTTP requests

Example:

Internet
↓
WAF
↓
Website

Memory:

WAF = protects websites/web apps.

NORMAL FIREWALL VS WAF

Normal firewall may look at:

IP addresses
ports
protocols
connections

WAF looks more deeply at:

HTTP/HTTPS web requests

If question says:

“Protect the website from SQL injection”

Answer:

WAF

UTM — UNIFIED THREAT MANAGEMENT

UTM combines multiple security functions into one appliance.

May include:

Firewall
IDS/IPS
Antivirus
Content filtering
VPN
Web filtering

Memory:

UTM = security Swiss Army knife.

NGFW — NEXT-GENERATION FIREWALL

A traditional firewall might make decisions using:

IP
port
protocol

An NGFW can also understand:

applications
users
content
threats

For example:

Traditional firewall:

ALLOW TCP 443

NGFW:

ALLOW Microsoft Teams

BLOCK BitTorrent

BLOCK known malware
LAYER 4 VS LAYER 7 FIREWALL
Layer 4

Uses transport/network information such as:

IP
TCP
UDP
Port

Example:

Allow TCP 443
Layer 7

Understands application-level information.

Example:

HTTP
DNS
SMTP
specific applications

Can make more intelligent decisions.

VPN

Virtual Private Network

Creates a secure encrypted connection across an untrusted network.

Example:

Remote employee
↓
Internet
↓
Encrypted VPN tunnel
↓
Company
SITE-TO-SITE VPN

Connects two networks.

Office Portugal
      ║
 encrypted tunnel
      ║
Office Germany
REMOTE-ACCESS VPN

Connects:

individual user → company network.

Employee laptop
↓
VPN
↓
Corporate network
TUNNELING

Tunneling means encapsulating one type of traffic inside another.

VPNs commonly use tunneling to transport protected communications.

TLS

Transport Layer Security

TLS protects communications.

Provides:

encryption
integrity
authentication

Most obvious example:

HTTPS.

HTTP + TLS = HTTPS
IPSEC

Internet Protocol Security

Protects traffic at the IP/network layer.

Often used in:

VPNs.

Two important concepts:

AH

Authentication Header.

Provides integrity/authentication.

Does NOT provide confidentiality.

ESP

Encapsulating Security Payload.

Can provide:

confidentiality
integrity
authentication

For Security+:

ESP is generally the more important one to recognize.

IPSEC TRANSPORT MODE

Protects mainly:

the payload.

Original IP header remains.

Typically:

host ↔ host
IPSEC TUNNEL MODE

Protects the original entire packet by encapsulating it inside a new packet.

Common:

network ↔ network

such as site-to-site VPN.

Memory:

Tunnel mode = original packet goes inside another packet.

TLS VS IPSEC
TLS

Usually protects:

specific applications/connections.

Example:

HTTPS
IPSec

Protects:

IP network traffic.

Often:

VPN
SD-WAN

Software-Defined Wide Area Networking

Uses software-based centralized management for WAN connections.

Can intelligently choose between:

MPLS
Internet
5G
broadband

based on:

performance
cost
availability
policy

Think:

SD-WAN = smart software-controlled WAN.

SASE

Secure Access Service Edge

This sounds complicated, but the concept is simple.

SASE combines:

networking + cloud-delivered security.

Instead of forcing all users back to the company data centre:

Remote User
↓
SASE cloud service
↓
Internet / SaaS / company

SASE may combine technologies such as:

SD-WAN
secure web gateway
firewall-as-a-service
Zero Trust access
cloud security

Memory:

SASE = networking + security delivered from the cloud/edge.

3.3 — PROTECTING DATA

CompTIA expects you to understand data types/classifications, data at rest/in transit/in use, sovereignty, geolocation, encryption, hashing, masking, tokenization, obfuscation, segmentation and permission restrictions.

DATA TYPES

Different information requires different protection.

REGULATED DATA

Data protected by law/regulation.

Examples:

personal data
health information
payment card data

Organizations may have legal requirements for how this data is:

stored
processed
transmitted
deleted
TRADE SECRET

Confidential information that gives a company competitive value.

Examples:

secret manufacturing process
recipe
algorithm
business method

If competitors obtain it:

company may lose competitive advantage.

INTELLECTUAL PROPERTY

Includes things such as:

software
designs
inventions
copyrighted works
patents
trade secrets
LEGAL INFORMATION

Examples:

contracts
lawsuit documents
legal correspondence
evidence

May require strict access controls.

FINANCIAL INFORMATION

Examples:

banking records
accounting information
credit card information
financial forecasts
HUMAN-READABLE DATA

Data easily understood by a person.

Example:

Customer Name: John Smith
Password: hello123
NON-HUMAN-READABLE DATA

Requires software/system interpretation.

Examples:

binary files
encrypted information
machine-formatted data
DATA CLASSIFICATION

Classification tells us:

how sensitive the information is.

CompTIA lists classifications such as public, private, confidential, sensitive, restricted and critical.

Exact labels vary between organizations.

Typical idea:

Public
↓
Internal/Private
↓
Sensitive
↓
Confidential
↓
Restricted/Critical

As sensitivity increases:

security controls become stronger.

PUBLIC

Anyone may access.

Example:

public company website
marketing material
PRIVATE / INTERNAL

Not intended for public distribution.

Example:

internal employee directory
internal procedures
CONFIDENTIAL

Unauthorized disclosure could cause significant damage.

Example:

customer records
business plans
employee information
RESTRICTED

Very sensitive.

Access should be extremely limited.

Example:

encryption keys
high-level financial data
classified research
CRITICAL

Information essential to the organization's operation.

Loss/corruption could seriously affect business.

THREE DATA STATES

You must know these instantly:

At rest
In transit
In use
DATA AT REST

Stored somewhere.

Examples:

SSD
hard drive
database
USB
backup
cloud storage

Best-known protection:

encryption at rest

Example:

BitLocker
database encryption
encrypted backup
DATA IN TRANSIT

Moving across a network.

Examples:

web traffic
email
VPN
file transfer

Protection:

TLS
VPN
IPSec
SSH
DATA IN USE

Data currently being processed.

Example:

decrypted information in RAM
database query being processed
application using information

This is often the hardest state to protect because:

the system needs to access the data.

EASY MEMORY
AT REST → stored

IN TRANSIT → moving

IN USE → being processed
DATA SOVEREIGNTY

Data sovereignty means:

data is subject to the laws of the country/jurisdiction where it is located.

Example:

European customer information
↓
stored on server in another country

Legal requirements may change because of location.

GEOLOCATION / GEOGRAPHIC RESTRICTIONS

Organizations may restrict:

where information is stored
where users may access information
where cloud systems operate

Example:

EU data must remain in approved European regions.

ENCRYPTION

Encryption protects:

confidentiality.

Plaintext:

HELLO

Encryption:

x9F82A7...

Someone without the key should not be able to understand it.

HASHING

Hashing is different from encryption.

Hashing:

Input
↓
Hash function
↓
Fixed-length digest

Example:

Password123
↓
SHA-256
↓
ef92b778...

Hashing is:

one-way.

You normally do not decrypt a hash.

Uses:

password verification
file integrity
digital signatures
forensics

Memory:

Encryption → confidentiality

Hash → integrity

DATA MASKING

Displays altered/hidden values instead of real information.

Example:

Real card:

4532 9845 1234 5678

Masked:

**** **** **** 5678

Used when users/applications need:

some information,

but not the entire sensitive value.

TOKENIZATION

Sensitive information is replaced with a non-sensitive token.

Example:

Credit card:
4532984512345678

Token:
TKN-839271

A separate secure system maps:

TKN-839271
→
4532984512345678

Very common in:

payment systems.

MASKING VS TOKENIZATION
Masking

Changes how information appears.

**** **** **** 5678
Tokenization

Replaces original information with another value.

TKN-928372
OBFUSCATION

Makes information/code intentionally difficult to understand.

Example:

Readable code:

password = getPassword()

Obfuscated code:

a7x9 = q3()

Purpose:

make reverse engineering more difficult.

Important:

Obfuscation is NOT the same as encryption.

SEGMENTATION AS DATA PROTECTION

Separate sensitive information/systems from normal systems.

Example:

Employees
   X
Payment Card Environment

This reduces who can reach the sensitive environment.

PERMISSION RESTRICTIONS

Use access control.

Example:

HR employee → HR files

IT employee → IT systems

Normal employee → no payroll database

Principle:

Least privilege

3.4 — RESILIENCE AND RECOVERY

This section covers high availability, hot/warm/cold sites, geographic dispersion, multi-cloud, capacity planning, testing, backups, replication, journaling, generators and UPS.

HIGH AVAILABILITY

Goal:

keep services operational even when components fail.

Two important technologies:

Load balancing
Clustering
LOAD BALANCING

Distributes requests among servers.

Users
↓
Load Balancer
├ Server A
├ Server B
└ Server C

Purpose:

performance
scalability
availability
CLUSTERING

Multiple systems work together and can take over for one another.

Example:

Database Server A
↕
Database Server B

If A fails:

B takes over.

LOAD BALANCING VS CLUSTERING

Simplified Security+ distinction:

Load balancing

distributes workload.

Clustering

systems cooperate to provide redundancy/failover.

They can exist together.

REDUNDANCY

Having extra components.

Examples:

Two power supplies
Two Internet providers
Two firewalls
Multiple servers
RAID disks

Goal:

eliminate single points of failure.

SINGLE POINT OF FAILURE

Something whose failure causes the entire service to fail.

Example:

3 servers
↓
1 switch

If that single switch dies:

all servers become unavailable.

Solution:

redundant switches
HOT SITE

A hot site is a disaster recovery site that is:

almost immediately ready.

Contains:

hardware
network
systems
applications
recent data

Recovery time:

very short.

Cost:

very high.

Memory:

HOT = ready NOW.

WARM SITE

Partially prepared.

May contain:

hardware
network
some software

but may require:

latest backups
configuration
activation

Middle option:

medium recovery time + medium cost.

COLD SITE

Basically a facility/location with basic infrastructure.

May contain:

power
space
network connectivity

But not ready systems/data.

Recovery:

slow.

Cost:

cheapest.

Memory:

HOT → fastest + expensive

WARM → middle

COLD → slowest + cheapest
GEOGRAPHIC DISPERSION

Do not place all infrastructure in the same physical area.

Example:

Bad:

Main Data Center → Lisbon
Backup Data Center → building next door

Flood/power outage could affect both.

Better:

Primary → Portugal

Backup → Spain

Geographic dispersion protects against:

floods
earthquakes
regional outages
fires
power problems
PLATFORM DIVERSITY

Using different platforms/technologies can prevent one vulnerability from affecting everything.

Example:

System A → Linux

System B → Windows

But diversity creates:

additional management complexity.

MULTI-CLOUD

Using more than one cloud provider.

Example:

AWS
+
Azure

Benefit:

avoid total dependency on one provider.

Can improve resilience.

Problems:

more complex;
more expensive;
different security controls;
difficult monitoring.
CONTINUITY OF OPERATIONS

The organization should be able to keep critical functions operating during disruptions.

Think:

“How do we keep the business working?”

It includes:

people
systems
communications
facilities
alternative processes
CAPACITY PLANNING

Ensures resources can handle current and future demand.

CompTIA groups this around:

People
Technology
Infrastructure
PEOPLE

Do we have enough:

administrators
security analysts
support staff
specialists
TECHNOLOGY

Do systems have enough:

CPU
RAM
storage
licenses
applications
INFRASTRUCTURE

Do we have enough:

bandwidth
power
cooling
servers
network capacity
TABLETOP EXERCISE

People discuss a hypothetical disaster.

Example:

“Ransomware has taken down the main data centre. What do we do?”

No real systems are normally interrupted.

Advantages:

cheap
safe
easy
SIMULATION

A more realistic exercise.

Example:

Security team simulates:

network outage
ransomware
disaster

without necessarily damaging production.

FAILOVER TEST

Tests whether systems correctly switch from primary to backup.

Example:

Server A OFF
↓
Server B automatically takes over
PARALLEL PROCESSING

Primary and secondary systems operate simultaneously.

This can provide:

redundancy
availability
performance
BACKUPS

One of the most important concepts in recovery.

Basic rule:

A backup is useful only if you can restore it.

ONSITE BACKUP

Stored at the same location.

Advantages:

fast restoration
easy access

Risk:

fire
flood
ransomware
physical disaster

may destroy both production data and backup.

OFFSITE BACKUP

Stored somewhere else.

Provides protection from local disasters.

Example:

Primary data → office

Backup → remote data centre/cloud
BACKUP FREQUENCY

How often do you back up?

Example:

Hourly
Daily
Weekly

More frequent backup:

less potential data loss.

But:

more storage/resources may be required.

FULL BACKUP

Copies everything.

Advantages:

easiest restoration.

Disadvantages:

slow backup;
large storage.
INCREMENTAL BACKUP

Copies data changed since:

the most recent backup of any type.

Example:

Sunday → Full

Monday → changes since Sunday

Tuesday → changes since Monday

Wednesday → changes since Tuesday

Advantages:

fastest backups, less storage.

Restore:

Full
+
Monday
+
Tuesday
+
Wednesday

Therefore restoration can be slower.

DIFFERENTIAL BACKUP

Copies everything changed since:

the last full backup.

Example:

Sunday → Full

Monday → Monday changes

Tuesday → Monday + Tuesday changes

Wednesday → Monday + Tuesday + Wednesday changes

Restore requires:

Full
+
latest differential
FULL VS DIFFERENTIAL VS INCREMENTAL

Memorize:

Backup	Backup speed	Restore speed	Storage
Full	Slow	Fast	High
Differential	Medium	Medium/Fast	Medium
Incremental	Fast	Slow	Low
BACKUP ENCRYPTION

Backups can contain:

everything valuable in your company.

Therefore backups should often be encrypted.

If attacker steals unencrypted backup:

attacker may get the entire database.

SNAPSHOT

Snapshot records the state of a system at a particular moment.

Example:

VM at 10:00

Later update breaks VM.

Restore:

10:00 snapshot

Important:

Snapshot is useful but should not automatically be considered a complete independent backup.

REPLICATION

Copies data/systems to another location.

Example:

Primary database
↓
continuous replication
↓
Secondary database

If primary fails:

secondary may take over.

BACKUP VS REPLICATION

Very important.

Backup

Historical copy.

Can restore old information.

Replication

Copies current changes to another system.

Problem:

If ransomware encrypts primary data:

encrypted data
↓
replication
↓
secondary may also receive encrypted changes

Therefore:

replication does NOT replace backups.

JOURNALING

Records changes/transactions as they occur.

Example database:

Transaction 1
Transaction 2
Transaction 3
...

If database fails:

journal can help replay/reconstruct changes.

Think:

Journaling = record of changes.

BACKUP 3-2-1 RULE

Very useful real-world principle:

3 copies of data

2 different media types

1 copy offsite

Example:

Production data

Local backup

Cloud/offsite backup
IMMUTABLE BACKUP

A backup that cannot easily be changed/deleted for a defined period.

Excellent against:

ransomware.

Attacker cannot simply:

encrypt/delete backup
GENERATOR

Provides electricity during longer power outages.

But generators:

normally take some time to start.

UPS — UNINTERRUPTIBLE POWER SUPPLY

Provides immediate temporary power.

Example:

Power fails
↓
UPS immediately supplies electricity
↓
Generator starts
↓
Generator takes over

UPS gives administrators time to:

keep systems running
or
shut down safely
UPS VS GENERATOR

Very common distinction.

UPS
Immediate power
Short duration
Battery
Generator
Starts after short delay
Long duration
Fuel

Memory:

UPS = immediate bridge

Generator = long-term power