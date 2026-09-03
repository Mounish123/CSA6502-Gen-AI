import os
from pathlib import Path
from dotenv import load_dotenv


# ---------------------------------------------------------
# PROJECT DIRECTORY
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------
# LOAD .ENV FROM PROJECT ROOT
# ---------------------------------------------------------
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE, override=True)


# ---------------------------------------------------------
# APPLICATION INFORMATION
# ---------------------------------------------------------
APP_NAME = "🌿 Crop Disease Diagnosis System"

APP_TITLE = "🤖 Generative AI System for Crop Disease Diagnosis and Localized Treatment Recommendation"

VERSION = "Version 1.0"

AUTHOR = "A. Mounish"

COLLEGE = "Computer Science & Engineering (AI)"


DESCRIPTION = """
This application detects crop diseases using AI-powered image analysis,
farmer voice queries, and Multimodal Large Language Models.

It provides localized treatment recommendations in multiple languages.
"""


# ---------------------------------------------------------
# GEMINI API KEY
# ---------------------------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()


# ---------------------------------------------------------
# CHECK API KEY
# ---------------------------------------------------------
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please configure it in the .env file."
    )