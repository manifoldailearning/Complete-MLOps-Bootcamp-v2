name: Build, Test, and Deploy to AWS EC2

on:
  push:
    branches:
      - main

jobs:
  build_test_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python 
        uses: actions/setup-python@v3
        with:
          python-version: '3.10' 

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Tests
        run: python tests.py

      - name: Build Docker Image
        run: docker build -t my-flask-app:latest .

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@0e613a0980cbf65ed5b322eb7a1e075d28913a83
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@62f4f872db3836360b72999f4b87f1ff13310f3a

      - name: Push Docker Image to ECR
        run: |
          aws ecr get-login-password --region ${{ secrets.AWS_REGION }} | docker login --username AWS --password-stdin ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com
          docker tag my-flask-app:latest ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/my-flask-app:latest
          docker push ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/my-flask-app:latest    

      - name: Deploy to EC2
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.EC2_HOST }} 
          username: ${{ secrets.EC2_USERNAME }} 
          key: ${{ secrets.EC2_SSH_KEY }}  
          script: |
            docker pull ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/my-flask-app:latest
            docker stop my-flask-app || true # In case the container doesn't exist yet
            docker rm my-flask-app || true
            docker run -d -p 80:8080 --name my-flask-app ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/my-flask-app:latest 
