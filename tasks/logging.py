from pyinfra import host
from pyinfra.operations import files
from pyinfra.facts.server import LinuxDistribution
from pyinfra.operations import sysvinit

hardennanokvm_syslog_size = 10240
hardennanokvm_syslog_rotate = 10
# remote syslog
hardennanokvm_syslog_server = ""
syslogd_args = f"-s {hardennanokvm_syslog_size} -b {hardennanokvm_syslog_rotate}"
if len(hardennanokvm_syslog_server) > 0:
    syslogd_args += f"-L -R {hardennanokvm_syslog_server}"


if host.get_fact(LinuxDistribution)["name"] == "Buildroot":
    files.file(
        name="Ensure /etc/init.d/S01syslogd permissions",
        path="/etc/init.d/S01syslogd",
        mode="755",
        # user="root",
        # group="root",
    )

    syslog = files.line(
        name="Configure busybox syslogd",
        path="/etc/default/syslogd",
        line='^SYSLOGD_ARGS=".*"',
        replace=f'SYSLOGD_ARGS="{syslogd_args}"',
        present=False,
    )

    if syslog.changed:
        sysvinit.service(
            name="Restart and enable rsyslog",
            service="syslogd",
            restarted=True,
            enabled=True,
        )
