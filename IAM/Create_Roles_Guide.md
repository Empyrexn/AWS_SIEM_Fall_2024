### **Creating IAM Roles Using the AWS Management Console**

1. **Sign in to the AWS Management Console**
   - Open the [IAM console](https://console.aws.amazon.com/iam/).
   - In the left navigation pane, click on **Roles**.

2. **Create a New Role**
   - Click **Create role**.
   - Choose the type of trusted entity:
     - **AWS Service**: Select this for roles that AWS services (like EC2, Lambda) will assume.
     - **Another AWS Account**: Use this for cross-account access.
     - **Web Identity**: For roles assumed by federated users via an identity provider (like Amazon Cognito).
     - **SAML 2.0 Federation**: For roles assumed by users in a SAML-compliant identity provider.

3. **Select a Use Case**
   - Depending on your choice of trusted entity, you'll be prompted to select a use case. For example, for an EC2 instance, select **EC2**.

4. **Attach Permissions Policies**
   - Attach policies that define the permissions granted to the role.
   - You can select from AWS managed policies or create and attach a custom policy.
   - Example: For full access to S3, select the `AmazonS3FullAccess` policy.

5. **Set Permissions Boundary (Optional)**
   - A permissions boundary limits the maximum permissions that a role can have. This is optional but useful for controlling permissions.

6. **Add Tags (Optional)**
   - Tags are key-value pairs that can help organize and track roles. You can add them if needed.

7. **Review and Create Role**
   - Review the configuration, give the role a name, and add a description if necessary.
   - Click **Create role**.
