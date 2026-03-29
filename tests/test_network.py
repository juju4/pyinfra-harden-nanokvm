def test_netif_file(host):
    netif_f = host.file("/etc/network/interfaces_test")
    assert netif_f.contains("192.168.1.150")
    assert netif_f.user == "root"
    assert netif_f.group == "root"
    assert netif_f.mode == 0o644
