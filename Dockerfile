FROM python:3
ADD mem_disk.py /
RUN pip3 install psutil

CMD [ "python", "./mem_disk.py" ]
