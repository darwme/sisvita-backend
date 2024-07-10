FROM node:latest
RUN mkdir -p /home/app
COPY . /home/app
EXPOSE 3000
WORKDIR "/home/app/src"
CMD ["npm","install"]
CMD ["node","/home/app/src/index.js"]