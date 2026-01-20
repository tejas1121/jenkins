pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout Info') {
            steps {
                echo "Triggered by GitHub SCM polling"
                sh '''
                  git log -1 --oneline
                '''
            }
        }
    }
}
