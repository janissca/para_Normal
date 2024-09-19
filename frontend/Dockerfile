FROM node:20-alpine
WORKDIR /src
COPY package.json package-lock.json ./
RUN npm install
COPY . ./
CMD npm start