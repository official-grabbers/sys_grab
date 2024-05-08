# Sys Grab

**Brief Overview** : This powerful tool goes beyond the surface, providing comprehensive hardware information about your servers. It can currently extract details like system health, CPU capabilities, memory usage, disk performance, and network configuration. Essentially, it acts as a digital diagnostic tool, offering a clear picture of your server's inner workings.


## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Docker Installation](#docker-installation)
- [Running the Project](#running-the-project)
- [License](#license)

## Requirements

- Python (>=3.10)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/official-grabbers/sys_grab/
    ```

1. Navigate to the project directory:

    ```bash
    cd sys_grab
    ```

## Running the Project

1. To install the dependencies of this project

    ```
    pip3 install -r requirements.txt
    ```

1. To run the project on your machine

    ```
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
    ```

The development server will be running at http://localhost:8080/ or http://127.0.0.1:8080/.

## Docker Installation

To run the application using Docker, follow these steps:

1. Build the Docker image:

    ```
    docker-compose build
    ```
2. Run the Docker container:

    ```
    docker-compose up -d
    ```

The development server will be running at http://localhost:8080/ or http://127.0.0.1:8080/.

## License
- None