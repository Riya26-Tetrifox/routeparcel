from parser import get_vulnerable_packages
from updater import update_package
from notifier import send_email
import sys

def main():
    vulns = get_vulnerable_packages("security-bot/report/trivy_report.json")

    if not vulns:
        print("No vulnerabilities found")
        sys.exit(0)
    print("Vulnerability detected")
    message = "Subject: Security Alert 🚨\n\n"
    message += "HIGH / CRITICAL Vulnerabilities Detected:\n\n"

    for vuln in vulns:
        update_package(vuln["package"], vuln["fixed_version"])

        message += (
            f"Package: {vuln['package']}\n"
            f"Installed Version: {vuln['current_version']}\n"
            f"Fixed Version: {vuln['fixed_version']}\n"
            f"CVE ID: {vuln['cve_id']}\n"
            f"Severity: {vuln['severity']}\n"
            "-----------------------------------\n"
        )

    print("Vulnerabilities List:", vulns)

    send_email(message)

    sys.exit(1)

if __name__ == "__main__":
    main()
