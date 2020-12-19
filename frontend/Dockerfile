FROM node:15.4.0-alpine

RUN mkdir /app
WORKDIR /app

COPY package*.json ./

RUN npm install
COPY ./ .
RUN npm run build --verbose
