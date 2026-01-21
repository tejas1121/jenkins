pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                  docker version
                  docker build -t python-backend:ci -f backend/Dockerfile backend


                '''
            }
        }

        stage('Verify Image') {
            steps {
                sh '''
                  docker images | grep python-backend
                '''
            }
        }
    }
}
