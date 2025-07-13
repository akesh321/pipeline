pipeline {
    agent any
    environment {
        JENKINS_HOME = '/var/lib/jenkins'
        CUSTOM_WORK_DIR = "${JENKINS_HOME}/custom-workspace"
        GIT_REPO = 'https://github.com/your-org/kafka-pipeline-demo.git'
        PRODUCER_SCRIPT = 'producer.py'
        CONSUMER_SCRIPT = 'consumer.py'
        TEST_MESSAGE = 'Hello from Jenkins'
        KAFKA_TOPIC = 'jenkins-test-topic'
        BOOTSTRAP_SERVERS = 'localhost:9092'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: "${GIT_REPO}"
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }
        stage('Start Consumer') {
            steps {
                script {
                    // Start consumer in background
                    sh "nohup python3 ${CONSUMER_SCRIPT} --topic ${KAFKA_TOPIC} --bootstrap-server ${BOOTSTRAP_SERVERS} > consumer.log 2>&1 & echo \$! > consumer.pid"
                }
            }
        }
        stage('Run Producer') {
            steps {
                sh "python3 ${PRODUCER_SCRIPT} --topic ${KAFKA_TOPIC} --message \"${TEST_MESSAGE}\" --bootstrap-server ${BOOTSTRAP_SERVERS}"
            }
        }
        stage('Verify Message Received') {
            steps {
                script {
                    sleep 5 // give consumer time to receive
                    def result = sh(script: "grep '${TEST_MESSAGE}' consumer.log || true", returnStdout: true).trim()
                    if (result == "") {
                        error("Message not received by consumer!")
                    } else {
                        echo "Consumer received message: ${result}"
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh 'kill $(cat consumer.pid) || true'
            sh 'rm -f consumer.pid consumer.log'
        }
    }
}
