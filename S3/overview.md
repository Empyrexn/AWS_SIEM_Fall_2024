# How to Create an S3 Bucket in AWS

*Before you begin, make sure you change your region to the desired one (e.g., us-west-1)*

## Step 1: Log in to the AWS Management Console
1. Navigate to the [AWS Management Console](https://aws.amazon.com/console/).
2. Log in with your AWS account credentials.

## Step 2: Access the S3 Service
1. Once logged in, locate the **Services** menu at the top of the page.
2. Under **Storage**, click on **S3** to access the S3 Dashboard.

![image](https://github.com/user-attachments/assets/78272fc1-4d90-486b-a6c9-e36fd9222562)

## Step 3: Create a New S3 Bucket
1. In the S3 Dashboard, click on the **Create bucket** button.
2. This will take you to the "Create bucket" configuration page.

![image](https://github.com/user-attachments/assets/567d5d94-b5ac-4398-acc9-fa659fc09f38)

## Step 4: Configure the S3 Bucket

### 4.1 Bucket Name and Region
1. **Bucket name**: Enter a unique name for your bucket. Bucket names must be globally unique across all AWS users.
2. **Region**: Select the AWS Region where you want the bucket to be created. (e.g., `us-west-1`)

![image](https://github.com/user-attachments/assets/0c04a766-e241-45ff-8a43-37f3ea914435)

### 4.2 Bucket Settings for Block Public Access
1. **Block Public Access settings for this bucket**: 
   - By default, all public access is blocked. You can keep it this way for most use cases.
   - If you need to make the bucket public, adjust the settings here by unchecking specific boxes, but ensure you understand the security implications.

### 4.3 Bucket Versioning (Optional)
1. **Bucket Versioning**: Enable versioning if you want to keep multiple versions of an object in the bucket. This is useful for backup and recovery scenarios.

### 4.4 Tags (Optional)
1. **Add Tags**: Tags help you organize and manage your AWS resources. 
   - **Key**: `Name`
   - **Value**: `MyS3Bucket`

### 4.5 Default Encryption (Optional)
1. **Default Encryption**: Enable server-side encryption if you want to encrypt objects stored in this bucket by default.

### 4.6 Advanced Settings (Optional)
1. Configure other advanced settings like Object Lock and Access Logs if needed for your use case.

### 4.7 Review and Create
1. Review all the configurations you have set. (Should all be left default)
2. Click **Create bucket** to create the bucket with the specified settings.

![image](https://github.com/user-attachments/assets/8c9b34bd-5f09-4fc6-906a-42970dc4475c)

## Step 5: Uploading Files to Your S3 Bucket
1. Navigate to the newly created bucket by clicking on its name in the S3 Dashboard.
2. Click the **Upload** button to upload files or folders to your bucket.
3. Drag and drop your files or use the **Add files** button to select them from your computer.
4. Click **Upload** to start the upload process.

![image](https://github.com/user-attachments/assets/bc3fa1a4-f60a-4420-b974-03037065a254)

## Step 6: Managing Bucket Permissions (Optional)
1. If you need to change the permissions for your bucket, go to the **Permissions** tab in your bucket settings.
2. Here, you can adjust the bucket policy, access control list (ACL), and CORS configuration according to your needs.

## Step 7: Accessing Your Files
1. After the files are uploaded, you can access them by navigating to your bucket and clicking on the object name.
2. Use the **Object URL** to access the file directly from the internet (if the bucket or object is public).

## Step 8: Deleting the Bucket (Optional)
1. If you no longer need the bucket, return to the S3 Dashboard.
2. Select the bucket you want to delete, click on **Delete** in the **Actions** menu.
3. Confirm the deletion by typing the bucket name in the confirmation prompt.
4. Click **Delete bucket** to remove the bucket and all its contents.

