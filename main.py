"""
docker pull alpine
pip3 install -r requirements.txt
python3 main.py
"""

import docker
client = docker.from_env()
client.networks.prune()
client.networks.create("internal_network", internal=True)
client.networks.create("external_network", internal=False)


def run_ping(network):
    print(f"starting docker container with network {network}...")
    output = client.containers.run("alpine", "echo hello", network=network)
    print(f"done. output is <{output.decode()}>")
    print("")

run_ping("external_network")
run_ping("internal_network")