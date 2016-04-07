# ECS Service Restart λ

ECS API currently does not allow users restart running services. Workaround is update service desired task to 0 and later update back with original value.
Another solutions, used in this Lambda, stops underlying tasks associated with service. This will force scheduler to run new tasks.

## How to use
1. `$ git clone https://github.com/s7anley/aws-ecs-service-stop-lambda.git` or [download zip](https://github.com/s7anley/aws-ecs-service-stop-lambda/archive/master.zip).
2. Deploy to lambda function with your favorite method e.g. copy content of main.py to editor or upload zip to S3 bucket
3. Create custom Cloudwatch Event Rule with event defined as Constant (JSON text) and attach it to Lambda
    ```json
    {
       "cluster": "mycluster",
       "service_name": "myservice"
    }
    ```

4. Configure lambda
  * Runtime: Python
  * Handler: `lambda_function.restart_service`
  * Set & attach `role` to lambda function
  * Minimum role policy
   ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ecs:ListTasks",
                    "ecs:StopTask",
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "*"
            }
        ]
    }
```

## What about other event types?

Maybe this Lambda will fits you out-of-box, but it's just generic template which shows, how you can restart ECS service.
You should adjust the code according your expected event e.g. S3 bucket name.
