# Step 1: Create the VPC

To create a VPC, follow these steps:

1. **Sign in to the AWS Management Console**  
   Open the AWS Management Console and navigate to the **VPC Dashboard**.

2. **Access Your VPCs**  
   In the navigation pane on the left side, click on **Your VPCs**.

3. **Create a New VPC**  
   Click the **Create VPC** button to begin configuring your VPC.

4. **Configure the VPC:**

   - **Name Tag:**  
     Provide a name for your VPC (e.g., `MyBasicVPC`).

   - **IPv4 CIDR Block:**  
     Enter an IP range (e.g., `10.0.0.0/16`). This defines the IP address range for your VPC.

   - **IPv6 CIDR Block:**  
     Leave this as **No IPv6 CIDR Block** unless you require IPv6.

   - **Tenancy:**  
     Choose **Default** unless you have specific requirements for dedicated instances.

5. **Create the VPC**  
   After configuring, click **Create VPC** to finalize the creation of your new VPC.

![Screenshot 2024-08-20 124401](https://github.com/user-attachments/assets/9d6722e7-3572-4537-93ea-595482249d29)


# Step 2: Create Subnets

Subnets allow you to segment your VPC into smaller networks. Follow these steps to create and configure subnets:

1. **Navigate to Subnets**  
   In the **VPC Dashboard**, click on **Subnets**.

2. **Create a Subnet**  
   Click on the **Create Subnet** button.

3. **Configure the Subnet:**

   - **Name Tag:**  
     Assign a name to your subnet (e.g., `MyPublicSubnet`).

   - **VPC:**  
     Select the VPC you just created (e.g., `MyBasicVPC`).

   - **Availability Zone:**  
     Choose an availability zone (e.g., `us-west-1a`).

   - **IPv4 CIDR Block:**  
     Specify a smaller range within your VPC's range (e.g., `10.0.1.0/24` for a public subnet).

4. **Create the Subnet**  
   After configuring the details, click **Create Subnet**.

5. **(Optional) Create Additional Subnets:**  
   If needed, repeat the above steps to create additional subnets. For example, you might want to create a private subnet (e.g., `10.0.2.0/24`).



![image](https://github.com/user-attachments/assets/11e48c8b-f550-45e8-8605-4a8796f5e0f0)
