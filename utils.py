# utils.py

import json
import os
import random
import re
from config import OFFRES_FILE, SCRIPTS_FILE, VIDEOS_FILE, PUBLICATIONS_FILE

def load_json(file_path):
    """📂 Charge un fichier JSON et retourne son contenu."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file_path, data):
    """💾 Sauvegarde des données dans un fichier JSON."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def clean_text(text):
    """🧼 Nettoie le texte brut pour le rendre plus lisible."""
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s.,!?]", "", text)
    return text.strip()

def get_random_color():
    """🎨 Retourne une couleur aléatoire pour les visuels."""
    colors = ["#FF5733", "#33FFBD", "#335BFF", "#FF33A8", "#8D33FF"]
    return random.choice(colors)

def get_random_background():
    """🖼️ Retourne un style de fond aléatoire."""
    styles = ["gradient-blue", "gradient-purple", "solid-black", "solid-white"]
    return random.choice(styles)

def get_random_font():
    """🔤 Retourne une police aléatoire."""
    fonts = ["Montserrat Bold", "Roboto Mono", "Lato Black", "Oswald"]
    return random.choice(fonts)

def append_to_json(file_path, new_entry):
    """📌 Ajoute une entrée à un fichier JSON existant."""
    data = load_json(file_path)
    data.append(new_entry)
    save_json(file_path, data)

def get_latest_entries(file_path, limit=5):
    """🕵️ Retourne les dernières entrées d’un fichier JSON."""
    data = load_json(file_path)
    return data[-limit:] if len(data) >= limit else data
  
