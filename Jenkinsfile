pipeline {
    agent {
        docker {
            image 'node:22.11.0-alpine3.20'
            // Optionally, you can add:
            // args '-u root'  // Runs as root user in the container if needed
        }
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
                withSonarQubeEnv('SonarQube') {  // Ensure 'SonarQube' matches your Jenkins setup
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
