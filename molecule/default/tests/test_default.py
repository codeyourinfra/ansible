import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ansible_is_installed(host):
    cmd = host.run("ansible --version")
    assert cmd.rc == 0
    pattern = re.compile("^ansible [\\d.]+")
    assert pattern.match(cmd.stdout)
