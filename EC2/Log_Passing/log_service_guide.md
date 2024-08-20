# Setting Up a Python Script as a Systemd Service on an EC2 Instance

## Step 1: Prepare the Script
First, make sure the script is executable and saved in a directory on your EC2 instance. For this example, let's assume the script is saved as `/usr/local/bin/s3_log_service.py`.

## Step 2: Ensure Python and Boto3 are Installed
If you haven't already, ensure that Python and the `boto3` library are installed on your instance:

```bash
sudo yum install -y python3
pip3 install boto3
```

## Step 3: Create a Systemd Service File
Next, you'll create a systemd service file to manage the script as a service.

1. Create the service file:
    ```bash
    sudo nano /etc/systemd/system/s3_log_service.service
    ```

2. Populate the service file with the following content:

    ```ini
    [Unit]
    Description=S3 Log Tagging and Download Service
    After=network.target

    [Service]
    ExecStart=/usr/bin/python3 /usr/local/bin/s3_log_service.py
    Restart=always
    User=nobody
    Group=nogroup
    Environment=BUCKET_NAME='insert-bucket-name'
    Environment=SOURCE_PREFIX=''
    Environment=DESTINATION_PATH='/var/log/s3_logs'
    Environment=TAG_KEY='Logged'
    Environment=TAG_VALUE='True'
    Environment=CHECK_INTERVAL=15

    [Install]
    WantedBy=multi-user.target
    ```

## Step 4: Reload Systemd and Start the Service
Reload systemd to apply the new service:

```bash
sudo systemctl daemon-reload
```

Start the service:

```bash
sudo systemctl start s3_log_service
```

Enable the service to start on boot:

```bash
sudo systemctl enable s3_log_service
```

## Step 5: Check the Service Status
To verify that the service is running correctly:

```bash
sudo systemctl status s3_log_service
```

## Step 6: View Logs
You can check the logs of your service using `journalctl`:

```bash
sudo journalctl -u s3_log_service -f
```

## Step 7: Stopping and Disabling the Service
If you need to stop the service:

```bash
sudo systemctl stop s3_log_service
```

To disable the service from starting at boot:

```bash
sudo systemctl disable s3_log_service
```
```

This markdown format provides a clear and structured guide to setting up a Python script as a systemd service on an EC2 instance.
