from pyinfra.operations import files
from pyinfra import host
from pyinfra.facts.files import File
from io import StringIO
from pyinfra.facts.server import LinuxDistribution

hardennanokvm_fw_dnsservers = [
    "1.1.1.1",
    "8.8.8.8",
    "9.9.9.9",
]

template = StringIO("""
{% for host in hardennanokvm_fw_dnsservers %}
nameserver {{ host }}
{% endfor %}
""")

resolv_status = host.get_fact(File, path="/boot/resolv.conf")

if resolv_status:
    dns = files.template(
        name="Configure dns nameservers",
        src=template,
        dest="/boot/resolv.conf",
        mode="0644",
        user="root",
        group="root",
        hardennanokvm_fw_dnsservers=hardennanokvm_fw_dnsservers,
    )

    if dns.changed and host.get_fact(LinuxDistribution)["name"] == "Buildroot":
        files.copy(
            name="Mirror /boot/resolv.conf to /etc/resolv.conf",
            src="/boot/resolv.conf",
            dest="/boot/resolv.conf",
            # TypeError: got an unexpected keyword argument 'mode'
            # mode="0644",
            # TypeError: got an unexpected keyword argument 'user'
            # user="root",
            # group="root",
        )
