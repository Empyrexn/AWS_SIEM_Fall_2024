# Configuring AWS CLI on Amazon Linux 2

## Step 1: Install the AWS CLI
Amazon Linux 2 usually comes with the AWS CLI pre-installed. You can check if it's installed by running:

```bash
aws --version
```

If the AWS CLI is not installed, you can install it using the following command:

```bash
sudo yum install -y aws-cli
```

## Step 2: Configure AWS CLI

To configure the AWS CLI, you'll need your AWS credentials (Access Key ID and Secret Access Key) and the default region you'd like to work in.

1. Run the configuration command:

    ```bash
    aws configure
    ```

2. You'll be prompted to enter the following information:

    - **AWS Access Key ID**: Your AWS Access Key ID.
    - **AWS Secret Access Key**: Your AWS Secret Access Key.
    - **Default region name**: The region you want to use by default (e.g., `us-west-1`).
    - **Default output format**: The output format you prefer (e.g., `json`, `text`, `table`). If unsure, you can leave this as `json`.

Example:

```bash
$ aws configure
AWS Access Key ID [None]: ABCDEFGHIJKLMNOPQRST
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-1
Default output format [None]: json
```

## Step 3: Verify the Configuration

You can verify that the configuration was successful by running a simple AWS CLI command, such as listing your S3 buckets:

```bash
aws s3 ls
```

This command should return a list of your S3 buckets if everything is configured correctly.

## Step 4: Advanced Configuration (Optional)

If you need to configure multiple profiles, you can add them manually by editing the `~/.aws/credentials` and `~/.aws/config` files.

### Example of `~/.aws/credentials`:
```plaintext
[default]
aws_access_key_id = ABCDEFGHIJKLMNOPQRST
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[profile2]
aws_access_key_id = ABCDEFGHIJKLMNOPQRST2
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY2
```

### Example of `~/.aws/config`:
```plaintext
[default]
region = us-west-1
output = json

[profile profile2]
region = us-east-1
output = table
```

You can then specify which profile to use with the `--profile` flag:

```bash
aws s3 ls --profile profile2
```

## Step 5: Update AWS CLI (Optional)
To ensure you have the latest version of the AWS CLI, you can update it using the following command:

```bash
sudo yum update aws-cli
```

This guide should help you get the AWS CLI configured on an Amazon Linux 2 instance.
