# Zapp-Automation

This repository contains a Python script to automate security scanning using the OWASP ZAP (Zed Attack Proxy) Docker image. The script facilitates a full security scan on a given target URL with authentication.

## Script Details

The `zapp.py` script:

1. Prompts the user for the target URL, login URL, email, and password.
2. Configures and runs the `zap-full-scan.py` script using the `ictu/zap2docker-weekly` Docker image.
3. Redirects the scan output to a file (`scan_output.txt`).
4. Logs the duration of the scan.

## Prerequisites

- Docker must be installed and running on your system.
- After Docker is installed and running on your system, pull the docker image.
  ```bash
  docker pull ictu/zap2docker-weekly
- Python 3.x

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/akhil218/Zapp-Automation.git
   cd zapp-automation
