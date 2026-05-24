def test_syslog_file(host):
    syslog_f = host.file("/etc/default/syslog")
    distro = host.system_info.distribution
    if distro == "buildroot":
        assert syslog_f.contains("-L -R")
        assert syslog_f.user == "root"
        assert syslog_f.group == "root"
        assert syslog_f.mode == 0o644
