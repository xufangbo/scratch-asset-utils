mkdir -p ~/log/scratch-asset

yarn build

docker stop scratch-asset
docker rm scratch-asset
docker image rm scratch-asset
docker build -t scratch-asset .
docker run -p 8084:3000 -v ~/log/scratch-asset:/home/node/scratch-asset/logs -v ~/docker/videos:/home/node/scratch-asset/public/video --name scratch-asset -d scratch-asset


# scp -r ./* root@scratch-asset.codingsprite.cn:~/baidu-download/
# http://scratch-asset.codingsprite.cn