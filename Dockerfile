FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV PROJECT_DIR="oc_lettings_site"
RUN mkdir $PROJECT_DIR
COPY . $PROJECT_DIR
WORKDIR $PROJECT_DIR
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
