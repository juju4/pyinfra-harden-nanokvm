from pyinfra import host as pyinfra_host
from pyinfra.facts.server import LinuxDistribution


def test_syslog_file(host):
    syslog_f = host.file("/etc/default/syslog")
    if pyinfra_host.get_fact(LinuxDistribution)["name"] == "Buildroot":
        assert syslog_f.contains("-L -R")
        assert syslog_f.user == "root"
        assert syslog_f.group == "root"
        assert syslog_f.mode == 0o644
