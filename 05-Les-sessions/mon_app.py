from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "9d263e09465118fcc3b288369ed53396922588fc3e8f466845ef8ab6a00cef25"

@app.route("/")
def index():
    return render_template("index.html")

utilisateurs = [
    {"nom": "admin", "mdp": "1234"},
    {"nom": "marie", "mdp": "nsi"},
    {"nom": "paul", "mdp": "azerty"}  
]

def recherche_utilisateur(nom_utilisateur, mot_de_passe):
    for utilisateur in utilisateurs:
        if utilisateur['nom'] == nom_utilisateur and utilisateur['mdp'] == mot_de_passe:
            return utilisateur
    return None

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')

        utilisateur = recherche_utilisateur(nom, mdp)

        if utilisateur is not None:
            print("utilisateur trouvé")
            session['nom_utilisateur'] = utilisateur['nom']
            print(session)
            return redirect(url_for('index'))
        else:
            print("utilisateur inconnu")
            return redirect(request.url)
    else:
        print(session)
        if 'nom_utilisateur' in session:
            return redirect(url_for('index'))
        return render_template("login.html")

@app.route('/logout')
def logout():
    print(session)
    session.pop('nom_utilisateur', None)
    print(session)
    return redirect(url_for('login'))

@app.route("/compteur")
def compteur():
    if "compteur" not in session:
        session['compteur'] = 1
    else:
        session['compteur'] = session['compteur'] + 1
    print(session)
    nb_visites = session['compteur']
    return f"Vous avez visité cette page {nb_visites} fois"


@app.route("/traitement", methods=["POST", "GET"])
def traitement():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        if nom == 'admin' and mdp == '1234':
            return render_template("traitement.html", nom_utilisateur=nom)
        else:
            return render_template("traitement.html")
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
