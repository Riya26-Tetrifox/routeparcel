from fastapi import Depends;
from backend.database import SessionLocal;
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    #   - name: Create Pull Request
    #     if: steps.auto_fix.outputs.fix_needed == 'true'
    #     uses: peter-evans/create-pull-request@v6
    #     with:
    #       commit-message: "🔐 Auto-fix HIGH/CRITICAL vulnerabilities"
    #       branch: security/auto-fix
    #       title: "Security Auto Remediation"
    #       body: |
    #         This PR automatically fixes HIGH/CRITICAL vulnerabilities detected by Trivy.
    #       add-paths: |
    #         requirements.txt
