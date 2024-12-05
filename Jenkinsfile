pipeline {
    agent any
    
    environment {
        NODE_HOME = '/usr/local/bin/node' // Adjust if needed
    }

    stages {
        // Stage 1: Checkout the repository from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2: Install Backend Dependencies (in 'server' directory)
        stage('Install Backend Dependencies') {
            steps {
                dir('server') { // Change to the backend directory
                    script {
                        // Install backend dependencies using npm
                        sh 'npm install'
                    }
                }
            }
        }

        // Stage 3: Install Frontend Dependencies (in 'src' directory)
        stage('Install Frontend Dependencies') {
            steps {
                dir('src') { // Change to the frontend directory
                    script {
                        // Install frontend dependencies using npm
                        sh 'npm install'
                    }
                }
            }
        }

        // Stage 4: Run Backend Tests (optional)
        stage('Backend Tests') {
            steps {
                dir('server') {
                    script {
                        // Run backend tests (e.g., using Jest or Mocha)
                        sh 'npm test'
                    }
                }
            }
        }

        // Stage 5: Run Frontend Tests (optional)
        stage('Frontend Tests') {
            steps {
                dir('src') {
                    script {
                        // Run frontend tests (e.g., using Jest or React Testing Library)
                        sh 'npm test'
                    }
                }
            }
        }

        // Stage 6: Build Frontend (for production)
        stage('Build Frontend') {
            steps {
                dir('src') {
                    script {
                        // Build the frontend for production (React app)
                        sh 'npm run build'
                    }
                }
            }
        }

        // Stage 7: Build Backend (optional - for Docker)
        stage('Build Backend') {
            steps {
                dir('server') {
                    script {
                        // Optionally, you can build a Docker container for the backend
                        sh 'docker build -t my-backend .'
                    }
                }
            }
        }

        // Stage 8: Deploy Backend and Frontend
        stage('Deploy') {
            steps {
                script {
                    // Deploy backend (e.g., with Docker)
                    sh 'docker run -d -p 5000:5000 my-backend'

                    // Deploy frontend (e.g., to AWS S3, Netlify, or similar)
                    // Example: AWS S3 deployment
                    // sh 'aws s3 sync ./src/build/ s3://your-bucket-name'
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean up workspace after build
        }

        failure {
            echo 'Build failed!'
        }
    }
}
