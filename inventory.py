# Define a group as a list of hosts
# details in ssh_config
my_hosts = [
    ("testhost", {"ssh_user": "deploy", "ssh_key": "~/.ssh/id_ed25519", "_sudo": True})
]
