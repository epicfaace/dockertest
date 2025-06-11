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
    kwargs = {"network": network} if network else {}
    output = client.containers.run("alpine", "ping -c 1 google.com", **kwargs)
    print(f"done. output is <{output.decode()}>")
    print("")

run_ping(None)
run_ping("external_network")
run_ping("internal_network")
