# Step-by-Step Tutorial: Creating an AWS Lambda Function for S3 Log File Processing

This tutorial will guide you through creating an AWS Lambda function to transfer `.log` files from an S3 bucket to an EC2 instance whenever a new log file is uploaded to the bucket. We’ll also set up the necessary environment variables and S3 bucket trigger.

## Prerequisites

- An AWS account with permissions to create Lambda functions, S3 buckets, and EC2 instances.
- An existing EC2 instance with the SSM (AWS Systems Manager) agent installed and running.

## Step 1: Create the Lambda Function

1. **Log in to the AWS Management Console.**

2. **Navigate to the Lambda service:**
   - Go to the AWS Management Console.
   - Search for "Lambda" in the search bar and select it.

3. **Create a new Lambda function:**
   - Click on the "Create function" button.
   - Choose "Author from scratch."
   - **Function name:** Give your function a name, e.g., `S3ToEC2LogTransfer`.
   - **Runtime:** Select `Python 3.8` (or a later supported version).
   - **Permissions:** Under "Change default execution role," select "Use an existing role" or create a new role with the necessary permissions (`AmazonS3ReadOnlyAccess`, `AmazonSSMFullAccess`, `AWSLambdaBasicExecutionRole`).
   - **Advanced Settings:** If you're using a VPC, ensure to enable the "Enable VPC" option and configure it with your desired VPC settings.

![image](https://github.com/user-attachments/assets/48442464-b520-4266-8293-2a1c158a9780)

![image](https://github.com/user-attachments/assets/afc49fde-72bb-47ac-9793-e0743876fd9e)

4. **Set up the Lambda function code:**
   - In the function's code editor, replace the placeholder code with the provided code:

     ```python
     import boto3
     import os

     s3_client = boto3.client('s3')
     ssm_client = boto3.client('ssm')

     EC2_INSTANCE_ID = os.environ['EC2_INSTANCE_ID']
     REMOTE_PATH = os.environ['REMOTE_PATH']
     BUCKET_NAME = os.environ['BUCKET_NAME']

     def lambda_handler(event, context):
         object_key = event['Records'][0]['s3']['object']['key']

         # Command to download the file directly from S3 on the EC2 instance
         command = f"aws s3 cp s3://{BUCKET_NAME}/{object_key} {os.path.join(REMOTE_PATH, os.path.basename(object_key))}"
         
         try:
             response = ssm_client.send_command(
                 InstanceIds=[EC2_INSTANCE_ID],
                 DocumentName="AWS-RunShellScript",
                 Parameters={'commands': [command]}
             )
             command_id = response['Command']['CommandId']
             waiter = ssm_client.get_waiter('command_executed')
             waiter.wait(CommandId=command_id, InstanceId=EC2_INSTANCE_ID)
         except boto3.exceptions.Boto3Error as e:
             print(f"An error occurred: {e}")

         return {
             'statusCode': 200,
             'body': f'Successfully transferred {object_key} to EC2 instance {EC2_INSTANCE_ID}'
         }
     ```
![image](https://github.com/user-attachments/assets/6a34efb8-638a-42a5-ad31-02d081269ec2)

5. **Set up the environment variables:**
   - Scroll down to the "Environment variables" section.
   - Add the following environment variables:
     - `EC2_INSTANCE_ID` = Your EC2 instance ID.
     - `REMOTE_PATH` = The path on the EC2 instance where you want to save the log files (e.g., `/var/logs/`).
     - `BUCKET_NAME` = The name of the S3 bucket where the log files are stored.

![image](https://github.com/user-attachments/assets/60b35341-cda5-4a61-8ab6-5d21d0cecd88)

6. **Review and save the function:**
   - Click on the "Deploy" button to save your Lambda function.

## Step 2: Set Up the S3 Trigger

1. **Navigate to the S3 service:**
   - Go to the AWS Management Console.
   - Search for "S3" and select it.

2. **Choose your S3 bucket:**
   - In the S3 dashboard, click on the bucket where your log files will be uploaded.

3. **Create a new event notification:**
   - Go to the "Properties" tab of the S3 bucket.
   - Scroll down to the "Event notifications" section.
   - Click on "Create event notification."

4. **Configure the event notification:**
   - **Event name:** Enter a name for the event (e.g., `LogFileUploadTrigger`).
   - **Prefix (optional):** If your log files are stored in a specific folder within the bucket, enter the folder path here (e.g., `logs/`).
   - **Suffix (optional):** To trigger the event only for `.log` files, enter `.log` here.
   - **Events:** Select "All object create events."
   - **Destination:** Choose "Lambda function."
   - **Lambda function:** Select the Lambda function you created earlier (`S3ToEC2LogTransfer`).
  
![image](https://github.com/user-attachments/assets/b8c695a8-79bf-479d-9b11-cc9d23cde0d1)

5. **Save the event notification:**
   - Click on the "Save changes" button.

## Step 3: Test the Lambda Function

1. **Upload a `.log` file to your S3 bucket:**
   - Use the S3 console, AWS CLI, or any SDK to upload a `.log` file to the bucket.

2. **Verify the file transfer:**
   - Check the specified `REMOTE_PATH` on your EC2 instance to ensure the file has been transferred.
   - You can also monitor the Lambda function logs in CloudWatch to see if the function executed successfully.

## Conclusion

You have successfully created an AWS Lambda function that triggers whenever a `.log` file is uploaded to an S3 bucket. The Lambda function sends the log file to an EC2 instance for further processing using AWS Systems Manager (SSM). This setup enables automated and efficient log file handling in your AWS environment.
