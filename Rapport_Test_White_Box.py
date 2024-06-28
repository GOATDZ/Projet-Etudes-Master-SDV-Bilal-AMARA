import re
from fpdf import FPDF
from zxcvbn import zxcvbn

# Fonction pour évaluer la force du mot de passe
def evaluate_password_strength(password):
    strength = zxcvbn(password)
    return strength

# Fonction pour vérifier les critères de complexité du mot de passe
def check_password_complexity(password):
    complexity_checks = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'\d', password)),
        'special_chars': bool(re.search(r'\W', password))
    }
    return complexity_checks

# Fonction pour générer un rapport PDF
def generate_pdf(password, strength, complexity_checks):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Titre du rapport
    pdf.cell(200, 10, txt="Rapport de Sécurité du Mot de Passe", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Mot de passe analysé : {password}", ln=True)
    
    # Résultats de la force du mot de passe
    pdf.cell(200, 10, txt="Force du mot de passe :", ln=True)
    pdf.cell(200, 10, txt=f"Score : {strength['score']} / 4", ln=True)
    pdf.cell(200, 10, txt=f"Temps pour deviner (en ligne, aucune contrainte) : {strength['crack_times_display']['online_no_throttling_10_per_second']}", ln=True)
    
    # Vérification de la complexité du mot de passe
    pdf.cell(200, 10, txt="Critères de complexité du mot de passe :", ln=True)
    for check, passed in complexity_checks.items():
        status = "OK" if passed else "Non satisfait"
        pdf.cell(200, 10, txt=f"{check} : {status}", ln=True)
    
    # Suggestions de renforcement
    pdf.cell(200, 10, txt="Suggestions pour renforcer le mot de passe :", ln=True)
    for suggestion in strength['feedback']['suggestions']:
        pdf.cell(200, 10, txt=f"- {suggestion}", ln=True)
    
    # Conseils de prévention
    pdf.cell(200, 10, txt="Conseils de prévention contre les attaques :", ln=True)
    pdf.multi_cell(0, 10, txt=(
        "1. Utilisez une combinaison de lettres majuscules et minuscules, de chiffres et de caractères spéciaux.\n"
        "2. Évitez d'utiliser des informations personnelles comme des noms, des anniversaires, etc.\n"
        "3. Utilisez un mot de passe d'au moins 12 caractères.\n"
        "4. Changez régulièrement vos mots de passe et n'utilisez pas le même mot de passe pour plusieurs comptes.\n"
        "5. Utilisez un gestionnaire de mots de passe pour stocker et générer des mots de passe forts."
    ))

    # Sauvegarde du fichier PDF
    pdf.output(f"rapport_mot_de_passe.pdf")

# Fonction principale
def main():
    password = input("Entrez le mot de passe à analyser: ")  # Saisie du mot de passe par l'utilisateur
    strength = evaluate_password_strength(password)  # Évaluation de la force du mot de passe
    complexity_checks = check_password_complexity(password)  # Vérification de la complexité du mot de passe
    generate_pdf(password, strength, complexity_checks)  # Génération du rapport PDF

if __name__ == "__main__":
    main()  # Exécution de la fonction principale
