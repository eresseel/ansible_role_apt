# ansible_role_apt

An Ansible Role that installs APT on Linux.

## Prepare developer environment
```bash
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r test-requirements.txt

molecule test (--all|-s <scenario name>)        // mind that there is no scenario named 'default'
```

## Role Variables
Available variables are listed below, along with default values (see defaults/main.yml):

| Variable                | Type    | Default Value | Possible Values                                     |
|-------------------------|---------|---------------| ----------------------------------------------------|
| apt_manage_sources_list | boolean | true          | `true` or `false`                                   |
| apt_focal_repositories  | array   | []            | - name: deb ...                                     |
| apt_repositories        | array   | []            | - name: deb-src...                                  |
| apt_gpg_keys            | array   | []            | - url: https://download.docker.com/gpg <br /> &nbsp;&nbsp;keyring: /etc/apt/keyrings/docker.gpg|
| apt_keys                | array   | []            | - keyserver: keyserver.ubuntu.com <br /> &nbsp;&nbsp;id: 7EA0A9C3F273FCD8                 |
| apt_deb_install         | array   | []            | - url: https://download...                          |
| apt_install             | array   | []            | - name: mc                                          |
| apt_remove              | array   | []            | - name: ncdu                                        |
| apt_remove_purge        | boolean | true          | `true` or `false`                                   |

## Variables example

```yaml
apt_manage_sources_list: true
    apt_remove_purge: true
    apt_keys:
      - keyserver: keyserver.ubuntu.com
        id: 7EA0A9C3F273FCD8
    apt_repositories:
      - repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    apt_gpg_keys:
      - url: https://download.docker.com/linux/ubuntu/gpg
        keyring: /etc/apt/keyrings/docker.gpg
    apt_deb_install:
      - url: https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
    apt_install:
      - name: mc
    apt_remove:
      - name: ncdu
```