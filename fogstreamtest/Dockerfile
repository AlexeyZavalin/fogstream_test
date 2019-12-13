FROM python:3
RUN mkdir test_fogstream/
COPY requirements.txt test_fogstream/
WORKDIR /test_fogstream/
RUN pip install -r requirements.txt
ADD . /test_fogstream/
