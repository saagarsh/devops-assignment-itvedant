pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1' 
        AWS_ACCOUNT_ID = '540547083417'
        ECR_REPO_NAME = 'devops-assignment-itvedant'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        FULL_IMAGE_NAME = "${ECR_REGISTRY}/${ECR_REPO_NAME}"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out by Jenkins'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -s app -p "test_*.py" -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-assignment-itvedant:local .'
            }
        }

        stage('Push to ECR') {
            steps {
                withCredentials([string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),
                                 string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh """
                        # Authenticate Docker to ECR
                        aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}
                        
                        # Tag the image
                        docker tag devops-assignment-itvedant:local ${FULL_IMAGE_NAME}:${IMAGE_TAG}
                        docker tag devops-assignment-itvedant:local ${FULL_IMAGE_NAME}:latest
                        
                        # Push to ECR
                        docker push ${FULL_IMAGE_NAME}:${IMAGE_TAG}
                        docker push ${FULL_IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Update the deployment with the new image
                sh "kubectl set image deployment/devops-app devops-app=${FULL_IMAGE_NAME}:${IMAGE_TAG}"
                
                // Wait for the rollout to finish successfully
                sh "kubectl rollout status deployment/devops-app"
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully! App deployed to EKS.'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
