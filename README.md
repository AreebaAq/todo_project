**Deploy Final Project to Aws through github, DockerFile and bash scripting.**
# Django Web App Deployment on AWS

This repository contains the code for a Django web app and provides instructions for deploying it on AWS using GitHub, bash scripting, and a Dockerfile.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [AWS account](https://aws.amazon.com/)
- [GitHub account](https://github.com/)

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/AreebaAq/todo_project.git)https://github.com/AreebaAq/todo_project.git
   Navigate your repository

![image](https://github.com/AreebaAq/todo_project/assets/152494545/a69c18be-3ea8-4c00-a6f8-2eb47768e2d1)

  ## Deploying to AWS
  
   1 Create an EC2 instance on AWS.
    
   2 Connect to your EC2 instance.

 ![image](https://github.com/AreebaAq/todo_project/assets/152494545/d520e74e-2ac6-46f2-b0d2-33e7f5416c6d)
    
   ## Install python and django
          # Update package lists
          sudo apt update
          
          # Install Python 3
          sudo apt install python3
          
          # Verify Python installation
          python3 --version

          # Install pip for Python 3
          sudo apt install python3-pip
          
          # Verify pip installation
          pip3 --version

 ![image](https://github.com/AreebaAq/todo_project/assets/152494545/bbdee287-4267-4db1-942b-276f4bdc99a

          
  ## Creating and running server (manual deploying)
  
    1 Add rule into security group for access
    
    2 Open settings.py and add ALLOWED_HOST=[*]

    3 Run server commnads
    
![image](https://github.com/AreebaAq/todo_project/assets/152494545/cd9aadb5-4e39-4fe6-94de-404c529c7d06)

 ## Application running in aws server        

![image](https://github.com/AreebaAq/todo_project/assets/152494545/990adaa9-ae51-449a-986e-9675153c9374)
## Application Deployment using Docker

    1 Add rule into security group for access
        
    2 Open settings.py and add ALLOWED_HOST=[*]

 ![image](https://github.com/AreebaAq/todo_project/assets/152494545/00795123-abaf-4353-b803-8a291c830a08)

       


