# config.py

import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# 🔐 Clés API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 📁 Chemins des fichiers
DATA_DIR = "data"
OFFRES_FILE = os.path.join(DATA_DIR, "offres.json")
SCRIPTS_FILE = os.path.join(DATA_DIR, "scripts_tiktok.json")
VIDEOS_FILE = os.path.join(DATA_DIR, "videos.json")
PUBLICATIONS_FILE = os.path.join(DATA_DIR, "publications.json")

# 🔍 Paramètres de scraping
DEFAULT_QUERY = "Développeur Web"
DEFAULT_LOCATION = "Montréal"
MAX_RESULTS_PER_SITE = 5

# 🎥 Paramètres vidéo
VIDEO_FORMAT = "9:16"
FONT_STYLE = "Montserrat Bold"
BACKGROUND_STYLE = "gradient-blue"

# 📲 Plateformes cibles
PLATFORMS = ["TikTok", "Instagram", "YouTube Shorts"]
