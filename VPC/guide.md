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

4. **(Optional: see note) Create Additional Subnets:**  
   If needed, repeat the above steps to create additional subnets. For example, you might want to create a private subnet (e.g., `10.0.2.0/24`). Note Opensearch requires 2 subnets to operate.
   


![image](https://github.com/user-attachments/assets/11e48c8b-f550-45e8-8605-4a8796f5e0f0)
![Screenshot 2024-08-20 125243](https://github.com/user-attachments/assets/6034f262-78ce-4ad4-9b80-aa92342141c5)

5. **Create the Subnet**  
   After configuring the details, click **Create Subnet**.
   
![Screenshot 2024-08-20 130202](https://github.com/user-attachments/assets/9c444062-4256-4a3d-88f7-fca223b94a4d)


# Step 3: Create an Internet Gateway

An Internet Gateway enables communication between instances in your VPC and the internet. Follow these steps to create and attach an Internet Gateway:

1. **Navigate to Internet Gateways**  
   In the **VPC Dashboard**, click on **Internet Gateways**.

2. **Create an Internet Gateway**  
   Click on the **Create internet gateway** button.

3. **Configure the Internet Gateway:**

   - **Name Tag:**  
     Assign a name to your Internet Gateway (e.g., `MyInternetGateway`).

4. **Create the Internet Gateway**  
   After entering the name, click **Create internet gateway**.

![Screenshot 2024-08-20 125547](https://github.com/user-attachments/assets/499b48e2-a442-4b99-9596-2437583c5f53)


5. **Attach the Internet Gateway:**

   - **Select the Internet Gateway**  
     Select the Internet Gateway you just created.

   - **Attach to VPC:**  
     Click on **Actions** and choose **Attach to VPC**.

![Screenshot 2024-08-20 125905](https://github.com/user-attachments/assets/fb676c9b-2aac-4fc0-a142-05f858c746c0)


   - **Select Your VPC:**  
     Choose your VPC (e.g., `MyBasicVPC`) and click **Attach Internet Gateway**.

![Screenshot 2024-08-20 130413](https://github.com/user-attachments/assets/62ed6dd1-4cf8-485a-a808-ad19b740befb)


# Step 4: Create a Route Table

Route tables manage the routing of traffic within your VPC. Follow these steps to create and configure a route table:

1. **Navigate to Route Tables**  
   In the **VPC Dashboard**, click on **Route Tables**.

2. **Create a Route Table**  
   Click on the **Create route table** button.



3. **Configure the Route Table:**

   - **Name Tag:**  
     Assign a name to your route table (e.g., `MyPublicRouteTable`).

   - **VPC:**  
     Select your VPC (e.g., `MyBasicVPC`).

4. **Create the Route Table**  
   After configuring, click **Create route table**.

![Screenshot 2024-08-20 131336](https://github.com/user-attachments/assets/e85dcba8-34ca-47d6-a81f-75e6a12fae8e)


5. **Configure Routes:**

   - **Select the Route Table:**  
     Choose the route table you just created.

   - **Edit Routes:**  
     Click on the **Routes** tab and then click **Edit routes**.

![Screenshot 2024-08-20 131532](https://github.com/user-attachments/assets/1497f6ae-01a3-431c-afa8-8889cbe1e390)

   - **Add a Route:**
     - **Destination:** Enter `0.0.0.0/0` (This route directs all internet traffic).
     - **Target:** Select the Internet Gateway (e.g., `MyInternetGateway`).

   - **Save Routes:**  
     Click **Save routes** to apply the changes.

![Screenshot 2024-08-20 131622](https://github.com/user-attachments/assets/0fc2711d-5980-4b8a-b128-35aab67432aa)

6. **Associate the Route Table with a Subnet:**

   - **Subnet Associations:**  
     Click on the **Subnet Associations** tab.

   - **Edit Subnet Associations:**  
     Click **Edit subnet associations**.

   - **Select Your Subnet:**  
     Choose the subnet you created earlier (e.g., `MyPublicSubnet`) and click **Save**.

![Screenshot 2024-08-20 131811](https://github.com/user-attachments/assets/27ef7a3f-114a-4bfb-b4d0-4c1ba90b2b17)

     
# Step 5: Create Security Groups

Security Groups act as virtual firewalls to control the traffic allowed to and from your instances. Follow these steps to create and configure a security group:

1. **Navigate to Security Groups**  
   In the **VPC Dashboard**, click on **Security Groups**.

2. **Create a Security Group**  
   Click on the **Create security group** button.

3. **Configure the Security Group:**

   - **Name Tag:**  
     Name your security group (e.g., `MyWebServerSG`).

   - **Description:**  
     Enter a description (e.g., `Allow HTTP and SSH access`).

   - **VPC:**  
     Select your VPC (e.g., `MyBasicVPC`).

4. **Configure Inbound Rules:**

   - **Type:** SSH  
     - **Port:** 22  
     - **Source:** `0.0.0.0/0` (or restrict to specific IPs).

   - **Type:** HTTP  
     - **Port:** 80  
     - **Source:** `0.0.0.0/0`.

   - **Add Rule:**  
     Click **Add Rule** for each additional rule.

5. **Create the Security Group**  
   After configuring the rules, click **Create security group**.

