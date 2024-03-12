Deployment Steps to AWS EC2 Instance
=====================================

Step 1: Generate AWS Key Pair
------------------------------

1. Sign in to the AWS Management Console.
2. Navigate to the EC2 Dashboard.
3. Click on "Key Pairs" in the left-hand navigation pane.
4. Click on "Create Key Pair".
5. Enter a name for the key pair (e.g., `my-aws-key`) and click "Create Key Pair".
6. Download the private key file (`my-aws-key.pem`) to your local machine and ensure secure storage.

Step 2: Configure CircleCI
---------------------------

1. Open your project's CircleCI configuration file (`config.yml`).
2. Ensure that the `config.yml` file contains the necessary steps for building and deploying your Django app.
3. Replace placeholders (e.g., `YOUR_AWS_KEY.pem`, `YOUR_EC2_PUBLIC_IP`, `DOCKERHUB_USERNAME`, `DOCKERHUB_PASSWORD`) with your actual credentials and settings.
4. Commit the changes to your repository.

Step 3: Create EC2 Instance
----------------------------

1. Log in to the AWS Management Console.
2. Navigate to the EC2 Dashboard.
3. Click on "Launch Instance" to create a new EC2 instance.
4. Choose an Amazon Machine Image (AMI) for your instance.
5. Select an instance type (e.g., t2.micro).
6. Configure instance details, including network settings, security groups, and key pairs.
7. Review and launch the instance.
8. Connect to the EC2 instance using SSH.

Step 4: Set Up Docker and Docker Compose on EC2 Instance
---------------------------------------------------------

1. Once connected to the EC2 instance via SSH, update the package repositories: ::
   
       sudo apt-get update

2. Install Docker: ::
   
       sudo apt-get install -y docker.io

3. Install Docker Compose: ::
   
       sudo apt-get install -y docker-compose

Step 5: Prepare Django App for Deployment
------------------------------------------

1. Ensure that your Django project is configured for deployment with Docker and Docker Compose.
2. Update the `Dockerfile` and `docker-compose.yml` files as necessary.
3. Make sure all project dependencies are listed in the `requirements.txt` file.

Step 6: Push Code Changes and Trigger CI/CD Pipeline
-----------------------------------------------------

1. Commit and push any changes to your project repository.
2. CircleCI will automatically trigger the CI/CD pipeline.
3. CircleCI will build the Docker image, run unittests, push the image to DockerHub, and deploy the app to the EC2 instance.

Step 7: Verify Deployment
--------------------------

1. Once the deployment is complete, verify that the Django app is running on the EC2 instance.
2. Access the app using the EC2 instance's public IP address or domain name.

Conclusion
----------

This documentation provides a step-by-step guide for deploying your Django app to an AWS EC2 instance using CircleCI for continuous integration and continuous deployment (CI/CD).
