# 🛡️ ISEC3004 Assignment 1 — Web Security Vulnerability Analysis

This repository contains the source code, exploit payloads, mitigation implementations, forensic evidence, testing documentation, and final report for **ISEC3004 Assignment 1**.

Our team analysed, exploited, detected, mitigated, and tested two critical web application security vulnerabilities:

1. **Cross-Site Request Forgery (CSRF)** — CWE-352
2. **Log Injection (CRLF Injection)** — CWE-117

The project demonstrates the **real-world impact of these vulnerabilities**, their exploitation techniques, detection methods, and industry-standard mitigation strategies.

The project was developed using a structured **Agile development lifecycle**, supported by GitHub Projects, feature branches, pull requests, testing, and project scheduling.

---

## 🔐 Vulnerabilities Analysed

### 1. Cross-Site Request Forgery (CSRF)

**CWE:** [CWE-352 — Cross-Site Request Forgery](https://cwe.mitre.org/data/definitions/352.html)

CSRF is a web security vulnerability where an attacker tricks an authenticated user into unknowingly sending a malicious request to a web application.

In our vulnerable application, an attacker can forge a request to change the authenticated user's email address without providing a valid CSRF token.

**Demonstrated using:**

* Malicious HTML payload
* Forged POST request
* Burp Suite request analysis
* Vulnerable Flask application
* Mitigated Flask application

**Mitigation implemented:**

* CSRF token validation
* Server-side request validation
* Rejection of requests containing invalid or missing tokens

---

### 2. Log Injection / CRLF Injection

**CWE:** [CWE-117 — Improper Output Neutralization for Logs](https://cwe.mitre.org/data/definitions/117.html)

Log Injection occurs when untrusted user input is written directly into application logs without proper sanitisation.

An attacker can inject newline characters such as `CR` (`\r`) and `LF` (`\n`) to create forged log entries or manipulate the appearance and integrity of log files.

**Demonstrated using:**

* Malicious CRLF payload
* Python exploit script
* Vulnerable logging implementation
* Log file analysis
* Forensic evidence

**Mitigation implemented:**

* Input validation
* Log sanitisation
* Removal/neutralisation of newline characters
* Safe logging practices

---

# 🔗 Quick Links & Resources

| Resource                                                                                                                                                     | Description                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| 📄 [Final Project Report](docs/ISEC3004_Report_Group13.pdf)                                                                                                  | Final assignment report            |
| 📊 [GitHub Projects Board](https://github.com/users/oshadhisadinya/projects/3/views/1)                                                                       | Task tracking and project progress |
| 📅 [Gantt Chart & Project Schedule](https://github.com/oshadhisadinya/ISEC3004_Assignment1_Group13/blob/main/docs/ISEC3004_Assignement01_Gantt%20Chart.xlsx) | Project schedule and milestones    |
| 📂 [Shared OneDrive Folder](https://curtin-my.sharepoint.com/:f:/g/personal/22520933_student_curtin_edu_au/IgC3-Nb63j-vS7HIOHeTW_xrASNC-AEaPzmCCqP0kn-mvy4)  | Collaborative project documents    |

---

# 👥 Team Members & Responsibilities

| Member       | Name                         | Student ID | Role & Responsibilities                                           |
| ------------ | ---------------------------- | ---------: | ----------------------------------------------------------------- |
| **Member 1** | Elizabeth Kristina Motha     |   22396545 | CSRF vulnerability development and exploit payload creation       |
| **Member 2** | Ameli Jithmini               |   22520933 | CSRF mitigation, Burp Suite tracing and QA testing                |
| **Member 3** | Bhagya Wijenanda             |   22716509 | Log Injection vulnerability development and CRLF payload creation |
| **Member 4** | Arindi Dulanya               |   23080234 | Log Injection mitigation, log analysis and QA testing             |
| **Member 5** | Oshadhi Sadinya Alahapperuma |   22169585 | Integration lead, project management, QA and report compilation   |

---

# 📂 Repository Structure

```text
ISEC3004_Assignment1_Group13/
│
├── vulnerable_app/
│   └── app.py
│
├── mitigated_app/
│   └── app.py
│
├── exploits/
│   ├── csrf_payload.html
│   └── log_injection_exploit.py
│
├── evidence/
│   ├── Burp Suite traces
│   ├── terminal outputs
│   └── log analysis screenshots
│
├── docs/
│   ├── Final Project Report
│   ├── Meeting Minutes
│   ├── Gantt Chart
│   └── QA Checklists
│
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

Before running the project, make sure the following are installed:

* **Python 3.8 or higher**
* **Git**
* A modern web browser
* **Burp Suite** *(required for the security demonstration/testing activities)*

---

## 1. Clone the Repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/oshadhisadinya/ISEC3004_Assignment1_Group13.git
```

Then navigate into the project directory:

```bash
cd ISEC3004_Assignment1_Group13
```

---

## 2. Create a Virtual Environment

Using a virtual environment is recommended to keep the project's dependencies isolated.

### Windows — PowerShell

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Install Flask:

```bash
pip install flask
```

If a `requirements.txt` file is added to the repository in the future, dependencies can instead be installed using:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Applications

The repository contains two versions of the application:

* `vulnerable_app` — intentionally vulnerable version used for exploitation
* `mitigated_app` — security-enhanced version containing the implemented fixes

> ⚠️ **Important:** The vulnerable application is intentionally insecure and should only be run in a controlled local environment for educational and assessment purposes.

---

## 🔴 Run the Vulnerable Application

From the project root:

```bash
cd vulnerable_app
python app.py
```

The application should be available at:

```text
http://127.0.0.1:5000
```

---

## 🟢 Run the Mitigated Application

Stop the vulnerable application first, then return to the project root:

```bash
cd ..
cd mitigated_app
python app.py
```

The application should be available at:

```text
http://127.0.0.1:5000
```

---

# 🔑 Demo Login Credentials

The application uses the following demonstration account:

```text
Username: student
Password: password123
```

> ⚠️ These credentials are for the local educational demonstration environment only and should not be reused for real applications.

---

# ⚔️ Exploitation & Live Demonstration

The exploit payloads are stored inside the `exploits/` directory.

## 🔴 CSRF Exploit

The CSRF exploit demonstrates how an attacker can submit a forged request while the victim is authenticated.

### Method 1 — Malicious HTML Payload

1. Start the vulnerable application.
2. Open the application in a browser.
3. Log in using the demonstration credentials.
4. Open:

```text
exploits/csrf_payload.html
```

5. Observe the forged request.
6. Verify that the user's email address has been changed.

### Method 2 — Burp Suite

A forged POST request can also be reproduced using Burp Suite Repeater.

The vulnerable request targets:

```text
/change-email
```

The vulnerable implementation does not require a valid CSRF token.

The mitigated implementation validates the CSRF token and rejects forged requests.

---

## 🔴 Log Injection Exploit

The Log Injection exploit demonstrates how malicious input can manipulate application log entries.

Run the vulnerable application first.

Then, from the project root, execute:

```bash
python exploits/log_injection_exploit.py
```

After the exploit runs, inspect the generated application log:

```text
app_vulnerable.log
```

The injected input demonstrates how an attacker can create a forged log entry such as:

```text
Admin access granted
```

This demonstrates the importance of sanitising untrusted input before writing it to application logs.

---

# 🛡️ Security Mitigations

## CSRF Mitigation

The mitigated application implements CSRF protection by:

* Generating/validating CSRF tokens
* Requiring a valid token for protected requests
* Rejecting requests with missing or invalid tokens
* Validating requests server-side

### Security Flow

```text
User
  │
  ▼
Authenticated Request
  │
  ▼
CSRF Token Validation
  │
  ├── Valid ──────► Process Request
  │
  └── Invalid ────► Reject Request
```

---

## Log Injection Mitigation

The mitigated application protects logging functionality by:

* Validating user input
* Sanitising newline characters
* Preventing forged log entries
* Safely handling untrusted input before logging
* Maintaining the integrity of application logs

### Security Flow

```text
User Input
    │
    ▼
Input Validation
    │
    ▼
Log Sanitisation
    │
    ▼
Safe Logging
    │
    ▼
Application Log
```

---

# 🧪 Testing & Quality Assurance

Testing was performed throughout the development process to verify both the vulnerabilities and their mitigations.

Testing activities included:

* Functional testing
* Security testing
* CSRF exploit testing
* CSRF mitigation testing
* Log Injection exploit testing
* Log sanitisation testing
* Burp Suite request analysis
* Negative testing with invalid input
* Regression testing
* Integration testing

Evidence from the testing process is stored in:

```text
evidence/
```

QA documentation and checklists are stored in:

```text
docs/
```

---

# 🔎 Vulnerable vs Mitigated Application

| Security Area       | Vulnerable Application | Mitigated Application       |
| ------------------- | ---------------------- | --------------------------- |
| CSRF Protection     | ❌ Not implemented      | ✅ CSRF token validation     |
| Forged POST Request | ❌ Accepted             | ✅ Rejected                  |
| Input Validation    | ❌ Insufficient         | ✅ Implemented               |
| Log Injection       | ❌ Vulnerable           | ✅ Mitigated                 |
| CRLF Characters     | ❌ Accepted             | ✅ Sanitised                 |
| Log Integrity       | ❌ Can be manipulated   | ✅ Protected                 |
| Security Testing    | ✅ Exploited            | ✅ Retested after mitigation |

---

# 📊 Project Management

The project followed an Agile development approach.

## Task Tracking

GitHub Projects was used to manage tasks through the following workflow:

```text
To Do
  │
  ▼
In Progress
  │
  ▼
Testing / QA
  │
  ▼
Done
```

Project board:

[GitHub Projects Board](https://github.com/users/oshadhisadinya/projects/3/views/1)

---

## 📅 Project Schedule

The project timeline and milestones were managed using a Gantt Chart.

[Gantt Chart & Project Schedule](https://github.com/oshadhisadinya/ISEC3004_Assignment1_Group13/blob/main/docs/ISEC3004_Assignement01_Gantt%20Chart.xlsx)

---

# 🌿 Git Workflow

The team followed a structured Git workflow to support collaborative development.

Feature branches were created for individual tasks, for example:

```text
feature/csrf-vulnerable
feature/csrf-mitigation
feature/log-injection-vulnerable
feature/log-injection-mitigation
```

The general workflow was:

```text
Create Feature Branch
        │
        ▼
Develop / Implement
        │
        ▼
Test
        │
        ▼
Commit Changes
        │
        ▼
Push Branch
        │
        ▼
Create Pull Request
        │
        ▼
Code Review
        │
        ▼
Merge
```

This workflow helped the team:

* Avoid direct changes to the main branch
* Reduce merge conflicts
* Review code before integration
* Track individual contributions
* Maintain a clear development history

---

# 📸 Evidence

The repository contains supporting evidence for the vulnerability analysis and testing process.

Evidence includes:

* Burp Suite request/response traces
* Exploitation results
* Terminal outputs
* Application log analysis
* Mitigation testing
* QA results

All supporting evidence is available in:

```text
evidence/
```

---

# 📄 Final Report

The complete assignment report is available here:

[📄 View Final Project Report](docs/ISEC3004_Report_Group13.pdf)

The report contains the detailed:

* Vulnerability analysis
* Exploitation methodology
* Security impact
* Mitigation strategies
* Testing results
* Forensic evidence
* Project management documentation
* Team contributions

---

# 📂 Shared Project Documents

Collaborative documents are maintained in the team's OneDrive folder:

[📂 Open Shared OneDrive Folder](https://curtin-my.sharepoint.com/:f:/g/personal/22520933_student_curtin_edu_au/IgC3-Nb63j-vS7HIOHeTW_xrASNC-AEaPzmCCqP0kn-mvy4)

---

# ⚠️ Educational Use Disclaimer

The vulnerable application and exploit scripts in this repository are intentionally insecure and are provided **strictly for educational and assessment purposes**.

Do not use these techniques against systems, applications, accounts, or networks without explicit authorisation.

The demonstrations should be performed only in a controlled local environment.

---

# 📚 References

* [MITRE CWE-352 — Cross-Site Request Forgery](https://cwe.mitre.org/data/definitions/352.html)
* [MITRE CWE-117 — Improper Output Neutralization for Logs](https://cwe.mitre.org/data/definitions/117.html)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

---

## 👥 ISEC3004 Assignment 1 — Group 13

**Web Security Vulnerability Analysis**

**Vulnerabilities:** CSRF & Log Injection
**Course:** ISEC3004
**Assignment:** Assignment 1
**Group:** 13
