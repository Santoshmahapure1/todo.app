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
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f ~/Downloads/todo-deployment.yaml'
            }
        }
        stage('Nagios Monitor') {
            steps {
                sh 'echo "App deployed - Nagios is monitoring!"'
                sh 'curl -s http://127.0.0.1/nagios/ -u nagiosadmin:nagios123 || echo "Nagios notified"'
            }
        }
    }
}
