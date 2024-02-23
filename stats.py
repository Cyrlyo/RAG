import os
import json

#TODO: add accurracy computation into mistralchat.py and print it in the consol

# Chemin du dossier contenant les fichiers JSON
dossier_output = "./output/llama2"

# Initialisation des compteurs
predictions_correctes = 0
predictions_incorrectes = 0

# Parcourir tous les fichiers dans le dossier "output"
for fichier_json in os.listdir(dossier_output):
    if fichier_json.endswith(".json"):
        chemin_fichier = os.path.join(dossier_output, fichier_json)

        # Lire le fichier JSON
        with open(chemin_fichier, 'r') as fichier:
            donnees_json = json.load(fichier)

        # Vérifier si la prédiction est correcte
        if donnees_json["result"] == donnees_json["ground_truth"]:
            predictions_correctes += 1
        else:
            predictions_incorrectes += 1

# Afficher les résultats
print("Nombre de prédictions correctes :", predictions_correctes)
print("Nombre de prédictions incorrectes :", predictions_incorrectes)
print("Taux de bonnes prédiction : ", round((predictions_correctes / (predictions_correctes + predictions_incorrectes))*100, 2), "%")