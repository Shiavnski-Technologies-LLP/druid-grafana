
# 🐳 Druid POCD Project 🚀

Welcome to the **Druid POCD** project! This repository demonstrates the setup of a **Druid cluster** integrated with **PostgreSQL**, **Zookeeper**, and **Grafana** using **Docker** and **Docker Compose**. The primary goal of this project is to establish a Druid cluster, automate **CSV ingestion**, and visualize data with **Grafana**.

## 🛠️ Project Setup

Follow the steps below to get the project running on your local machine:

### 1. Clone the Repository 🔽

Clone this repository to your local environment:

```bash
git clone https://github.com/Shiavnski-Technologies-LLP/druid-grafana.git
cd druid-grafana-main
````

### 2. Start the Services with Docker Compose 🚀

To bring up all services, use the `docker-compose.yml` file. Run the following command in the project directory:

```bash
docker-compose up -d
```

This command will:

- Build and start the following services:
    - **PostgreSQL** 🗃️: Database for Druid
    - **Zookeeper** 🦸: Druid coordination service
    - **Druid** 🌲: Includes Coordinator, Broker, Historical, MiddleManager, and Router
    - **Grafana** 📊: Data visualization dashboard

The `-d` flag will run the services in **detached mode**, meaning they will run in the background.

### 3. Access the Services 🌐

