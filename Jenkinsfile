pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'santoshmahapure1'
        IMAGE_NAME = 'todo-app'
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Santoshmahapure1/todo.app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB_USER/$IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker stop todo-app || true'
                sh 'docker rm todo-app || true'
                sh 'docker run -d -p 5000:5000 --name todo-app $DOCKER_HUB_USER/$IMAGE_NAME:latest'
            }
        }

        stage('Verify App') {
            steps {
                sh 'sleep 3'
                sh 'curl -s http://localhost:5000 | grep -i "todo" && echo "✅ App is UP!" || echo "❌ App not responding"'
            }
        }
    }

    post {
        success {
            echo '✅ SUCCESS - App live at http://localhost:5000'
            echo '✅ Image at hub.docker.com/r/santoshmahapure1/todo-app'
        }
        failure {
            echo '❌ Pipeline FAILED - Check logs'
        }
    }
}
