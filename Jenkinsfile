pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Task 3: Fetch the source code from GitHub
                checkout scm
            }
        }

        stage('Automated HTML Form Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest test_form.py'
                    } else {
                        // Use exact python path if Jenkins service user PATH differs, with fallback to standard python
                        bat '''
                        @echo off
                        if exist "C:\\Users\\abhyu\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" (
                            "C:\\Users\\abhyu\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m unittest test_form.py
                        ) else (
                            python -m unittest test_form.py
                        )
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline run completed."
        }
        success {
            echo "All HTML form validation tests passed successfully!"
        }
        failure {
            echo "Validation tests failed. Required form fields are missing or invalid."
        }
    }
}
