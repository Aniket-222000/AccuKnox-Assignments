# Use alpine with bash for simple shell script app
FROM alpine:3.18

# Install dependencies used by wisecow (fortune, cowsay, and socat for simple TCP server)
RUN apk add --no-cache bash fortune cowsay socat

# Create app directory and copy the repo files (assumes wisecow.sh is present in repo root)
WORKDIR /app
COPY . /app
RUN chmod +x /app/wisecow.sh

# Expose the default port used by the upstream repo (4499)
EXPOSE 4499

# Entrypoint runs the provided script
CMD ["/app/wisecow.sh"]
