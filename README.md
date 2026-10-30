# Cryptocurrency Analytics Dashboard

A small data collection and visualization stack using CoinGecko, InfluxDB, Grafana, Python and Docker Compose. The dashboard tracks BTC, ETH and DOGE prices.

## Stack

- Python for fetching market data
- CoinGecko API as a market-data source
- InfluxDB 2.7 for time-series storage
- Grafana for visualization
- Docker Compose for local deployment

## Run locally

1. Install Docker Engine and the Docker Compose plugin.
2. Copy the environment template:

```bash
cp .env.example .env
```

3. Replace every placeholder in `.env` with unique credentials and a long random InfluxDB admin token. Never commit the real `.env` file.
4. Start the services:

```bash
docker compose up -d
docker compose ps
docker compose logs -f
```

5. Open Grafana at `http://localhost:3000` and InfluxDB at `http://localhost:8086`. Use the credentials configured in `.env`.

## Security notes

- The Compose file intentionally refuses to start if required passwords or tokens are missing.
- Keep `.env` private and restrict access to it.
- Do not expose the database or Grafana ports directly to an untrusted network. Use a firewall and HTTPS reverse proxy for remote access.
- The InfluxDB initialization variables are used when the data directory is initialized for the first time. Changing values in `.env` later does not automatically rotate credentials in an already initialized database.

## Dashboard preview

![Sample dashboard showing BTC, ETH and DOGE prices](https://github.com/user-attachments/assets/e81416c9-9ad5-409f-8060-8e57e99dd4b0)
