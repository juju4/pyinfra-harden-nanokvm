from pyinfra.operations import files

hardennanokvm_env = []
hardenanokvm_backup = True

if hardennanokvm_env:
    files.block(
        name="Custom /etc/environment",
        path="/etc/environment",
        content=hardennanokvm_env,
        backup=hardenanokvm_backup,
    )
