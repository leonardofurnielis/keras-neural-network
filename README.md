# python-neural-network

- [Kaggle Dataset](https://leonardofurnielis.medium.com/criando-modelos-de-machine-learning-com-ibm-watson-studio-1-de-2-35d012f8eec)
- [Implementing with Red Hat OpenShift](https://leonardofurnielis.medium.com/implemente-uma-api-de-rede-neural-com-python-no-red-hat-openshift-6c3eb9ecaedf) (portuguese-Brazil)


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
$ docker build -t python-neural-network .
$ docker run -p 8080:8080 -d python-neural-network
```
