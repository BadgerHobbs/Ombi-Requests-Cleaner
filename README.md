# Ombi Requests Cleaner
Docker container running python which remove Ombi requests for movies no longer availible. Run as a cron job or uncomment and set the sleep timer in the .py file to run every x seconds.

Docker Run Script
```
(in the directory of the Dockerfile and Python file)
docker build -t ombicleaner:latest .
```
```
docker create \
  --name=ombicleaner \
  -v /path/to/files:/ombi
  --restart unless-stopped \ # Include if not running as cron job
  ombicleaner:latest
```
