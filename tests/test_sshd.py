def test_sshdconf_file(host):
    with host.sudo():
        sshdconf_f = host.file("/etc/ssh/sshd_config")
        assert sshdconf_f.contains("OpenBSD: sshd_config,")
        assert sshdconf_f.contains("AllowAgentForwarding no")
        assert sshdconf_f.user == "root"
        assert sshdconf_f.group == "root"
        assert sshdconf_f.mode == 0o600
