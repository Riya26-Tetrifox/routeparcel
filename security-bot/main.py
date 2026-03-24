from parser import get_vulnerable_packages
from updater import update_package
import sys

def main():
    report_path = "security-bot/report/trivy_report.json"
    try:
        vulns = get_vulnerable_packages(report_path)
    except FileNotFoundError:
        print(f"Error: Trivy report not found at {report_path}")
        return "REPORT_MISSING"

    if not vulns:
        print("No vulnerabilities found")
        return "NO_VULNERABILITIES"

    for vuln in vulns:
        update_package(vuln["package"], vuln["fixed_version"])
    return "VULNERABILITIES_FOUND"


if __name__ == "__main__":
    main()
    sys.exit(0)
