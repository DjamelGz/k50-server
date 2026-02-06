from flask import Flask, request

app = Flask(__name__)

# Dictionnaire ID → Nom (ajoute d'autres utilisateurs si nécessaire)
users = {
    "1": "Djamel",
    # "2": "Sami",
    # "3": "Leila",
}

@app.route('/iclock/cdata', methods=['POST'])
def receive_data():
    data = request.data.decode(errors="ignore").strip()
    if not data:
        return "OK"

    # Filtrer uniquement les vrais pointages
    table = request.args.get("table")
    if table != "ATTLOG":
        return "OK"  # ignorer OPERLOG et autres tables

    # Exemple de data reçue : '1\t2026-02-07 07:35:52\t0\t1\t0\t0\t0\t0\t0\t0\t'
    fields = data.split('\t')
    if len(fields) >= 2:
        user_id = fields[0]
        timestamp = fields[1]
        name = users.get(user_id, f"Utilisateur {user_id}")
        print(f"Bienvenue {name} ! Heure : {timestamp}")
    else:
        print(f"Impossible de parser les données: {data}")

    return "OK"

@app.route('/iclock/getrequest', methods=['GET'])
def get_request():
    sn = request.args.get("SN")
    print(f"📤 COMMAND REQUEST from {sn}")

    # Demander au K50 d’envoyer les templates si besoin
    command = "DATA QUERY FINGERTMP\n"
    return command

@app.route('/')
def home():
    return "Serveur K50 actif"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
