pipeline {
    agent any 
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                sh '/usr/bin/python3 -m unittest discover'  // Adjust the path as needed
            }
        }
        stage('Build') {
            steps {
                sh '/usr/bin/python3 setup.py build'  // Adjust the path as needed
            }
        }
    }
}
