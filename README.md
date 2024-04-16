# ct-iot-things-report-job-service

Description
The things-report-job-service consumes messages from job-queue and generates report job csv files, then places an archive job onto the job-archive-queue.

Diagrams

Run
make server-start
Test
make test
Deployment
Must be deployed after things-service and things report job queue.