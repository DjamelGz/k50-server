from flask import Flask, request

app = Flask(__name__)

# Dictionnaire ID → Nom (ici juste Djamel)
users = {
    "1": "Djamel"
}

@app.route('/iclock/cdata', methods=['POST'])
def receive_data():
    data = request.data.decode(errors="ignore").strip()
    if not data:
        return "OK"

    # Exemple reçu du K50 : '1\t2026-02-07 06:54:27\t0\t1\t0\t0\t0\t0\t0\t0\t\n'
    fields = data.split('\t')
    user_id = fields[0]
    timestamp = fields[1]

    # Cherche le nom dans le dictionnaire, sinon "Inconnu"
    name = users.get(user_id, f"Utilisateur {user_id}")
    print(f"Bienvenue {name} ! Heure : {timestamp}")
    return "OK"

@app.route('/iclock/getrequest', methods=['GET'])
def get_request():
    sn = request.args.get("SN")
    print(f"📤 COMMAND REQUEST from {sn}")

    # On n'a déjà Djamel dans le dictionnaire → rien à renvoyer
    return ""

@app.route('/')
def home():
    return "Serveur K50 actif"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
