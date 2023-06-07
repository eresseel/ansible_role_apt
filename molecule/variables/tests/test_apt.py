# """
# Testing Ansible Role APT
# """
import os
import testinfra
from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).\
        get_hosts('ubuntu-focal-ansible-apt-role')


def ansible_ip():
    host = testinfra.\
        get_host("docker://root@ubuntu-focal-ansible-apt-role", sudo=True)
    ansible_address = host.addr("ubuntu-focal-ansible-apt-role").ipv4_addresses
    return ansible_address[0]


def test_sources_list_removed(host):
    assert host.file("/etc/apt/sources.list").exists is False


def test_key_is_added(host):
    cmd = host.run("apt-key --keyring /etc/apt/trusted.gpg list | grep '9DC8'")
    assert cmd.rc == 0


def test_package_is_installed(host):
    packages = ["teamviewer", "mc", "docker-ce"]
    for item in packages:
        package = host.package(item)
        assert package.is_installed


def test_ncdu_is_not_installed(host):
    ncdu = host.package("ncdu")
    assert ncdu.is_installed is False
