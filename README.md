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

## Build process

The build process is performed in [Travis CI](https://travis-ci.org/codeyourinfra/ansible). During the build, the role is tested by using [Ubuntu Docker images with Python 3](https://hub.docker.com/r/codeyourinfra/python3).

## Author Information

[@gustavomcarmo](https://github.com/gustavomcarmo) is a contributor of [Codeyourinfra](https://github.com/codeyourinfra). Get on board too! :)
