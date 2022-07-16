FROM nikolaik/python-nodejs:python3.10-nodejs16-slim
COPY . /app
WORKDIR /app/frontend
RUN yarn install && yarn build
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x ./upgrade_migrations.sh
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]