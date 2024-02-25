# containerized-keras-nn

- [Kaggle Dataset](https://leonardofurnielis.medium.com/criando-modelos-de-machine-learning-com-ibm-watson-studio-1-de-2-35d012f8eec)

## Table of Contents

- Developing locally
  - [Native runtime](#native-runtime)
  - [Containerized](#containerized)

## Native runtime

To run this code in your computer execute the following commands into project root directory

```bash
cd <directory to store your Python environment>
python -m venv <your-venv-name>

source <your-venv-name>/bin/activate

$ pip install --no-cache-dir -r requirements.txt
```

#### Dectivate your Python virtual environment

If you need to change to a different environment, you can deactivate your current environment using the command below:

```bash
deactivate
```

## Containerized

To run this code using Docker container execute the following commands into project root directory

```bash
$ docker build -t containerized-keras-nn .
$ docker run -p 8080:8080 -d containerized-keras-nn
```
