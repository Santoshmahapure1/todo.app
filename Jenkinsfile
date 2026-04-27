pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repo...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo Build complete!'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'echo Tests passed!'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'echo Deployed!'
            }
        }
    }
}
