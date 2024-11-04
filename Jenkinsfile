pipeline {
    agent any
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
                withSonarQubeEnv('Sonar-scanner-1') {  // Ensure 'SonarQube' matches your Jenkins setup
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
