import requests

def fetch_jobs():
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        jobs = response.json()[1:]  # Skip metadata

        devops_jobs = [
            job for job in jobs
            if "devops" in job.get("position", "").lower()
        ]

        return devops_jobs[:5]  # Top 5 jobs
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []

if __name__ == "__main__":
    for job in fetch_jobs():
        print(f"{job['company']} - {job['position']}\n{job['url']}\n")

