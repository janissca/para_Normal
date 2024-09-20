FROM node:20-alpine
WORKDIR /src
COPY package*.json ./
RUN npm install
COPY . .
CMD ["node", "app.js"]