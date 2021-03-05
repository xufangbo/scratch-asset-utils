#!/bin/bash
FROM node:14
MAINTAINER qiushi "qiushi@codingsprite.com"

WORKDIR /home/node/scratch-asset
# COPY ./build /home/node/mouse/build
COPY . /home/node/scratch-asset

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["npm", "run","start"]