# Exercise 3

## Instructions

- Build: docker-compose up -d --build
- Browse:
http://localhost:8997/, http://localhost:8998/, http://localhost:8999/
- Stop: docker-compose down

### Bibliography

https://stackoverflow.com/questions/50705838/docker-compose-with-nginx-keeps-displaying-welcome-page

docker run --rm -d -p 80:80 --name my-nginx nginx

docker exec -it my-nginx bash
cd /etc/nginx/
cat nginx.conf

cd /etc/nginx/conf.d/
