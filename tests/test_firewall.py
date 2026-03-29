def test_fwrules_file(host):
    fwrules_f = host.file("/etc/iptables.conf")
    assert fwrules_f.contains("192.168.1.0")
    assert fwrules_f.user == "root"
    assert fwrules_f.group == "root"
    assert fwrules_f.mode == 0o644
