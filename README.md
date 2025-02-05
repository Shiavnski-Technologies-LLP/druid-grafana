
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

Once the services are up and running, you can access the following:

- **Druid UI**: [http://localhost:8888](http://localhost:8888)  
    This is the web interface for managing and monitoring Druid.
    
- **Grafana**: [http://localhost:3000](http://localhost:3000)  
    This is the dashboard for visualizing Druid data.  
    **Credentials**:
    
    - **Username**: `admin`
    - **Password**: `admin`

These services should now be accessible via the URLs above.

### 4. Ingest CSV Data 📄

To ingest **CSV data** into Druid:

1. Place your CSV file in the `/csv-data/` directory (or any other directory you've set for CSV files).
2. Trigger the ingestion task using a Python script or the Druid task API.

### 5. Custom Dashboards 📈

The project comes with pre-configured Grafana dashboards. You can view and modify these dashboards directly from the **Grafana UI** to visualize the ingested data.

### 6. Example Data Ingestion 📥

To ingest CSV data into Druid, you can use the `csv_ingestion_task.json` file. Ensure it is placed in the appropriate directory (`/opt/druid/var/tmp/`), and update any necessary configurations in Druid before triggering the task.

## ⚙️ Files Included 📂

Here are the important files included in this repository:

- **docker-compose.yml**: Defines the configuration for all Docker services.
- **environment**: Contains environment variables for the Druid services.
- **csv_ingestion_task.json**: Example task for ingesting CSV data into Druid.
- **grafana-dashboards/**: Pre-configured Grafana dashboards for visualizing Druid data.
- **/csv-data/**: Directory to store CSV files for ingestion into Druid.

## 📄 License 📝

This project is licensed under the MIT License. See the LICENSE file for details.
