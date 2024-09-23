from fastapi import FastAPI, HTTPException
from asterisk.ami import AMIClient, SimpleAction

app = FastAPI()

# Initialize Asterisk AMI client


# Endpoint to make calls giving caller and receiver
@app.post("/make-call")
def make_call(caller: str = "10", receiver: str = "1234"):
    ami_client = AMIClient(address="172.17.0.2", port=5038)
    
    ami_client.login(username="user", secret="password")

    action = SimpleAction(
        'Originate',
        Channel=f'PJSIP/{caller}',
        Exten=receiver,
        Priority=1,
        Context='internal',
        CallerID='python',
    )
    print(action,caller,receiver)

    ami_client.send_action(action)
    ami_client.logoff()
    return {"message": "Call initiated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
