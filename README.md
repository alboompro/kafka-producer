# Cron Kafka Producer
## Simple kafka producer 

This software built specific on purpose to produce message to topic in schedule

## Plugins

| Name | Description |
| ------ | ------ |
| KAFKA_BOOSTRAP_SERVER | Kafka boostrap server |
| KAFKA_TOPIC | Topic name |
| KAFKA_MESSAGE_KEY | Message key in string |
| KAFKA_MESSAGE_VALUE | Message payload in string |


## Docker
*Note: This docker image design to run as cronjob on kubernetes, When it finish the container will exit
```sh
docker pull alboom/kafka-producer:latest

# Using ENVs
docker run -e ENV=VALUE alboom/kafka-producer

# Extra argv
docker run -e ENV=VALUE alboom/kafka-producer python app.py {"asd":321}
```

## Kubernetes CronJob

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: cronjob-name
  
spec:
  schedule: 0 0 * * *
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: cronjob-name
              image: alboom/kafka-producer:latest
              args:
                - "$(date +%F)"
              env:
                - name: KAFKA_BOOSTRAP_SERVER
                  valueFrom:
                    secretKeyRef:
                      name: secret-name
                      key: SECRET_KEY_KAFKA_HOSTS
                - name: KAFKA_TOPIC
                  value: topic.name
                - name: KAFKA_MESSAGE_KEY
                  value: $(HOSTNAME)
              imagePullPolicy: Always
          restartPolicy: OnFailure
          terminationGracePeriodSeconds: 30
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
```

## License

Apache 2.0