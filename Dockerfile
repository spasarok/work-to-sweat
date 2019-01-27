FROM python:3.7.2-slim-stretch
ENV PYTHONPATH /pythonpath

RUN echo hi

COPY ./requirements.txt /build/requirements.txt
RUN pip install -r /build/requirements.txt && rm -r /build
COPY api /pythonpath/api

#CMD tail -f /dev/null

CMD python -m api.main
