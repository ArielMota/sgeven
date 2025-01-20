FROM python:3.11-slim
WORKDIR /core
COPY requirements.txt /core/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /core/
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py create_admin_user || exit 1 && python manage.py runserver 0.0.0.0:8000"]
