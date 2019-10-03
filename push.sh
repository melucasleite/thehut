git push
rm jobs.sqlite
docker build -t melucasleite/thehut:latest .
docker push melucasleite/thehut:latest
