def test_resolvconf_file(host):
    resolv_f= host.file("/boot/resolv.conf")
    assert resolv_f.contains("1.1.1.1")
    assert resolv_f.user == "root"
    assert resolv_f.mode == 0o644
