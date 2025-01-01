
# Automated Testing System (ATS)

This project is an Automated Testing System (ATS) designed to perform automated tests, track test results, and generate reports. It is built using Python, Flask for the backend, and React.js for the frontend. The system allows users to run tests, view results, and manage test configurations.

## Features
- **Test Execution**: Run automated tests on different environments.
- **Test Results Tracking**: View and analyze past test results.
- **Customizable Test Configurations**: Set up and manage test configurations.
- **Reports Generation**: Automatically generate detailed reports based on test execution.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Node.js and npm (for frontend)
- Flask (for backend)
- React.js (for frontend)
- Tailwind CSS (for styling)

## Installation

Follow these steps to get the project up and running:

### Clone the Repository
```bash
git clone https://github.com/your-username/automated-testing-system.git
cd automated-testing-system
```

### Set up Python Virtual Environment
Create a virtual environment to manage dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### Install Backend Dependencies
Install the necessary Python dependencies:
```bash
pip install -r requirements.txt
```

### Install Frontend Dependencies
Install the required Node.js dependencies for React:
```bash
cd frontend
npm install
```

### Running the Application
1. **Start the Flask Backend**:
   ```bash
   python app.py
   ```
   This will run the Flask app on `http://localhost:5000`.

2. **Start the React Frontend**:
   In a separate terminal, navigate to the `frontend` directory and run:
   ```bash
   npm start
   ```
   This will run the React app on `http://localhost:3000`.

## Project Structure

```
automated-testing-system/
│
├── app.py                   # Flask backend application
├── requirements.txt         # Python dependencies
├── frontend/                # Frontend React app
│   ├── src/
│   ├── public/
│   └── package.json
├── test_config/             # Test configurations
│   └── config.json
└── README.md                # Project documentation
```

## Usage

### Running Tests
- After logging in, you can trigger automated tests by selecting the tests you want to run and clicking the "Run Tests" button.

### Viewing Results
- Once tests are completed, you can view the results in the "Test Results" section of the dashboard. The results include details like pass/fail status, execution time, and logs.

### Managing Configurations
- The "Test Configurations" page allows you to set up and modify test configurations, including test environments, execution parameters, and test scripts.

## Deployment

To deploy the system to production, you can follow these steps:

### Deploy on Google Cloud (App Engine)
1. Create a Google Cloud project and enable App Engine.
2. Make sure the `app.yaml` file is correctly configured for your environment.
3. Run the following command to deploy:
   ```bash
   gcloud app deploy
   ```

### Docker (Optional)
If you prefer using Docker for deployment, you can build and run the app in a Docker container:
1. Build the Docker image:
   ```bash
   docker build -t ats-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 ats-app
   ```

## Contributing

We welcome contributions to the project. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit: `git commit -am 'Add new feature'`.
4. Push your branch: `git push origin feature-branch`.
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Flask, React.js, Tailwind CSS for the main technologies used in the project.
- Special thanks to contributors.

