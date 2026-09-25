import os, yaml, requests
from common import generate_token

PLATFORMS = {
    'daint': 'hpc',
    'eiger': 'hpc',
    'clariden': 'ml',
    'bristen': 'ml',
    'santis': 'cw',
}

with open(os.path.join(os.path.dirname(__file__), 'config.yaml')) as f:
    config = yaml.safe_load(f)

cluster = config['cluster']
platform = PLATFORMS.get(cluster)

token = generate_token(config)
r = requests.get(
    f"https://api.cscs.ch/{platform}/firecrest/v2/status/{config['cluster']}/userinfo",
    headers={'Authorization': f'Bearer {token}'},
)
print(r.status_code, r.text)