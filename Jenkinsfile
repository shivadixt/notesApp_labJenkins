pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:shivadixt/notesApp_labJenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v
                '''
            }
        }
    }

    post {
        success {
            echo 'Tests passed! Pipeline completed successfully.'
        }
        failure {
            echo 'Something failed — check the logs above.'
        }
    }
}
