# desc-pic-verification-ms
## How to run
1. Build flask image using command `docker build -t web_images .`
2. Execute docker compose using command `docker-compose up -d`
3. Execute migrations using command `docker-compose exec web_images flask db upgrade`