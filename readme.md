# Campaign Management Web Application

This is a simple Campaign Management Web Application for managing marketing campaigns. It includes a backend built with FastAPI and a frontend built with React and TypeScript.

## Features

- Create a new campaign
- Run and stop a campaign
- List created campaigns with search functionality

## Backend Setup

### Prerequisites

- Python 3.7+
- SQLite (or any other preferred database)

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd /D:/projects/adcash
   ```

2. **Set up a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```sh
   uvicorn src.main:app --reload
   ```

5. **Access the API:**
   Open your browser and navigate to `http://127.0.0.1:8000` to see the "Hello World" message.

6. **API Documentation:**
   FastAPI provides interactive API documentation. You can access it at:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Filter Campaigns

You can filter campaigns by title, landing page URL, and is_running status.

- **URL:** `/campaigns/filter`
- **Method:** `GET`
- **Query Parameters:**
  - `title` (optional): Filter by campaign title.
  - `landing_page_url` (optional): Filter by landing page URL.
  - `is_running` (optional): Filter by running status.
  - `skip` (optional): Number of records to skip.
  - `limit` (optional): Maximum number of records to return.

Example request:
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/campaigns/filter?title=example&is_running=true' \
  -H 'accept: application/json'
```

## Frontend Setup

### Prerequisites

- Node.js
- npm or yarn

### Installation

1. **Navigate to the frontend directory:**
   ```sh
   cd frontend
   ```

2. **Install the dependencies:**
   ```sh
   npm install  # or yarn install
   ```

3. **Run the React application:**
   ```sh
   npm start  # or yarn start
   ```

4. **Access the frontend:**
   Open your browser and navigate to `http://localhost:3000` to see the application.

## Deployment to Amazon ECS

### Prerequisites

- AWS CLI configured with your credentials
- Amazon ECR repository created
- Amazon ECS cluster and service created
- ECS task definition JSON file created and stored in the repository

### Steps

1. **Set up GitHub Secrets:**
   Store your AWS credentials in GitHub Actions secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

2. **Update the GitHub Actions workflow:**
   Ensure the `.github/workflows/aws.yml` file is configured with your environment variables.

3. **Push to the main branch:**
   When you push changes to the `main` branch, the GitHub Actions workflow will automatically build and deploy your application to Amazon ECS.

4. **Monitor the deployment:**
   You can monitor the deployment process in the GitHub Actions tab of your repository.

## Contributing

Feel free to submit issues and pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License.