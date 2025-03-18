from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "PC Control API is Running!"

@app.route("/command/<action>")
def command(action):
    if action == "shutdown":
        os.system("shutdown /s /t 5")  # Shutdown PC in 5 seconds
    elif action == "sleep":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Sleep PC
    elif action == "lock":
        os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock PC
    return f"Command executed: {action}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
