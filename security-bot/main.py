from parser import get_vulnerable_packages
from updater import update_package
from notifier import send_email
import sys
import json

def main():
    report_path = "security-bot/report/trivy_report.json"

    # Ensure we handle missing report gracefully
    try:
        vulns = get_vulnerable_packages(report_path)
    except FileNotFoundError:
        print(f"Error: Trivy report not found at {report_path}")
        # Return a clear message but exit 0 so CI/CD doesn't fail unexpectedly
        return "REPORT_MISSING"

    if not vulns:
        print("No vulnerabilities found")
        return "NO_VULNERABILITIES"

    print("VULNERABILITIES_DETECTED")  # Workflow will look for this string
    message = "Subject: Security Alert 🚨\n\n"
    message += "HIGH / CRITICAL Vulnerabilities Detected:\n\n"

    for vuln in vulns:
        # Apply the fix
        update_package(vuln["package"], vuln["fixed_version"])

        message += (
            f"Package: {vuln['package']}\n"
            f"Installed Version: {vuln['current_version']}\n"
            f"Fixed Version: {vuln['fixed_version']}\n"
            f"CVE ID: {vuln['cve_id']}\n"
            f"Severity: {vuln['severity']}\n"
            "-----------------------------------\n"
        )

    print("Vulnerabilities List:", json.dumps(vulns, indent=2))

    # Send email alert
    try:
        send_email(message)
    except Exception as e:
        print(f"Warning: Failed to send email: {e}")

    # Instead of exiting 1, just return string so Bash can capture it
    return "VULNERABILITIES_FOUND"


if __name__ == "__main__":
    output = main()
    # Exit 0 always for CI/CD safety; workflow uses output string to detect fixes
    if output == "VULNERABILITIES_FOUND":
        print("VULNERABILITIES_FOUND")
    elif output == "NO_VULNERABILITIES":
        print("NO_VULNERABILITIES")
    elif output == "REPORT_MISSING":
        print("REPORT_MISSING")
    sys.exit(0)
