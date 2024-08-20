Here’s a guide to changing the STS endpoint and other AWS configuration settings for your `default` and `my-profile` profiles:

# Guide to Updating STS Endpoint in AWS CLI Configuration

## Step 1: Navigate to the `.aws` Directory

Start by navigating to the `.aws` directory where your AWS CLI configuration files (`config` and `credentials`) are stored.

```bash
cd ~
cd .aws
```

## Step 2: View the Current Configuration

List the files in the `.aws` directory and view the current `config` file to understand the existing settings.

```bash
ls
cat config
```

This will display something like:

```plaintext
[default]
region = us-west-1

[profile my-profile]
region = us-west-1
sts_regional_endpoints = regional
endpoint_url = https://vpce-04d9e4dc750078c2b-s9cm8r83.sts.us-west-1.vpce.amazonaws.com
```

## Step 3: Edit the Configuration File

To modify the STS endpoint or other variables, you'll need to edit the `config` file.

1. Open the `config` file in a text editor:

    ```bash
    nano config
    ```

2. Update the STS endpoint and any other desired settings under the appropriate profile.

### Example Configuration:

If you want to update the STS endpoint URL and ensure both profiles use the regional STS endpoints, your `config` file might look like this:

```plaintext
[default]
region = us-west-1
sts_regional_endpoints = regional
endpoint_url = https://vpce-04d9e4dc750078c2b-s9cm8r83.sts.us-west-1.vpce.amazonaws.com

[profile my-profile]
region = us-west-1
sts_regional_endpoints = regional
endpoint_url = https://vpce-04d9e4dc750078c2b-s9cm8r83.sts.us-west-1.vpce.amazonaws.com
```

### Key Variables:
- **region**: Specifies the AWS region.
- **sts_regional_endpoints**: This can be set to `regional` to use the regional endpoint for STS.
- **endpoint_url**: The custom endpoint URL for the STS service.

## Step 4: Save and Exit

After making your changes, save the file and exit the editor.

- In Nano, you can save and exit by pressing `Ctrl + O`, then `Enter`, and `Ctrl + X`.

## Step 5: Verify the Configuration

To ensure your changes have been applied correctly, you can use the following command to display the current configuration for a specific profile:

```bash
aws configure list --profile my-profile
```

This command should show the updated settings, including the new STS endpoint.

## Step 6: Test the Configuration

Finally, test the configuration by making an STS request using the updated profile:

```bash
aws sts get-caller-identity --endpoint-url https://vpce-sts-dns
```

This should return your AWS account details if everything is configured correctly.
