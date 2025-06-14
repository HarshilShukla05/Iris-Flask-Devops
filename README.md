# Iris Species Prediction API

This project provides a RESTful API for predicting the species of an Iris flower based on its sepal and petal measurements. It uses a machine learning model trained on the classic Iris dataset.

## API Endpoints

### GET /

- **Description:** Returns a welcome message and confirms the API is running.
- **Method:** `GET`
- **Response:**
  ```json
  {
    "message": "Iris Species Prediction API"
  }
  ```

### POST /predict

- **Description:** Predicts the Iris species based on input features.
- **Method:** `POST`
- **Request Body:** `application/json`
  ```json
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }
  ```
- **Response (Success):** `application/json`
  ```json
  {
    "species": "setosa"
  }
  ```
- **Response (Error):** `application/json`
  ```json
  {
    "error": "Invalid input data"
  }
  ```

## Training the Model

To train the Iris species prediction model, follow these steps:

1.  **Install Dependencies:**
    The required Python libraries are listed in `requirements.txt`. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Training Script:**
    Execute the training script located at `app/train_iris_model.py`:
    ```bash
    python app/train_iris_model.py
    ```
    This will train the model and save it to a file (e.g., `iris_model.pkl`) which will be used by the API.

## Running the Application Locally

To run the Iris Species Prediction API locally, follow these steps:

1.  **Install Dependencies:**
    If you haven't already, install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Environment Variables:**
    The application uses the following environment variables:
    - `PORT`: The port on which the Flask application will run (e.g., `5000`).
    - `MODEL_FILE`: Path to the trained model file (e.g., `iris_model.pkl`).
    - `SPECIES_MAP_FILE`: Path to the JSON file mapping class indices to species names (e.g., `species_map.json`).
    - `DEBUG`: Set to `True` for Flask debug mode, `False` otherwise.

    You can set these variables in your shell or create a `.env` file in the project root. The application uses `python-dotenv` to load variables from a `.env` file automatically.
    Example `.env` file:
    ```
    PORT=5000
    MODEL_FILE=iris_model.pkl
    SPECIES_MAP_FILE=species_map.json
    DEBUG=True
    ```

3.  **Run the Application:**
    The main entry point for the application is `app/main.py`.

    You can run the application directly using Python:
    ```bash
    python app/main.py
    ```
    Alternatively, if you have Flask installed and environment variables set (or a `.env` file is present), you can use the `flask` command:
    ```bash
    flask run --host=0.0.0.0 --port=${PORT:-5000}
    ```
    (The `${PORT:-5000}` syntax will use the PORT environment variable if set, otherwise default to 5000).

    The API will then be accessible at `http://localhost:<PORT>`.

## Running with Docker

This project includes a `Dockerfile` and `docker-compose.yml` for containerized deployment.

1.  **Build the Docker Image:**
    From the project root directory, build the Docker image:
    ```bash
    docker build -t iris-api .
    ```

2.  **Run with Docker:**
    You can run the container directly using `docker run`. You'll need to map the port and pass environment variables. If you have a `.env` file, you can use the `--env-file` option.
    ```bash
    # Ensure your .env file is configured as described in "Running the Application Locally"
    # The -e PORT=5000 is still useful if .env doesn't specify PORT or for overriding
    docker run -p 5000:5000 -e PORT=5000 --env-file .env iris-api
    ```
    *Note: The Dockerfile is set up to use port 5000 by default if the PORT environment variable is not set.*

3.  **Run with Docker Compose:**
    Alternatively, you can use Docker Compose to manage the application container. Docker Compose will automatically use the `.env` file in the project root to configure environment variables for the service.
    ```bash
    # This command builds the image if not already built, and starts the service
    docker-compose up
    ```
    To run in detached mode:
    ```bash
    docker-compose up -d
    ```
    The API will be accessible at `http://localhost:5000` (or the port specified in your `.env` file if `docker-compose.yml` is configured to use it).

## Deployment

### Kubernetes

Kubernetes configuration files for deploying the application are available in the `k8s/` directory.

### Infrastructure (Terraform)

Terraform configuration files for setting up the required infrastructure are available in the `infra/` directory.
