# ISEC3004 Assignment 1: Web Security Vulnerability Analysis

## Project Overview
This repository contains the vulnerable code, exploit payloads,mitigated codes ,  evidence, and final report for the **ISEC3004 Assignment 1**. 

Our team successfully analyzed, exploited, detected, and mitigated two critical web vulnerabilities:
1. **Cross-Site Request Forgery (CSRF)**
2. **Log Injection (CRLF Injection)**

This project demonstrates the real-world impact of these vulnerabilities and provides industry-standard mitigation strategies.

---

## Team Members & Roles
| Member | Name | Role & Responsibilities |
| :--- | :--- | :--- |
| **Member 1** | Kristina | CSRF Vulnerability Development & Exploit Payload Creation |
| **Member 2** | Ameli | CSRF Mitigation, Tracing (Burp Suite) & QA Testing |
| **Member 3** | Bhagya | Log Injection Vulnerability Development & CRLF Payload Creation |
| **Member 4** | Arindi | Log Injection Mitigation, Log Analysis & QA Testing |
| **Member 5** | Sadinya | Integration Lead, Project Management, QA & Report Compilation |

---

## Repository Structure

ISEC3004_Assignment1_Group13/
│
├── vulnerable_app/       # Contains the integrated vulnerable Flask application
├── mitigated_app/        # Contains the security-enhanced (fixed) Flask application
├── exploits/             # Contains malicious payloads (HTML forms, Python scripts)
├── evidence/             # Contains Burp Suite traces and log file screenshots
├── docs/                 # Contains the final report, meeting minutes, and Gantt chart
├── .gitignore            # Files and folders to be ignored by Git
└── README.md             # Project documentation and setup instructions

---

## How to Run the Application

**Prerequisites**
Before running the application , ensure you have the following installed:
    . Python 3.8 or higher 
    . Git 

**Step 1: Clone the Repository**

Open your terminal or command prompt and run : 
      
      . git clone https://github.com/oshadhisadinya/ISEC3004_Assignment1_Group13.git
     
      . cd ISEC3004_Assignment1_Group13
         
**Step 2: Setup Virtual Environment(Recommended)**

For Windows(PowerShell)

    python -m venv .venv
    .venv\Scripts\Activate.ps1

(Note : If you get an execution policy error, run Set-ExecutionPolicy Unrestricted -Scope CurrentUser first).

For Mac/Linux :
    
    python3 -m venv .venv
    source .venv/bin/activate

**Step 3 : Install Dependencies**
       
    pip install flask

**Step 4 : Run the Application**

To run the Vulnerable App :
   
    cd vulnerable_app
    python app.py

To run the Mitigated(Secure) App :
  
    cd mitigated_app
    python app.py

*The application will start on http://127.0.0.1:5000.*

**Step 5 : Demo Login Credentials**

   . Username : student
   . Password : password123

---

## Project Management & Version Control ##
 
. Task Tracking : Managed via GitHub Projects Board (To Do , In Progress , Testing/QA , Done)

. Schedule : Project Timeline managed via Gantt Chart (Available in the docs/folder)

. Version Control : We strictly followed a professional Git workflow using feature branches (e.g., feature/csrf-vulnerable, feature/csrf-mitigation , feature/log-injection-vulnerable , feature/log-injection-mitigation, feature/integration) and Pull Requests (PRs) for all code integrations.



   


