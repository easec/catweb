# Basavspegling
FROM python:3.4-alpine
LABEL maintainer="<din_e-postadress>"

# Installera Pythonmoduler
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r
/usr/src/app/requirements.txt

# Kopiera filer
COPY app.py /usr/src/app/
COPY templates/index.html
/usr/src/app/templates/

# Exponering av port f app
EXPOSE 5000

# Starta app
CMD ["python3", "/usr/src/app/app.py"] 

