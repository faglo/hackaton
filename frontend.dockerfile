FROM node:16-slim as compole-image

COPY ./frontend /frontend
WORKDIR /frontend
RUN yarn install
RUN yarn build

FROM node:16-slim as build-image
COPY --from=compole-image /frontend/dist /frontend

RUN npm install -g http-server

WORKDIR /frontend
CMD [ "http-server", "-o", "--cors", "--port", "8000" ]