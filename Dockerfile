FROM continuumio/miniconda3

WORKDIR /app

RUN mkdir -p src
RUN mkdir -p data
RUN mkdir -p output

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "python-sample", "/bin/bash", "-c"]

# The code to run when container is started:
ADD python/src /app/src

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "python-sample", "python", "src/predict.py"]