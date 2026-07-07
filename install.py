import subprocess
import sys

# This forces Python to install Flask and Requests to its active location
subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "requests"])
print("\n🎉 SUCCESS! LIBRARIES ARE INSTALLED PERFECTLY! 🎉")
