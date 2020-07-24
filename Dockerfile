FROM python:3
ADD mem_disk.py /
RUN pip3 install psutil
RUN  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
CMD [ "python", "./mem_disk.py" ]
