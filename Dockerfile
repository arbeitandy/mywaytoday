FROM nginx:1.15-alpine
RUN rm -rf /usr/share/nginx/html
COPY html_output /usr/share/nginx/html
COPY assets /usr/share/nginx/html/assets
