# ansible

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/codeyourinfra/ansible.svg)](https://github.com/codeyourinfra/ansible/releases/latest) [![Build status](https://travis-ci.org/codeyourinfra/ansible.svg?branch=master)](https://travis-ci.org/codeyourinfra/ansible) [![Ansible Role](https://img.shields.io/ansible/role/30166.svg)](https://galaxy.ansible.com/codeyourinfra/ansible) [![Ansible Role downloads](https://img.shields.io/ansible/role/d/30166.svg)](https://galaxy.ansible.com/codeyourinfra/ansible)

Ansible role to install [Ansible](https://www.ansible.com).

## Example Playbook

```yml
---
- hosts: servers
  roles:
    - codeyourinfra.ansible
```

The role requires the *ansible_python_version* variable, obtained through the [gathering facts phase](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#information-discovered-from-systems-facts). So please don't turn off facts.

## Build process

The build process is performed in [Travis CI](https://travis-ci.org/codeyourinfra/ansible). During the build, the role is tested by using [Molecule](https://molecule.readthedocs.io).

## Test yourself

Inside your [Python virtual environment](https://docs.python.org/3/tutorial/venv.html), run:

`pip install -r requirements.txt`

And then:

`molecule test`

## Author Information

[@gustavomcarmo](https://github.com/gustavomcarmo) is a contributor of [Codeyourinfra](https://github.com/codeyourinfra). Get on board too! :)
