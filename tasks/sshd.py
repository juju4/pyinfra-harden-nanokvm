from pyinfra.operations import files
from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import sysvinit

harden_sshd_port = 22
harden_sshd_listen = "0.0.0.0"

sshd_config = files.template(
    name="Configure sshd_config",
    src="templates/sshd_config.j2",
    dest="/etc/ssh/sshd_config",
    mode="0600",
    user="root",
    group="root",
    harden_sshd_port=harden_sshd_port,
    harden_sshd_listen=harden_sshd_listen,
)

if sshd_config.changed and host.get_fact(LinuxDistribution)["name"] == "Buildroot":
    sysvinit.service(
        name="Restart sshd",
        service="S50sshd",
        restarted=True,
        enabled=True,
    )
