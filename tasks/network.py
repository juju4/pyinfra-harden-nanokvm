from pyinfra.operations import files
from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import sysvinit
from pyinfra.facts.server import LinuxDistribution

hardennanokvm_dhcp_enable = False
hardennanokvm_net_ip = "192.168.1.150"
hardennanokvm_netmask = "255.255.255.0"
hardennanokvm_broadcast = "192.168.1.255"
# leave empty to not set a default route
hardennanokvm_gw = ""

files.directory(
    name="Ensure /etc/network exists",
    path="/etc/network",
    mode="0755",
)

netif = files.template(
    name="Configure network interfaces",
    src="templates/interfaces.j2",
    dest="/etc/network/interfaces_test",
    mode="0644",
    user="root",
    group="root",
    hardennanokvm_dhcp_enable=hardennanokvm_dhcp_enable,
    hardennanokvm_net_ip=hardennanokvm_net_ip,
    hardennanokvm_netmask=hardennanokvm_netmask,
    hardennanokvm_broadcast=hardennanokvm_broadcast,
    hardennanokvm_gw=hardennanokvm_gw,
)

if netif.changed and host.get_fact(LinuxDistribution)["name"] == "Buildroot":
    sysvinit.service(
        name="Restart network",
        service="S40network",
        restarted=True,
        enabled=True,
    )

s30eth = host.get_fact(File, path="/etc/init.d/S30eth")

if s30eth:
    files.move(src="/etc/init.d/S30eth", dest="/etc/init.d/DISABLED-S30eth")
