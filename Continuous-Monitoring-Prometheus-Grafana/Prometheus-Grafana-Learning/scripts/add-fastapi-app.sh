#!/bin/bash
echo "  - job_name: 'app'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:8005']" >> /etc/prometheus/prometheus.yml
