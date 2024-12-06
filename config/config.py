from dotenv import load_dotenv
import os

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Model
MODEL = "gpt-4o-mini"

# List of ADHD medications to search for
ADHD_MEDICATIONS = [
    "Adderall",
    "Ritalin",
    "Concerta",
    "Vyvanse",
    "Strattera"
]

# List of countries to research
TARGET_COUNTRIES = [
    "Australia", "Austria", "Belgium", "Canada", "Chile", "Colombia", "Costa Rica",
    "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany",
    "Greece", "Hungary", "Iceland", "Ireland", "Israel", "Italy", "Japan",
    "Korea", "Latvia", "Lithuania", "Luxembourg", "Mexico", "Netherlands",
    "New Zealand", "Norway", "Poland", "Portugal", "Slovak Republic", "Slovenia",
    "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", "United States"
]