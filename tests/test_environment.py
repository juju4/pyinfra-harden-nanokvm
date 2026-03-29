def test_env_file(host):
    env_f = host.file("/etc/environment")
    assert env_f.user == "root"
    assert env_f.group == "root"
    assert env_f.mode == 0o644
