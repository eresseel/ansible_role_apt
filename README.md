# ansible_role_apt

## Prepare environment
```bash
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r test-requirements.txt

molecule test (--all|-s <scenario name>)        // mind that there is no scenario named 'default'