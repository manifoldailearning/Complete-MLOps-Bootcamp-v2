
# Querying Prometheus
https://prometheus.io/docs/prometheus/latest/querying/basics/


# Installation Steps for Prometheus
- Launch an EC2 instance with Ubuntu and run the below commands
- Open the traffic for all the ports (All Traffic - anywhere ipv4)

```
sudo su -
git clone https://github.com/manifoldailearning/Prometheus-Grafana-Docs
cd Prometheus-Grafana-Docs/scripts

chmod u=rwx,g=r,o=r 1-install.sh
./1-install.sh
ps aux | grep prometheus
sudo service prometheus start
sudo service prometheus status

cat /etc/prometheus/prometheus.yml

chmod u=rwx,g=r,o=r 3-install-grafana.sh
./3-install-grafana.sh
sudo service grafana-server status

# default username & password is : admin

ps uax | grep prometheus

cat /etc/prometheus/prometheus.yml

```
# Install Node Exporter
- Run the script
chmod u=rwx,g=r,o=r 2-node-exporter.sh
./2-node-exporter.sh
```
sudo apt-get install vim -y
sudo update-alternatives --config vi

vim /etc/prometheus/prometheus.yml
  - job_name: 'node_exporter'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9100']


sudo service prometheus restart
```
```
localhost:9090 --> Prometheus
localhost:3000 --> grafana
curl localhost:9100 --> node exporter
curl localhost:9100/metrics
```
https://pypi.org/project/prometheus-client/

# Install Docker 
- Run the script
```
chmod u=rwx,g=r,o=r 4-install-docker.sh
./4-install-docker.sh
cd ..
cd fast-api-metrics
docker build -t fast-api .

echo "  - job_name: 'app'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:8005']" >> /etc/prometheus/prometheus.yml

docker run -d -p 8005:8005 fast-api

localhost:8005 --> FastAPI
localhost:8005/docs --> Documentation
localhost:8005/metrics --> monitoring

sudo service prometheus restart

docker ps
```