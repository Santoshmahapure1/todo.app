pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Santoshmahapure1/todo.app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t todo-app .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker stop todo-app || true'
                sh 'docker rm todo-app || true'
                sh 'docker run -d -p 5000:5000 --name todo-app todo-app'
            }
        }
    }
    post {
        success {
            echo 'App running at http://localhost:5000'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
