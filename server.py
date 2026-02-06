from flask import Flask, request

app = Flask(__name__)

@app.route('/iclock/cdata', methods=['GET', 'POST'])
def receive_data():
    print("REQUETE K50 RECUE")
    print(request.data)
    return "OK"

@app.route('/')
def home():
    return "Serveur K50 actif"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
