import boto3
import time

# Configuration
BUCKET_NAME = 'insert-bucket-name'
SOURCE_PREFIX = ''  # Adjust the path to where your logs are stored
DESTINATION_PATH = '/var/log/s3_logs'
TAG_KEY = 'Logged'
TAG_VALUE = 'True'
CHECK_INTERVAL = 15  # Check every 15 seconds (15 seconds)

# Initialize the S3 client
s3_client = boto3.client('s3')

def check_and_tag_logs():
    # List all objects under the specified prefix
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=SOURCE_PREFIX)

    if 'Contents' in response:
        for obj in response['Contents']:
            object_key = obj['Key']

            # Get object tags
            try:
                tags = s3_client.get_object_tagging(Bucket=BUCKET_NAME, Key=object_key)
                tag_set = tags['TagSet']

                # Check if the tag already exists
                tag_exists = any(tag['Key'] == TAG_KEY and tag['Value'] == TAG_VALUE for tag in tag_set)

                if not tag_exists:
                    # Copy the log to the local directory
                    local_path = f"{DESTINATION_PATH}/{object_key.split('/')[-1]}"
                    s3_client.download_file(BUCKET_NAME, object_key, local_path)
                    print(f"Copied {object_key} to {local_path}")

                    # Add the CheckSeen=True tag
                    tag_set.append({'Key': TAG_KEY, 'Value': TAG_VALUE})
                    s3_client.put_object_tagging(
                        Bucket=BUCKET_NAME,
                        Key=object_key,
                        Tagging={'TagSet': tag_set}
                    )
                    print(f"Added tag {TAG_KEY}={TAG_VALUE} to {object_key}")

            except s3_client.exceptions.NoSuchTagSet:
                # If no tags are present, proceed to tag the object
                print(f"No tags found for {object_key}. Copying and tagging...")
                local_path = f"{DESTINATION_PATH}/{object_key.split('/')[-1]}"
                s3_client.download_file(BUCKET_NAME, object_key, local_path)
                print(f"Copied {object_key} to {local_path}")

                # Add the CheckSeen=True tag
                s3_client.put_object_tagging(
                    Bucket=BUCKET_NAME,
                    Key=object_key,
                    Tagging={'TagSet': [{'Key': TAG_KEY, 'Value': TAG_VALUE}]}
                )
                print(f"Added tag {TAG_KEY}={TAG_VALUE} to {object_key}")

    else:
        print("No logs found.")

if __name__ == "__main__":
    while True:
        check_and_tag_logs()
        print(f"Waiting for {CHECK_INTERVAL} seconds before the next check...")
        time.sleep(CHECK_INTERVAL)
