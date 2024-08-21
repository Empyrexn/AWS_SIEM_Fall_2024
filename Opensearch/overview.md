
# Guide to Creating a Private OpenSearch Domain on AWS

This guide walks you through the steps to create a private OpenSearch domain, ensuring that it is accessible only within your Amazon Virtual Private Cloud (VPC), enhancing security by restricting public access.

## **Step 1: Create a Private VPC (No Internet Gateway Routed)**

Before setting up a private OpenSearch domain, ensure you have a VPC where the domain will reside.

1. **Navigate to the VPC Dashboard**:
   - Go to the [VPC Dashboard](https://console.aws.amazon.com/vpc/).
  
2. **Create a New VPC**:
   - Click on **Create VPC**.
   - Fill in the following details:
     - **Name tag**: Enter a name for your VPC.
     - **IPv4 CIDR block**: Specify the CIDR block (e.g., `10.0.0.0/16`).
     - **Tenancy**: Choose between **Default** or **Dedicated**.
   - Click **Create VPC**.

## **Step 2: Create Subnets**

Subnets in your VPC will host the OpenSearch domain.

1. **Create Subnets**:
   - In the VPC Dashboard, go to **Subnets** and click **Create subnet**.
   - Select your VPC and specify the subnet details:
     - **Name tag**: Enter a name for the subnet.
     - **Availability Zone**: Choose an availability zone.
     - **IPv4 CIDR block**: Specify a CIDR block (e.g., `10.0.1.0/24`).
   - Repeat the above steps to create additional subnets in different availability zones if needed.

## **Step 3: Create Security Groups**

Security groups control inbound and outbound traffic to your OpenSearch domain.

1. **Create a Security Group**:
   - In the VPC Dashboard, go to **Security Groups** and click **Create security group**.
   - Fill in the details:
     - **Name tag**: Provide a name for the security group.
     - **Description**: Briefly describe the security group.
     - **VPC**: Select the VPC you created earlier.
  
2. **Configure Inbound Rules**:
   - Add rules to allow traffic from trusted sources (e.g., your EC2 instances).
   - Typically, allow traffic on port `443` (HTTPS) from your VPC CIDR block.

3. **Configure Outbound Rules**:
   - Allow all outbound traffic by default.

4. **Create the Security Group**:
   - Click **Create security group**.

## **Step 4: Create a Private OpenSearch Domain**

With your VPC, subnets, and security groups ready, you can now create the OpenSearch domain.

1. **Go to the OpenSearch Service Console**:
   - Visit the [Amazon OpenSearch Service Console](https://console.aws.amazon.com/es/).

2. **Configure Domain Settings**:
   - **Domain name**: Enter a name for your domain.

![Screenshot 2024-08-21 080442](https://github.com/user-attachments/assets/fcbf0b8a-9cac-437b-bc90-942b3b8487c6)

3. **Start Domain Creation**:
   - Click **Create domain**.
   - Choose **Deployment type**: Select **Production** for a private domain.

![Screenshot 2024-08-21 080510](https://github.com/user-attachments/assets/19a58e8d-c977-44db-a63b-8b2d393ee074)

4. **Data Nodes**:
   - Configure the domain’s instance type, storage, and other settings according to your needs.

5. **Network Configuration**:
   - **VPC**: Select the VPC you created.
   - **Subnets**: Select the subnets where your domain will reside.
   - **Security groups**: Select the security group created earlier.

![Screenshot 2024-08-21 080619](https://github.com/user-attachments/assets/b9622236-4ecf-48b7-8a5c-97a4f0e1b4d6)

6. **Access Policy**:
   - Choose **Fine-grained access control** if you want to manage access to the domain through IAM roles.

![Screenshot 2024-08-21 080748](https://github.com/user-attachments/assets/dc905f92-3c94-4f23-b9c1-ff0b07c226cc)


7. **Create the Domain**:
   - Review the configuration and click **Create**.
   - Note Opensearch Domain clusters do take 15 min+

![Screenshot 2024-08-21 081443](https://github.com/user-attachments/assets/7a2d04d7-a524-4340-8278-4a4c040e5eee)


## **Step 5: Configure Access to the Domain**

Ensure that your EC2 instances or other AWS resources can access the private OpenSearch domain within the same VPC.

1. **Attach an IAM Policy**:
   - Attach a policy to your EC2 instances that grants permission to access the OpenSearch domain.
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "es:*",
         "Resource": "arn:aws:es:<your-region>:<your-account-id>:domain/<your-domain-name>/*"
       }
     ]
   }
   ```
   
## **Step 6: Test the OpenSearch Domain**

1. **Access from EC2**:
   - Log in to an EC2 instance within the same VPC.
  
2. **Test Connectivity**:
   - Use `curl` or another HTTP client to make a request to the OpenSearch domain’s endpoint.
   ```bash
   curl -XGET https://<your-opensearch-endpoint> -u 'username:password'
   ```

## **Step 7: Monitor and Manage the Domain**

- **Use CloudWatch**: Monitor the health and performance of your OpenSearch domain using Amazon CloudWatch.
- **Review Security**: Regularly review security settings and access policies to ensure they align with your security requirements.

## **Step 8: Access Opensearch Domain**
   -Creating a ssh tunnel into the Opensearch Domain by setting up a bastion host in the EC2 instance
```bash
ssh -i "path-to/your-key-file.pem" -L local_port:opensearch_endpoint:opensearch_port -o IdentitiesOnly=yes ec2-user@your-ec2-public-ip
```

   -Browser link to access Opensearch Dashboards
```text
https://localhost:9200/_dashboards/app/home#/

```

![Screenshot 2024-08-21 083210](https://github.com/user-attachments/assets/f1b5d695-27d3-49d1-a365-ad435b215b5c)

