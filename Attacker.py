try:
    import requests 
except:
    from os import system
    system('pip install requests')
    import requests 
ip = input("IP: ")
while(1):
    command = input("Command: ")
    data = {
        "Password":"root",
        "Command":command
    }
    status = int(requests.post(f"http://{ip}:4444/",data=data).status_code)
    if(status==200):
        print("Successful")
    elif(status==401):
        print("Password incorrect")
    else:
        print(f"Error Status Code {status}")