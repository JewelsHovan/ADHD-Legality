from dotenv import load_dotenv
import os

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

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
    "United States",
    "United Kingdom",
    "Canada",
    "Australia",
    "Japan",
    # Add more countries as needed
] 