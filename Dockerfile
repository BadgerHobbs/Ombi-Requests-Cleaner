FROM python:3

ADD OmbiCleaner.py /

CMD [ "python", "-u", "./OmbiCleaner.py" ]