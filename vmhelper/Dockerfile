FROM python:3.7-alpine
WORKDIR /vmhelper
ADD . /vmhelper
ENV NAME vmhelper
# install gcc
RUN apk add --no-cache gcc musl-dev
# install python pack
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python","./main.py"]