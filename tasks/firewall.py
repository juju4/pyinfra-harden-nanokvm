from pyinfra.operations import files, server

hardennanokvm_fw_template_v4 = "templates/rules.v4.j2"
hardennanokvm_fw_template_v6 = "templates/rules.v6.j2"

files.directory(
    name="Ensure /etc/iptables exists",
    path="/etc/iptables",
    mode="0755",
    user="root",
    group="root",
)

fw4 = files.template(
    name="Iptables configuration file update",
    src=hardennanokvm_fw_template_v4,
    dest="/etc/iptables.conf",
    mode="0644",
    user="root",
    group="root",
    hardennanokvm_fw_default="ACCEPT",
    hardennanokvm_network="192.168.1.0",
    hardennanokvm_prefix="24",
    hardennanokvm_netmask="255.255.255.0",
    hardennanokvm_broadcast="192.168.1.255",
    hardennanokvm_fw_systemupdates_allow=True,
    hardennanokvm_fw_https_out_allow=True,
)

if fw4.changed:
    server.shell(
        name="Ensure iptables v4 rules are correct",
        commands=["iptables-restore -tv < /etc/iptables.conf"],
    )
    server.shell(
        name="Restore iptables v4 rules",
        commands=["iptables-restore < /etc/iptables.conf"],
    )

fw6 = files.template(
    name="Ip6tables configuration file update",
    src=hardennanokvm_fw_template_v6,
    dest="/etc/ip6tables.conf",
    mode="0644",
    user="root",
    group="root",
    hardennanokvm_fw6_default="ACCEPT",
    hardennanokvm_fw_systemupdates_allow=True,
    hardennanokvm_fw_https_out_allow=True,
)

if fw6.changed:
    server.shell(
        name="Ensure iptables v6 rules are correct",
        commands=["ip6tables-restore -tv < /etc/ip6tables.conf"],
    )
    server.shell(
        name="Restore iptables v6 rules",
        commands=["ip6tables-restore < /etc/ip6tables.conf"],
    )

# No patch task https://github.com/pyinfra-dev/pyinfra/issues/877
