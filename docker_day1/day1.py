# === Day1 Ideas covered ===

"""

1. dev env deployment - ** docker **
2. dev env - ** docker-compose **
3. dev env integration - ** docker-compose **
4. dev tool - for this static site we use ** pycco ** to generate html
5. delivery  - we publish the html site to ** aws s3 **
6. version ctrl - ** github **, we might use aws CodeCommit, etc

"""

# === Day1 Section 1 ===

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
                            -t tag      # add tag as image name
    docker run
                            -p 8080:80  # mapping container 80 to host 8080
                            -d          # run detached
                            --name      # container name

"""
use docker-compose to build and run
"""

    docker-compose up --build -d
                        --build         # build if no container
                        --no-recreate   # if there is container, do not recreate it

    open http://localhost:8080          # local test


# === Day1 Section 2 ===

"""
docker-compose

if not specify image it will use <project>_<service> as container name

with already built image, you can remove [build] from docker-compose.yml
add the specified image and container name

    image: my_custom_nginx_image
    container_name: nginx

"""
    docker image image_id tag image_name
    docker-compose up -d

# === Day1 Section 3 ===

"""
1. ** docker ** - use docker cmd to clean up
2. ** docker-compose ** - stop and/or cleanup
"""

    docker container rm container_name
    docker image rm image_name
                            -f      # force
    docker image prune              # remove unused images
    docker images

    docker-compose ps
    docker-compose stop
                            stop    # stop all containers
                            rm -f   # remove all containers
    docker-compose down --rmi all
                            down    # stop and remove containers networks, volumes and images

    docker-compose up -d


# === Day1 Section 4 ===

"""
generate document from pyfile
"""
    pip install pycco
    pycco docker_day1/*.py -d html_output -p -i
                            -p  # preservce path
                            -d  # output directory
                            -i  # generate index
    # local test
    python -m http.server 8000      


# === Day1 Section 5 ===

"""
use aws s3 to host the site

* currently use google domain 301 redirect to serve the files

1. [aws_website-policy.json][policy]
2. [aws_website.json][website]

[policy]: http://2018-test-bucket-andydocket.s3-website.us-west-1.amazonaws.com/assets/aws_website-policy.json
[website]: http://2018-test-bucket-andydocket.s3-website.us-west-1.amazonaws.com/assets/aws_website.json

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


# === Day1 Section 6 ===

"""
sync with github
"""

git remote add github git@github.com:arbeitandy/mywaytoday.git
git pull github master --allow-unrelated-histories

git push github master --all


"""
made by [Pycco][pycco]

[Home][home]

[pycco]: https://pycco-docs.github.io/pycco/
[home]: http://d.fogtown.us/
"""
