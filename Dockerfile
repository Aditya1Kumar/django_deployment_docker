FROM python
#ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]

# FROM nginx:1.25
# COPY /code /usr/share/nginx/html
# COPY /static /usr/share/nginx/html

# COPY --from=python /code /usr/share/nginx/html
# # RUN rm /etc/nginx/conf.d/default.conf
# COPY nginx.conf /etc/nginx/conf.d