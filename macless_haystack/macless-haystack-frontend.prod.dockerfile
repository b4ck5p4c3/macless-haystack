FROM ghcr.io/cirruslabs/flutter:3.19.6 AS build-env

# Copy files to container and build
COPY . /app
WORKDIR /app

# RUN ls; sleep 10
RUN flutter build web

# Stage 2 - Create the run-time image
FROM nginx:1.21.1-alpine
COPY --from=build-env /app/build/web /usr/share/nginx/html
