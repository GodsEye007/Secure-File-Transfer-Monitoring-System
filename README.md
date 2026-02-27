# Secure File Transfer Monitoring System

## Project Overview
The Secure File Transfer Monitoring System is a cybersecurity monitoring tool developed to track file activity and detect unauthorized movement of sensitive files within a system.

File transfers and modifications can pose security risks such as data leakage, insider threats, and file tampering. This project demonstrates how monitoring file system activity can help detect suspicious behavior and maintain file integrity.

The system monitors file operations, detects activity involving sensitive files, verifies file integrity using SHA-256 hashing, and records all events in security logs.

---

## Features
- File system activity monitoring
- Detection of sensitive file access
- File integrity verification using SHA-256 hashing
- Security alert generation for sensitive file events
- Activity logging for audit purposes
- Final audit report summarizing monitored activity

---

## Technologies Used
- Python
- Kali Linux
- Watchdog (filesystem monitoring)
- Hashlib (file integrity hashing)

---

## Project Structure

SecureMonitor/
│
├── monitor.py
│
├── monitored/
│   Normal files used for testing file activity
│
├── sensitive/
│   Contains sensitive files that trigger alerts
│
├── logs/
│   └── file_activity.log
│
└── reports/
    └── audit_report.txt

---

## How the System Works
1. The monitoring script observes filesystem activity in the project directory.
2. Events such as file creation, modification, deletion, and movement are detected.
3. If the activity involves a sensitive directory, a security alert is generated.
4. The system calculates SHA-256 hashes of files to detect integrity changes.
5. All events are recorded in a log file.
6. A final audit report summarizes detected activities.

---

## Example Alert Output

[2026-01-03 05:26:34] MODIFIED - sensitive/secret.txt | HASH: 4e20620845428ff04bf87ab5bb24c4627121ac45703ebc32f3b7099f017566ef ⚠️ ALERT: Sensitive file activity detected

---

## Learning Outcomes
- File system monitoring techniques
- Detection of sensitive file access
- Hash-based integrity verification
- Security logging and auditing
- Basic Data Loss Prevention (DLP) concepts

---

## Author
Akash Kachare  
Cybersecurity Internship Project
