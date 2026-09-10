DOMAIN 5 — SECURITY PROGRAM MANAGEMENT AND OVERSIGHT

Now we move away from technical operations.

Think:

Policies + risk + vendors + compliance + audits + people

5.1 — SECURITY GOVERNANCE

Governance means:

How an organization directs and controls its security program.

It determines:

who makes decisions;
who is responsible;
what rules exist;
how security aligns with business goals.
POLICIES

Policies are high-level rules.

Example:

All company information must be protected according to its classification.

Policies usually tell you:

WHAT must be done

not exactly how.

STANDARDS

Standards define mandatory technical requirements.

Example:

All company laptops must use AES-256 full-disk encryption.

More specific than policy.

PROCEDURES

Procedures explain:

exactly HOW to perform something.

Example:

1. Open BitLocker settings
2. Enable encryption
3. Store recovery key
4. Verify status
GUIDELINES

Recommended practices.

Unlike standards:

usually not mandatory.

Example:

Employees should avoid using public Wi-Fi whenever possible.

POLICY VS STANDARD VS PROCEDURE VS GUIDELINE

Very important.

POLICY
What must be achieved?

STANDARD
What mandatory requirement must be followed?

PROCEDURE
Exactly how do I do it?

GUIDELINE
Recommended best practice.
ACCEPTABLE USE POLICY — AUP

Defines acceptable use of company technology.

Examples:

Internet use
Company email
Personal software
Social media
USB devices
Company laptops
INFORMATION SECURITY POLICY

High-level policy describing how the organization protects information.

BUSINESS CONTINUITY POLICY

Defines expectations for maintaining business operations during disruptions.

DISASTER RECOVERY POLICY

Defines expectations for recovering technology/systems after disaster.

CHANGE MANAGEMENT POLICY

Defines how changes to systems must be controlled.

A change should normally involve:

Request
↓
Impact analysis
↓
Approval
↓
Testing
↓
Implementation
↓
Validation
↓
Documentation
ROLLBACK PLAN

You asked about this before.

A rollback plan answers:

What do we do if the change fails?

Example:

You update a production server.

Update breaks application.

Rollback plan:

restore previous software version
restore configuration
restore snapshot

Memory:

Rollback = go BACK to previous working state

CHANGE APPROVAL

Major changes should not be performed randomly.

Depending on organization they may require approval from:

manager;
system owner;
security team;
Change Advisory Board.
OWNER

The owner has responsibility/accountability for an asset or information.

Example:

Head of Finance owns the financial database.

CUSTODIAN

Custodian handles/protects the asset on behalf of the owner.

Example:

IT administrators manage the database server.

Simplified:

Owner → decides
Custodian → manages
DATA CONTROLLER

Common privacy concept.

The controller decides:

why and how personal data is processed.

DATA PROCESSOR

Processes data:

on behalf of the controller.

Example:

Company uses a cloud payroll provider.

Company:

controller.

Payroll company:

processor.

MOU

Memorandum of Understanding

Describes an understanding/agreement between organizations.

Usually less formal than a full legal contract.

MOA

Memorandum of Agreement

Similar concept but generally describes agreed responsibilities more formally.

For Security+, focus on:

documents describing cooperation/responsibilities between organizations.

NDA

Non-Disclosure Agreement

Legal agreement requiring confidential information not to be disclosed.

Example:

Employee learns trade secrets.

NDA says:

You may not disclose this information.

SLA

Service-Level Agreement

Defines expected service performance.

Example:

99.99% uptime
Critical response within 30 minutes
Backups every 4 hours
5.2 — RISK MANAGEMENT

Risk is one of the most important parts of Domain 5.

Think:

Something bad may happen to something valuable.

ASSET

Something valuable.

Examples:

server
customer database
reputation
building
employees
intellectual property
THREAT

Something capable of causing harm.

Examples:

attacker
fire
flood
malware
employee mistake
VULNERABILITY

A weakness.

Examples:

unpatched software
weak password
open port
poor physical security
RISK

Threat exploiting vulnerability and causing impact.

Very simplified:

Risk = Likelihood × Impact
RISK REGISTER

Document containing identified risks.

Could include:

Risk
Likelihood
Impact
Risk owner
Response
Status
Controls
RISK APPETITE

How much risk an organization is generally willing to accept.

Example:

A startup may tolerate greater risk than a bank.

RISK TOLERANCE

Acceptable variation around risk objectives.

Simplified for the exam:

how much risk an organization can tolerate.

RISK THRESHOLD

Specific level at which action must be taken.

INHERENT RISK

Risk:

before controls are applied.

Example:

Internet-facing server has high inherent risk.

RESIDUAL RISK

Risk remaining:

after security controls.

Initial risk
↓
Apply controls
↓
Residual risk

You can rarely reduce risk to zero.

RISK ACCEPTANCE

Organization knowingly accepts the risk.

Example:

Expected loss = €100
Security control = €100,000

Company may accept risk.

RISK MITIGATION

Apply controls to reduce risk.

Example:

Firewall
MFA
Encryption
Security training
RISK TRANSFER

Transfer financial responsibility to someone else.

Classic example:

cyber insurance.

Also contracts may transfer some liability.

Important:

You transfer financial consequences, not magically transfer the vulnerability itself.

RISK AVOIDANCE

Stop doing the risky activity.

Example:

Company decides not to offer a vulnerable public service at all.

FOUR RISK RESPONSES

Memorize:

Accept
Mitigate
Transfer
Avoid
QUALITATIVE RISK ANALYSIS

Uses descriptive categories.

Example:

Likelihood = High
Impact = Medium
Overall risk = High

Usually faster and more subjective.

QUANTITATIVE RISK ANALYSIS

Uses numbers/money.

Important formulas.

SLE

Single Loss Expectancy

How much money is lost from ONE incident.

Formula:

SLE = Asset Value × Exposure Factor

Example:

Asset Value = €100,000
Exposure Factor = 40%
SLE = 100,000 × 0.40
SLE = €40,000

One incident costs approximately:

€40,000.

ARO

Annualized Rate of Occurrence

How often event occurs per year.

Example:

Once every 5 years:

ARO = 0.2

Twice per year:

ARO = 2
ALE

Annualized Loss Expectancy

Expected annual loss.

Formula:

ALE = SLE × ARO

Example:

SLE = €40,000
ARO = 0.2
ALE = €8,000/year
SECURITY+ FORMULA MEMORY
SLE = AV × EF

ALE = SLE × ARO
BUSINESS IMPACT ANALYSIS — BIA

BIA identifies:

critical business functions;
impact of downtime;
recovery priorities;
dependencies.
RTO

Recovery Time Objective

Question:

How quickly must the system be restored?

Example:

RTO = 4 hours

System should be back within four hours.

Memory:

RTO = TIME

RPO

Recovery Point Objective

Question:

How much DATA can we afford to lose?

Example:

RPO = 30 minutes

Backups/data replication should limit loss to approximately 30 minutes of data.

Memory:

RPO = POINT in data history

MTTR

Often:

Mean Time to Repair / Restore

Average time needed to repair/recover something.

MTBF

Mean Time Between Failures

Average operating time between failures.

Higher MTBF:

more reliable.

5.3 — THIRD-PARTY RISK MANAGEMENT

Companies rely on:

cloud providers
software vendors
suppliers
contractors
MSPs
payment processors

These companies create:

third-party risk.

VENDOR ASSESSMENT

Before trusting vendor:

examine security controls;
review audit reports;
assess compliance;
inspect policies;
understand incident history;
check financial stability;
understand data handling.
DUE DILIGENCE

Research performed before entering an agreement.

Question:

Is this vendor safe/reliable enough?

DUE CARE

Taking reasonable actions to protect systems and information.

Easy way:

Due diligence → investigate
Due care → act responsibly
VENDOR MONITORING

Third-party assessment does not stop after signing contract.

Organizations should monitor:

security posture;
incidents;
compliance;
service performance;
contract requirements.
RIGHT-TO-AUDIT CLAUSE

Contract may give customer the right to:

audit the vendor.

SUPPLY CHAIN RISK

Attack does not directly target your company.

It compromises a supplier.

Example:

Trusted software vendor
↓
Vendor compromised
↓
Malicious update distributed
↓
Customers compromised
SLA

Again important with vendors.

Specifies expected:

uptime;
response times;
support;
performance.
NDA

Protects confidential information shared with third parties.

5.4 — COMPLIANCE

Compliance means:

following required laws, regulations, standards, or contractual requirements.

REGULATORY COMPLIANCE

Required by laws/regulations.

Examples may include privacy or industry regulations.

CONTRACTUAL COMPLIANCE

Requirement exists because of a contract.

Example:

Organization signs contract requiring specific encryption.

PCI DSS

Security standard for organizations processing payment card information.

Think:

credit/debit card data

GDPR

European privacy/data protection regulation.

Important concepts include:

personal data;
lawful processing;
data subject rights;
data minimization;
protection of personal information.
DATA LOCALIZATION / DATA RESIDENCY

Some laws/contracts require data to remain:

in a particular country or region.

This matters especially with cloud services.

PRIVACY

Organizations should control:

collection;
processing;
storage;
sharing;
deletion

of personal information.

DATA MINIMIZATION

Collect only information you actually need.

Example:

If registration only requires:

name
email

do not collect:

passport
home address
birth certificate

without reason.

5.5 — AUDITS AND ASSESSMENTS

You previously had difficulty with this.

AUDIT

An audit evaluates whether an organization complies with:

requirements;
policies;
standards;
regulations;
controls.
INTERNAL AUDIT

Performed by people:

inside the organization.

Example:

Company's internal audit department checks whether security policies are being followed.

Benefits:

frequent;
organization-specific;
helps discover problems before external audit.
EXTERNAL AUDIT

Performed by:

independent outside organization.

Usually provides greater independence/objectivity.

Example:

External auditors assess compliance certification.

INTERNAL VS EXTERNAL
Internal → our organization checks itself
External → independent outsider checks us
ASSESSMENT

A broader evaluation of security posture.

Examples:

vulnerability assessment;
risk assessment;
security assessment.
AD HOC ASSESSMENT

You asked about this before.

Ad hoc means:

performed when needed, without a regular schedule.

Example:

CEO hears about a new serious attack.

Security team immediately performs an assessment.

That is:

Ad hoc assessment

Not:

weekly
monthly
annually
SELF-ASSESSMENT

Organization evaluates itself.

THIRD-PARTY ASSESSMENT

External party evaluates organization.

PENETRATION TEST

Attempts to exploit weaknesses to determine real impact.

RED TEAM

Acts like attacker.

Goal:

compromise organization.

BLUE TEAM

Defensive team.

Goal:

detect and stop attacks.

PURPLE TEAM

Red + Blue cooperation.

Goal:

improve defensive capability by sharing information.

Memory:

RED → attack
BLUE → defend
PURPLE → improve together
5.6 — SECURITY AWARENESS

People are a major security risk.

Therefore organizations perform security awareness training.

PHISHING TRAINING

Employees learn to recognize:

suspicious links;
fake login pages;
unusual requests;
malicious attachments;
impersonation.
PHISHING SIMULATION

Organization sends fake phishing emails to employees.

Purpose:

measure and improve awareness.

Not to punish users.

SOCIAL ENGINEERING

Manipulating people rather than exploiting software.

Examples:

phishing
vishing
smishing
pretexting
tailgating
impersonation
PHISHING

Usually fraudulent email/message.

SMISHING

Phishing using:

SMS/text messages.

Memory:

SMishing = SMS

VISHING

Phishing using:

voice/phone calls.

Memory:

Vishing = Voice

SPEAR PHISHING

Highly targeted phishing attack against a specific person/group.

WHALING

Spear phishing targeting important executives.

Example:

CEO
CFO
Director
BUSINESS EMAIL COMPROMISE — BEC

Attacker impersonates or compromises a business email account.

Typical attack:

“CEO” tells finance employee to urgently transfer €50,000.

PRETEXTING

Attacker creates a believable fake story.

Example:

“I am from IT support. I need your password to repair your account.”

TAILGATING

Unauthorized person follows an authorized person into secure location.

Example:

Employee uses badge
Attacker walks behind them
SHOULDER SURFING

Watching someone enter:

password
PIN
sensitive information
USB DROP ATTACK

Attacker leaves malicious USB drives where employees will find them.

Curious employee inserts USB.

Malware executes.

SECURITY AWARENESS TOPICS

Employees should understand:

password security;
MFA;
phishing;
social engineering;
physical security;
reporting suspicious activity;
removable media;
safe Internet usage;
data handling.
REPORTING SUSPICIOUS ACTIVITY

Employees should know:

WHO to contact and HOW to report security incidents.

Early reporting can drastically reduce attack impact.