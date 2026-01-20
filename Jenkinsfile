
pipeline {
    agent any

    stages {
        stage('Checkout Info') {
            steps {
                echo "Pipeline triggered from GitHub"
                sh '''
                  pwd
                  ls -la
                '''
            }
        }

        stage('Basic Linux Commands') {
            steps {
                sh '''
                  whoami
                  uname -a
                  date
                '''
            }
        }
    }
}
