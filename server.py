from flask import Flask, request

app = Flask(__name__)

# Dictionnaire ID utilisateur → Nom
users = {
    "1": "Djamel",
    "2": "Ahmed",
    "3": "Sophie",
    "4": "Fatima"
}

@app.route('/iclock/cdata', methods=['POST'])
def receive_data():
    data = request.data.decode(errors="ignore").strip()
    if not data:
        return "OK"

    # Exemple de format reçu : '2\t2026-02-07 06:54:27\t0\t1\t0\t0\t0\t0\t0\t0\t\n'
    fields = data.split('\t')
    user_id = fields[0]
    timestamp = fields[1]

    name = users.get(user_id, "Inconnu")
    print(f"Bienvenue {name} ! ID : {user_id} Heure : {timestamp}")
    return "OK"

@app.route('/iclock/getrequest', methods=['GET'])
def get_request():
    # On ne demande rien au K50 pour l'instant
    sn = request.args.get("SN")
    print(f"📤 COMMAND REQUEST from {sn}")
    return ""  # juste OK, pas de DATA QUERY

@app.route('/')
def home():
    return "Serveur K50 actif"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
