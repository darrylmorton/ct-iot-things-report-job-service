# ct-iot-things-report-job-service

## Description

The `things-report-job-service` consumes messages from `job-queue` and generates `report job csv files`,  
then places an `archive job message` onto the `job-archive-queue`.

[Diagrams](./docs/DIAGRAMS.md)

## Requirements

python v3.12+  
poetry v1.7.1
[thing-service](https://github.com/darrylmorton/ct-iot-thing-service) (for running tests only)

## Run

```
make server-start
```

## Test

Use the `thing-service` repo to run the database container, with migrate and seed npm run scripts:

```
docker-compose up -d

npm run test:migrate
npm run test:seed
```

### Run Tests
```
make test
```

## Deployment

Must be deployed **after** `things-service`,  `things report job queue` and ` things report archive job queue`.