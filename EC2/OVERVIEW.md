# How to Create an EC2 Instance in AWS

*Before you begin, make sure you change your region to us-west-1*

![image](https://github.com/user-attachments/assets/51ef1963-e327-44f7-8af8-388fe7ba662e)


## Step 1: Log in to the AWS Management Console
1. Navigate to the [AWS Management Console](https://aws.amazon.com/console/).
2. Log in with your AWS account credentials.

## Step 2: Access the EC2 Dashboard
1. Once logged in, locate the **Services** menu at the top of the page.
2. Under **Compute**, click on **EC2** to access the EC2 Dashboard.

![image](https://github.com/user-attachments/assets/3bcbf1ad-8809-4dd5-93b7-df12bd0a65a6)

## Step 3: Launch a New Instance
1. In the EC2 Dashboard, click on the **Launch Instance** button.
2. This will take you to the "Launch an instance" page.

![image](https://github.com/user-attachments/assets/10630271-ae33-4860-9495-96f188667cb1)

## Step 4: Configure the Instance

### 4.1 Choose an Amazon Machine Image (AMI)
1. Select an Amazon Machine Image (AMI) from the list. Common options include:
   - **Amazon Linux 2**
   - **Ubuntu Server**
   - **Red Hat Enterprise Linux**
   - **Microsoft Windows Server**
2. For this architecture, click **Select** next to your preferred AMI.

   **Use the defaults for the Amazon Machine Image**:
   - **Amazon Linux**: Amazon Linux 2023 AMI
   - **Architecture**: 64-bit

![image](https://github.com/user-attachments/assets/4c82b33c-4cbc-485f-a9c3-006810bbc638)

### 4.2 Choose an Instance Type
1. **Use the default Instance Type**: `t2.micro` (1 vCPU, 1 GiB RAM) - Free tier eligible.
2. Click **Next: Configure Instance Details**.

![image](https://github.com/user-attachments/assets/56c5cbe9-8b18-493b-9ba7-e7578ccd590f)

### 4.3 Create a New Key Pair
1. **Create a new key pair** for remote SSH access.
2. You can name the key pair anything, but for this lab, consider using your login as the name.
3. Set the following:
   - **Type**: RSA
   - **Format**: `.pem`
4. Click **[Create key pair]**.

   Creating the key will download it to your computer. You can use this to remotely connect using an SSH client from your desktop.

![image](https://github.com/user-attachments/assets/4163e7fd-a7f1-46cd-ad73-010f679bda16)

### 4.4 Configure Instance Details
1. **Network**: Choose the VPC where you want to launch the instance.
2. **Subnet**: Select a subnet if you have specific requirements; otherwise, use the default.
3. **Auto-assign Public IP**: Choose whether to auto-assign a public IP. For our architecture you will enable this.
4. **Create a new security group**: Define a new security group or select an existing one.
5. **Inbound Rules**: Set up rules to allow specific traffic, such as SSH (port 22) for Linux or RDP (port 3389) for Windows.
5. Leave the other settings as default unless you have specific needs.
6. Click **Next: Add Storage**.

![image](https://github.com/user-attachments/assets/1b7d77ae-d2a3-4f4b-8ab1-930207b983f6)

### 4.5 Add Storage
1. The default root volume will be displayed. Keep the default storage; However you may modify the size if necessary.
2. To add additional storage, click **Add New Volume**.
3. Click **Review and Launch**.

![image](https://github.com/user-attachments/assets/182e735e-f48f-4fe0-a4ce-7dcf334486a8)

## Step 5: Review and Launch
1. Review all your instance settings.
2. Click **Launch** to start your instance.

## Step 6: Access Your EC2 Instance
1. Click **View Instances** to see your running instance.
2. Note the **Public IP** or **Public DNS** of your instance.
3. Use an SSH client to connect to your instance (for Linux) or RDP (for Windows).

## Step 7: Terminate the Instance (Optional)
1. If you no longer need the instance, go to the **Instances** section.
2. Select the instance, click on **Actions**, then **Instance State** > **Terminate**.
3. Confirm the termination.
