# Ombi Requests Cleaner
Docker container running python which remove Ombi requests for movies no longer availible. Run as a cron job or edit to add a sleep timer (time.sleep(seconds)) to run ever x hours (and add restart if stopped setting to always run).

Docker Run Script
```
(in the directory of the Dockerfile and Python file)
docker build -t ombicleaner:latest .
```
```
docker create \
  --name=ombicleaner \
  -v /path/to/files:/ombi
  ombicleaner:latest
```
