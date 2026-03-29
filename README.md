# Pyinfra nanokvm hardening

[![Actions Status - Main](https://github.com/juju4/pyinfra-harden-nanokvm/workflows/AnsibleCI/badge.svg)](https://github.com/juju4/pyinfra-harden-nanokvm/actions?query=branch%3Amain)
[![Actions Status - Devel](https://github.com/juju4/pyinfra-harden-nanokvm/workflows/AnsibleCI/badge.svg?branch=devel)](https://github.com/juju4/pyinfra-harden-nanokvm/actions?query=branch%3Adevel)

This is an adaptation of my ansible role [harden_nanokvm](https://github.com/juju4/ansible-harden-nanokvm/) to pyinfra.

It does system hardening on [NanoKVM](https://github.com/sipeed/NanoKVM/). Mostly

* Firewall enforcing restricted network traffic
* Configure custom DNS server
* Configure more restricted ssh config
* Set syslog logging to higher retention (default 10MB rotate 10 times instead of 200KB rotate once)

## Requirements & Dependencies

### Pyinfra

It was tested on the following versions:

* 3.6

### Operating systems

Tested on NanoKVM 2.3.

## Example Playbook

```shell
pyinfra inventory.py nanokvm_deploy.py -y
```

## ## Continuous integration

Using pytest-testinfra

```shell
pytest --hosts='ssh://testhost' tests/test_*.py
```

## Troubleshooting & Known issues

TBD

## Resources

* nameserver <https://github.com/sipeed/NanoKVM/issues/210> <https://github.com/sipeed/NanoKVM/issues/399> <https://github.com/sipeed/NanoKVM/issues/311#issuecomment-2658954062>
* firewall <https://github.com/sipeed/NanoKVM/issues/301#issuecomment-3172900815>

## License

BSD 2-clause
