# AWS VPC Setup Guide

## Step 1: Create a VPC

1. **Sign in to the AWS Management Console** and open the VPC Dashboard.
2. **Click on "Your VPCs"** from the navigation pane on the left side.
3. **Click on "Create VPC"**.
4. **Configure the VPC**:
   - **Name Tag**: Enter a name for your VPC (e.g., `MyCustomVPC`).
   - **IPv4 CIDR block**: Enter an IP range for your VPC (e.g., `10.0.0.0/16`).
   - **IPv6 CIDR block**: Leave as `No IPv6 CIDR Block` unless you need IPv6 addresses.
   - **Tenancy**: Choose `Default` unless you require dedicated hardware for instances in this VPC.
5. **Click "Create VPC"** to create the VPC.

![Screenshot 2024-08-20 133825](https://github.com/user-attachments/assets/17f0fa59-2862-4a8e-9329-3c48ec13e304)


## Step 2: Create Subnets

Subnets divide the VPC's IP address range into smaller networks.

1. **Click on "Subnets"** in the VPC Dashboard.
2. **Click on "Create Subnet"**.

![Screenshot 2024-08-20 134051](https://github.com/user-attachments/assets/efad397e-2162-4288-a1f5-caa493009d91)

3. **Configure the First Subnet (e.g., Private Subnet)**:
   - **Name Tag**: Name your subnet (e.g., `MyPrivateSubnet1`).
   - **VPC**: Select the VPC you created (`MyCustomVPC`).
   - **Availability Zone**: Choose an availability zone (e.g., `us-west-1a`).
   - **IPv4 CIDR block**: Enter a subnet IP range within your VPC (e.g., `10.0.0.0/25`).

![Screenshot 2024-08-20 134157](https://github.com/user-attachments/assets/2f7966e1-90df-45cb-b326-332d11c73926)

4. **Configure the Second Subnet (e.g., Private Subnet)**:
   - **Name Tag**: Name your subnet (e.g., `MyPrivateSubnet2`).
   - **VPC**: Select the VPC you created (`MyCustomVPC`).
   - **Availability Zone**: Choose an availability zone (e.g., `us-west-1a`).
   - **IPv4 CIDR block**: Enter a subnet IP range within your VPC (e.g., `10.0.0.128/25`).
   - **Click "Create Subnet"**.

![Screenshot 2024-08-20 135103](https://github.com/user-attachments/assets/86a050e0-1f75-4f62-824b-70ea6a649c17)

## Step 3: Create a Route Table

Route tables define how traffic is routed within your VPC.

1. **Click on "Route Tables"** in the VPC Dashboard.
2. **Click on "Create route table"**.
3. **Configure the Route Table**:
   - **Name Tag**: Name your route table (e.g., `MyPublicRouteTable`).
   - **VPC**: Select your VPC (`MyCustomVPC`).
4. **Click "Create route table"**.

### Add a Route to the Route Table:

1. **Select the route table** you just created.
2. **Click on the "Routes" tab** and then "Edit routes".
3. **Add a route**:
   - **Destination**: `0.0.0.0/0` (This sends all outbound traffic to the internet).
   - **Target**: If you have an Internet Gateway, select it here.
4. **Click "Save routes"**.

### Associate the Route Table with a Subnet:

1. **Click on the "Subnet Associations" tab**.
2. **Click "Edit subnet associations"**.
3. **Select the subnet** you want to associate with this route table (e.g., `MyPublicSubnet`) and click "Save".

## Step 4: Create Security Groups

Security Groups control the inbound and outbound traffic to your resources.

1. **Click on "Security Groups"** in the VPC Dashboard.
2. **Click on "Create security group"**.
3. **Configure the Security Group**:
   - **Name Tag**: Name your security group (e.g., `MyWebServerSG`).
   - **Description**: Enter a description (e.g., `Allow HTTP and SSH traffic`).
   - **VPC**: Select your VPC (`MyCustomVPC`).

### Configure Inbound Rules:

1. **Type**: `SSH (port 22)`, **Source**: `0.0.0.0/0` (or restrict to specific IPs for security).
2. **Type**: `HTTP (port 80)`, **Source**: `0.0.0.0/0`.
3. **Add any additional rules** as necessary.

### Configure Outbound Rules:

- By default, all outbound traffic is allowed. You can leave this as is or restrict it based on your needs.

4. **Click "Create security group"**.

## Step 5: Create VPC Endpoints

VPC Endpoints allow you to privately connect your VPC to supported AWS services without needing an Internet Gateway, NAT device, VPN connection, or AWS Direct Connect.

### Create an Endpoint for S3 (or Another AWS Service)

1. **Click on "Endpoints"** in the VPC Dashboard.
2. **Click on "Create Endpoint"**.

#### Choose the Service:

1. **Service category**: Choose `AWS services`.
2. **Service Name**: Select the service you want to connect to (e.g., `com.amazonaws.us-west-1.s3` for S3).

#### Configure the Endpoint:

1. **VPC**: Select your VPC (`MyCustomVPC`).
2. **Subnets**: Select the subnets where you want the endpoint to be available.
3. **Security Group**: Select the security group you created earlier or create a new one specifically for the endpoint.

#### Policy:

1. You can either select `Full Access` or create a custom policy to control which resources within the service can be accessed.
2. Click **"Create Endpoint"**.

### Create an Endpoint for STS

Repeat the process for creating an STS endpoint:

1. **Click "Create Endpoint"** again to create an additional VPC endpoint.

#### Choose the STS Service:

1. **Service category**: Choose `AWS services`.
2. **Service Name**: Type `sts` in the search bar and select `com.amazonaws.us-west-1.sts` (make sure to select the correct region).

#### Configure the STS Endpoint:

1. **VPC**: Select your VPC (`MyCustomVPC`).
2. **Subnets**: Choose the subnets where the STS endpoint should be available. Typically, you'd select subnets that host resources needing access to STS.
3. **Security Group**: Select the security group you created earlier or create a new one specifically for this STS endpoint.

#### Policy:

1. Similar to other endpoints, you can choose `Full Access` or create a custom policy depending on your security requirements.
2. Click **"Create Endpoint"**.