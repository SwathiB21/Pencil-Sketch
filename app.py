from flask import Flask, render_template
import os,time,socket
from flask import Flask, render_template, send_file, request
import pythoncom
import signal
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("mocker.html")
@app.route("/",methods = ['GET', 'POST'])
def ps():
    df = request.form.get('submit1')
    df1 = request.form.get('submit3')
    df2 = request.form.get('submit2')
    if df == "start_assistant":
        print("\nOpening pencil sketch")
        try:
            pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
            os.system("\& \"C:/Users/91630/AppData/Local/Microsoft/WindowsApps/python3.10.exe\" \"C:/Users/91630/OneDrive/Desktop/pencilsketch.py\"")
        except pythoncom.com_error:
            pass
        message = "start_assistant"
        return render_template("mocker1.html",msg=message)
    if df1 == "restart_assistant":
        print("\n\nrestarting the pencil sketch\n")
        try:
            pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
            os.system("\& \"C:/Users/91630/AppData/Local/Microsoft/WindowsApps/python3.10.exe\" \"C:/Users/91630/OneDrive/Desktop/pencilsketch.py\"")
        except pythoncom.com_error:
            pass
        message = "restart_assistant"
        return render_template("mocker2.html",msg=message)
    if df2 == "stop":
        print("\n Stopping flask server.\n")
        os.kill(os.getpid(),signal.SIGINT)
        
        message = "stop"
        return render_template("mocker3.html",msg=message)
    
if __name__ == "__main__":
    app.run(debug=True)
