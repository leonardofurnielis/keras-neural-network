# neural-network-openshift

## Table of Contents

- [Local](#local)
- [Docker](#docker)

## Local

To run this code in your computer execute the following commands into project root directory

```bash
$ pip install --no-cache-dir -r requirements.txt
```

## Docker

To run this code using Docker container execute the following commands into project root directory

```bash
$ docker build -t neural-network-openshift .
$ docker run -p 80:80 -d neural-network-openshift
```