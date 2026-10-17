pipeline {
    agent any

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
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
