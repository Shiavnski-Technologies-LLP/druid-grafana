import requests
import json

# Druid Coordinator URL
druid_url = "http://localhost:8081/druid/indexer/v1/task"

# Load the ingestion spec
with open("csv_ingestion_task.json", "r") as f:
    ingestion_spec = json.load(f)

# Send ingestion request
response = requests.post(druid_url, json=ingestion_spec)

print("Response:", response.status_code, response.text)
