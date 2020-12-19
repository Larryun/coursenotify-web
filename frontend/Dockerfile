FROM node:15.4.0-alpine

RUN mkdir /app
RUN mkdir /app/static

WORKDIR /app
COPY package*.json ./

RUN npm install
COPY ./ .
COPY ./.env.production .
RUN npm run build --verbose
