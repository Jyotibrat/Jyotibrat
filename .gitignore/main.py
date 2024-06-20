import requests
from datetime import datetime

GITHUB_API = "https://api.github.com"
USER = "Jyotibrat"
TOKEN = "ACTIONS_PAT"

def get_repos():
    url = f"{GITHUB_API}/users/{USER}/repos"
    response = requests.get(url, auth=(USER, TOKEN))
    return response.json()

def generate_metrics(repos):
    # Generate your metrics content here
    pass

if __name__ == "__main__":
    repos = get_repos()
    generate_metrics(repos)
    # Save to github-metrics.svg
