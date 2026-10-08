# 🛡️ ISEC3004 Assignment 1: Web Security Vulnerability Analysis

This repository contains the vulnerable code, exploit payloads, mitigated code, forensic evidence, and the final report for the **ISEC3004 Assignment 1**. 

Our team successfully analyzed, exploited, detected, and mitigated two critical web vulnerabilities:
1. **Cross-Site Request Forgery (CSRF)** - *CWE-352*
2. **Log Injection (CRLF Injection)** - *CWE-117*

This project demonstrates the real-world impact of these vulnerabilities and provides industry-standard mitigation strategies, following a structured Agile development lifecycle.

---

## 🔗 Quick Links & Resources
- 📄 **[Final Project Report (PDF)](docs/ISEC3004_Report_Group13.pdf)** 
- 📊 **[GitHub Projects Board](https://github.com/users/oshadhisadinya/projects/3/views/1)** *(Task Tracking & Burnup Chart)*
- 📅 **[Gantt Chart & Project Schedule](https://github.com/oshadhisadinya/ISEC3004_Assignment1_Group13/blob/main/docs/ISEC3004_Assignement01_Gantt%20Chart.xlsx)**
- 📂 **[Shared OneDrive Folder](https://curtin-my.sharepoint.com/:f:/g/personal/22520933_student_curtin_edu_au/IgC3-Nb63j-vS7HIOHeTW_xrASNC-AEaPzmCCqP0kn-mvy4)** *(Collaborative Documents)*

---

## 👥 Team Members & Roles
| Member | Name | Student ID | Role & Responsibilities |
| :--- | :--- | :---: | :--- |
| **Member 1** | Elizabeth Kristina Motha | 22396545 | CSRF Vulnerability Development & Exploit Payload Creation |
| **Member 2** | Ameli Jithmini | 22520933 | CSRF Mitigation, Tracing (Burp Suite) & QA Testing |
| **Member 3** | Bhagya Wijenanda | 22716509 | Log Injection Vulnerability Development & CRLF Payload Creation |
| **Member 4** | Arindi Dulanya | 23080234 | Log Injection Mitigation, Log Analysis & QA Testing |
| **Member 5** | Oshadhi Sadinya Alahapperuma | 22169585 | Integration Lead, Project Management, QA & Report Compilation |

---

## 📂 Repository Structure

```text
ISEC3004_Assignment1_Group13/
│
├── vulnerable_app/       # Contains the integrated vulnerable Flask application
├── mitigated_app/        # Contains the security-enhanced (fixed) Flask application
├── exploits/             # Contains malicious payloads (csrf_payload.html, log_injection_exploit.py)
├── evidence/             # Contains Burp Suite traces, terminal outputs, and log file screenshots
├── docs/                 # Contains Meeting Minutes, Gantt Chart, and QA Checklists
├── .gitignore            # Files and folders to be ignored by Git
└── README.md             # Project documentation and setup instructions

---
## 🚀 How to Run the Application

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Git

### Step 1: Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone https://github.com/oshadhisadinya/ISEC3004_Assignment1_Group13.git
cd ISEC3004_Assignment1_Group13

