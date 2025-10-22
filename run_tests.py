import subprocess
import sys


# Simple entrypoint to run pytest programmatically
args = ["pytest", "-q", "--html=reports/test_report.html"]
code = subprocess.call(args)
sys.exit(code)