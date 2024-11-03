pipeline {
    agent {
        docker { image 'node:22.11.0-alpine3.20' }
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // Add build commands here, such as `npm install`
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                }
                // Replace 'SonarQube' with your actual SonarQube installation name
                withSonarQubeEnv('SonarQube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
