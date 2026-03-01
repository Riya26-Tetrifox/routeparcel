import json
def get_vulnerable_packages(report_file):
    with open(report_file) as f:
        data = json.load(f)

    vulnerabilities = []

    for result in data.get("Results", []):
        for vuln in result.get("Vulnerabilities", []):
            if vuln.get("Severity") in ["HIGH", "CRITICAL"]:
                vulnerabilities.append({
                    "package": vuln["PkgName"],
                    "current_version": vuln["InstalledVersion"],
                    "fixed_version": vuln.get("FixedVersion"),
                     "cve_id": vuln.get("VulnerabilityID"),
                    "severity": vuln.get("Severity")
                })
    return vulnerabilities
   
