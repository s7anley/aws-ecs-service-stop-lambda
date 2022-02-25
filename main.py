import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
client = boto3.client('ecs')


def restart_service(event, context):
    # Process own expected event
    cluster = event["cluster"]
    service_name = event["service_name"]

    logger.info("Starting restart of {0} service in {1} cluster".format(service_name, cluster))
    response = client.list_tasks(cluster=cluster, serviceName=service_name)
    tasks = response.get('taskArns', [])
    logger.info("Service is running {0} underlying tasks".format(len(tasks)))
    for task in tasks:
        logger.info("Stopping tasks {0}".format(tasks))
        client.stop_task(cluster=cluster, task=task)

    logger.info("Completed service restart")
