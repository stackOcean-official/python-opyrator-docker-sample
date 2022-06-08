# python-opyrator-docker-sample

Sample Deployment of a Python Machine-Learning Model using Docker

## How to setup

Create a new venv (virtual environment):

```
python3 -m venv .venv
```

Activate new environment:

```
source .venv/bin/activate
```

Install packages:

```
pip install -r requirements.txt
```

## Run the streamlit app

```
python3 -m streamlit run src/streamlit.py
```

## How to build & run the Docker Image

```
docker build -t python-docker-sample .
```

Run the Docker Image with:

```
docker run -d --rm -p 8501:8501 --name python-docker-sample python-docker-sample
```

To view the logs of the container run:

```
docker logs python-docker-sample
```

To stop the container run:

```
docker stop python-docker-sample
```
