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
                sh '/usr/bin/python -m unittest discover'  // Adjust the path as needed
            }
        }
        stage('Build') {
            steps {
                sh '/usr/bin/python setup.py build'  // Adjust the path as needed
            }
        }
    }
}
