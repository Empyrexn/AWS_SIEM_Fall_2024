# Setting Up Fluent Bit on EC2 to Process Logs from S3 and Send to OpenSearch

This guide will walk you through installing Fluent Bit on an EC2 instance, configuring it to process logs from an S3 bucket, and sending the logs to an OpenSearch Ingestion pipeline.

## Step 1: Install Fluent Bit on EC2

First, you need to install Fluent Bit on your EC2 instance. Fluent Bit is a fast Log Processor and Forwarder, allowing you to collect logs from different sources, process them, and deliver them to multiple destinations.

### 1.1 Update the Package Index

```
sudo yum update -y
```
### 1.2 Install Fluent Bit

```
curl https://raw.githubusercontent.com/fluent/fluent-bit/master/install.sh | sh
```

## Step 2: Configure Fluent Bit

Now that Fluent Bit is installed, you need to configure it to read logs from an S3 bucket and send them to OpenSearch.

### 2.1 Create the Fluent Bit Configuration File

Edit the default configuration file in Fluent Bit:

```bash
sudo nano /etc/fluent-bit/fluent-bit.conf
```

### 2.2 Add the Following Configuration

Replace the placeholders with your actual values:

```ini
[SERVICE]
    Flush 1                      # Interval in seconds to flush records
    Daemon Off                   # Set to 'Off' to run in foreground
    Parsers_File /etc/fluent-bit/parsers.conf    # File containing parsers
    Plugins_File /etc/fluent-bit/plugins.conf    # File containing plugins
    Buffer_Max_Size 8M           # Maximum buffer size
    Buffer_Chunk_Size 512k       # Chunk size
    Log_Level trace              # Set log level (error, warn, info, debug, trace)

[INPUT]
    Name tail                    # Plugin name
    refresh_interval 5           # Interval to refresh file in seconds
    Path /path/to/your/logs/*.log    # Path to log files
    read_from_head true          # Read logs from the start of the file

[FILTER]
    Name parser                  # Plugin name
    Match *                      # Apply to all logs
    Key_Name log                 # The key name to parse
    Parser your_parser_name      # Specify the parser name
    Reserve_Data true            # Reserve original data
    Preserve_Key true            # Keep original key

[OUTPUT]
    Name http                    # Plugin name
    Match *                      # Apply to all logs
    Host your-pipeline-endpoint  # Hostname of your pipeline endpoint
    Port 443                     # Port number
    URI /your-uri-path           # URI path
    Format json                  # Output format
    AWS_Auth On                  # Use AWS IAM role for authentication
    AWS_Region your-region       # AWS region
    AWS_Service your-service     # AWS service name
    tls On                       # Enable TLS encryption
    Log_Level trace              # Set log level (error, warn, info, debug, trace)
```

### 2.3 Save and Exit

Press `Ctrl + X`, then `Y`, and hit `Enter` to save the configuration file and exit the editor.

## Step 3: Restart Fluent Bit

After configuring Fluent Bit, restart the service to apply the changes:

```bash
sudo systemctl restart fluent-bit
```

## Step 4: Enable Fluent Bit to Start on Boot

Ensure Fluent Bit starts automatically when your EC2 instance boots:

```bash
sudo systemctl enable fluent-bit
```

## Step 5: Verify Fluent Bit Status

To verify that Fluent Bit is running correctly:

```bash
sudo systemctl status fluent-bit
```

## Step 6: Check Fluent Bit Logs

You can check the logs of Fluent Bit to troubleshoot or confirm it is processing logs correctly:

```bash
sudo journalctl -u fluent-bit -f
```

## Additional Steps: Customizing Fluent Bit Configuration

- **Parsers**: Define custom parsers in `/etc/fluent-bit/parsers.conf`.
- **Plugins**: Add custom plugins by specifying them in `/etc/fluent-bit/plugins.conf`.

## Summary

With this setup, Fluent Bit will process logs from your specified S3 bucket, filter them, and send them to your OpenSearch ingestion pipeline. This setup can be customized further based on your specific requirements.
```
