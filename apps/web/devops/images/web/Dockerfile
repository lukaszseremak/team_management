# Frontend
FROM node:18-alpine as webapp

ENV LANG=C.UTF-8

# Frontend build
WORKDIR /webapp/apps/web/
COPY package.json yarn.lock /webapp/apps/web/
RUN yarn install
COPY . /webapp/apps/web/
RUN yarn build

# Web server
FROM nginx:alpine

WORKDIR /app/
COPY --from=webapp /webapp/apps/web/build/ /app/public
