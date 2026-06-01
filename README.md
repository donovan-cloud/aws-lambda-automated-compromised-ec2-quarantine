# AWS Lambda Automated Compromised EC2 Quarantine

[![Runtime](https://img.shields.io/badge/Runtime-Python%203.11-blue.svg)](https://www.python.org/)
[![Service](https://img.shields.io/badge/Service-AWS%20Lambda-orange.svg)](https://aws.amazon.com/lambda/)
[![Function](https://img.shields.io/badge/Ops-Incident%20Response-red.svg)](https://aws.amazon.com/security/)

## 📋 Operational Overview

This repository contains an automated incident response playbook executed via AWS Lambda. 

When an EC2 instance exhibits malicious behavior (such as a command-and-control beacon detected by GuardDuty), response time is critical. This Python-based Lambda function acts as an automated triage mechanism. When triggered, it instantly detaches the compromised instance from its active production security groups, attaches an isolated "Quarantine" security group (blocking all ingress/egress traffic), terminates any active SSH/RDP sessions, and takes a snapshot of the root volume for later forensic investigation.

---

### 🛡️ Core Incident Response Controls

* **Zero-Trust Network Isolation:** Instantly replaces active security groups with an isolated, zero-traffic firewall boundary.
* **Automated Forensic Evidence Preservation:** Captures a point-in-time EBS snapshot of the volume before attackers can execute anti-forensic wiping scripts.
* **Metadata Tagging for SecOps:** Automatically stamps the instance with critical metadata tags highlighting the quarantine event status.

---

## 📂 Repository Structural Mapping

```text
aws-lambda-automated-compromised-ec2-quarantine/
├── README.md                      # Playbook runbook operational logic
├── lambda_function.py             # Active containment automation script
└── event_trigger_sample.json      # Sample GuardDuty event payload schema
