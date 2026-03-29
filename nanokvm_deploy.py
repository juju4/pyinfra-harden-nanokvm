from pyinfra import local

local.include("tasks/dns.py")
local.include("tasks/environment.py")
local.include("tasks/firewall.py")
local.include("tasks/logging.py")
local.include("tasks/network.py")
local.include("tasks/sshd.py")
