
# === hour 1 day 1 ===

"""
minimal Dockerfile nginx alpine
"""

    # Dockerfile
    FROM nginx:1.15-alpine
    RUN rm -rf /usr/share/nginx/html
    COPY output /usr/share/nginx/html

"""
run command
src: https://hub.docker.com/_/nginx/
"""

    docker build -t static-nginx .
    docker run --name day1 -d -p 8080:80 static-nginx
    docker stop day1
  
    docker build
        -t tag
    docker run
        -p mapping container 80 to host 8080
        -d run detached

"""
use docker-compose to build and run
"""

    docker-compose up --build -d
        --build if no container
        --no-recreate if there is container, do not recreate it

    open http://localhost:8080


# === hour 2 day 1 ===

"""
docker-compose
if not specify image it will use <project>_<service> as container name
"""

    docker-compose container name <project>_<service>
    docker-compose --project-name foo build bar
    docker images foo_bar

"""
with already built image, you can remove [build] from docker-compose.yml
add the specified image and container name
    image: my_custom_nginx_image
    container_name: nginx

"""

# === hour 3 day 1 ===

"""
1. ** docker ** - use docker cmd to clean up
2. ** docker-compose ** - stop and/or cleanup
"""
    docker container rm container_name
    docker image rm image_name
        -f force
    docker image prune                  # remove unused images
    docker images

    docker-compose ps
    docker-compose stop
        stop    # stop all containers
        rm -f   # remove all containers
    docker-compose down --rmi all
        down    # stop and remove containers networks, volumes and images

    docker-compose up -d


# === hour 4 day 1 ===

"""
generate document from pyfile
"""
    pip install pycco
    pycco docker_day1/*.py -d html_output -p -i
        -p  # preservce path
        -d  # output directory
        -i  # generate index
    python -m http.server 8000      # test

# === hour 5 day 1 ===

"""
use aws s3 to host the site

* currently use google domain 301 redirect to serve the files

1. [aws_website-policy.json][policy]
2. [aws_website.json][website]

[policy]: assets/aws_website-policy.json
[website]: assets/aws_website-policy.json

"""

* init

aws s3 mb s3://2018-test-bucket-andydocket
aws s3api put-bucket-policy --bucket 2018-test-bucket-andydocket \
    --policy file://assets/aws_website-policy.json
aws s3api put-bucket-website --bucket 2018-test-bucket-andydocket \
    --website-configuration file://assets/aws_website.json

* update

aws s3 sync html_output/ s3://2018-test-bucket-andydocket
aws s3 sync assets s3://2018-test-bucket-andydocket/assets

"""
# === hour 6 day 1 ===
sync with github

git remote add github git@github.com:arbeitandy/mywaytoday.git
git pull github master --allow-unrelated-histories

git push github master --all

"""
"""
made by [Pycco][pycco]

[Home][home]

[pycco]: https://pycco-docs.github.io/pycco/
[home]: http://d.fogtown.us/
"""


