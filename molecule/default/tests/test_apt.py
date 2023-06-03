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
    assert host.file("/etc/apt/sources.list").exists is True


def test_other_sources_list_exists(host):
    assert host.file("/etc/apt/sources.list.d/archive_ubuntu_com_ubuntu.list")\
        .exists is False
