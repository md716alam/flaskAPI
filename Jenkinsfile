pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-app:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        docker.withRegistry('', 'docker-hub') {
                            docker.image("my-app:${BUILD_NUMBER}").push()
                        }
                    }
                }
            }
        }
    }
}
