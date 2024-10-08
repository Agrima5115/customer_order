# Small Revenue and Customer Metrics Application Deployed on AWS

This application processes customer orders from a CSV file and provides insights such as total revenue generated by month, by product, and by customer. It also identifies the top 10 customers by revenue. The application is containerized using Docker and deployed on an AWS EC2 instance.

# Table of Contents

1. [Introduction](#small-revenue-and-customer-metrics-application-deployed-on-aws)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Deployment](#deployment)
7. [Screenshots](#screenshots)
8. [Project Structure](#project-structure)

## Features

- Process customer orders from a CSV file.
- Compute total revenue by month, by product, and by customer.
- Identify the top 10 customers by revenue.
- Containerized using Docker for easy deployment.

## Tech Stack

| **Technology** | **Purpose**          |
|----------------|----------------------|
| Python         | Application logic    |
| Docker         | Containerization     |
| AWS EC2        | Cloud                |
| PuTTY          | Remote connections   |
| FileZilla      | File transfers       |

## Prerequisites

- Docker installed on your local machine.
- AWS account with access to create and manage EC2 instances.
- Git installed on your local machine.
- [PuTTY](https://www.putty.org/) installed on your local machine.
- [FileZilla](https://filezilla-project.org/) installed on your local machine.

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/Agrima5115/customer_order.git
    cd customer_order
    ```

2. **Build the Docker Image:**
    ```sh
    docker-compose build
    ```

3. **Run the Docker Container:**
    ```sh
    docker-compose up
    ```

3. **Get the Output:**
    ```sh
    cd app
    python app.py
    ```

## Deployment

### Launch an EC2 Instance
1. **Create a new EC2 instance on AWS:**
    - Choose Ubuntu as the AMI.
    - Select an instance type (e.g., t3.micro for free tier).
    - Configure the security group and allow HTTP and HTTPS traffic from the internet.

2. **Create and Download the key pair (.pem file):**
    - Save the key pair file securely; you will need it to connect to your EC2 instance.

### Connect to the EC2 Instance using PuTTY
1. **Convert the .pem file to .ppk using PuTTYgen:**
    - Open PuTTYgen, click "Load," and select your .pem file.
    - Click "Save private key" to save the .ppk file.

2. **Connect to your EC2 instance:**
    - Open PuTTY, enter your EC2 instance's public DNS in the "Host Name" field.
    - In the "Connection" > "SSH" > "Auth" > "Credentials" section, browse and select your .ppk file.
    - Click "Open" to connect.

### Transfer Files using FileZilla
1. **Open FileZilla and go to "File" > "Site Manager":**
    - Click "New Site" and enter your EC2 instance details:
        - Protocol: SFTP
        - Host: Your EC2 instance's public DNS
        - Logon Type: Key file
        - User: `ec2-user` (for Amazon Linux) or `ubuntu` (for Ubuntu)
        - Key file: Browse and select your .ppk file

2. **Transfer the application files:**
    - Connect to your EC2 instance in FileZilla.
    - Drag and drop your application files from your local machine to the EC2 instance.

### Install Docker on EC2
1. **Connect to the EC2 instance using PuTTY:**
    - Use the same steps as above to connect via SSH.

2. **Install Docker:**
    ```sh
    sudo apt-get update
    
    sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    sudo apt-get install docker-ce docker-ce-cli containerd.io

    apt-cache madison docker-ce

    sudo apt-get install docker-ce docker-ce-cli containerd.io

    sudo apt install docker.io

    sudo apt install docker-compose
   
    ```

### Deploy the Docker Container on EC2
  **Transfer your Docker image to the EC2 instance or build it directly on the instance:**
 ```sh
    sudo docker-compose build
    sudo docker-compose up
    cd app
    python3 app.py
```

## Screenshots

<img src="https://github.com/user-attachments/assets/6e246ecb-9326-40df-8d08-1e321d582814" alt="ss1" width="400" height="300" style="margin-right: 20px;">
<img src="https://github.com/user-attachments/assets/5556b6d6-8d5f-4158-a066-641b07363b99" alt="ss2" width="400" height="300" style="margin-right: 20px;">
<img src="https://github.com/user-attachments/assets/9ddba210-d1ac-42bc-b69d-12ba33d750d3" alt="ss3" width="400" height="300" style="margin-right: 20px;">
<img src="https://github.com/user-attachments/assets/8f568214-75b2-442f-b263-c8b49886f965" alt="ss4" width="400" height="300" style="margin-right: 20px;">
<img src="https://github.com/user-attachments/assets/22b8448b-5f78-44b1-acbe-38e6858bde69" alt="ss5" width="400" height="300" style="margin-right: 20px;">
<img src="https://github.com/user-attachments/assets/af56ebd6-c923-48d8-9a59-658369377d13" alt="ss6" width="400" height="300" style="margin-right: 20px;">
<img src="https://github.com/user-attachments/assets/f6b0ecc2-4d1f-4ba2-a54b-404849f7484c" alt="ss7" width="400" height="300" style="margin-right: 20px;">
<img src="https://github.com/user-attachments/assets/8c96ecc7-7b85-4134-8dfe-a2d791bf7de2" alt="ss8" width="400" height="300" style="margin-right: 20px;">

## Project Structure
```sh
customer/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .vscode/
│   ├── launch.json
│   ├── settings.json
├── app/
│   ├── app.py
│   ├── orders.csv
│   ├── test_app.py
├── Dockerfile
├── docker-compose.yml
├── orders.ppk
└── README.md
```
