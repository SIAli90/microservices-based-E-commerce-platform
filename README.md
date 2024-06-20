# Microservices E-commerce Platform

This project demonstrates a microservices-based e-commerce platform using Rust, Python, and Elixir.

## Project Structure

- **inventory-service (Rust)**: Manages inventory.
- **user-service (Python)**: Manages user data.
- **order-service (Python)**: Manages orders.
- **payment-service (Elixir)**: Processes payments.

## Setup

### Prerequisites

- Rust
- Python 3
- Elixir

### Running the Inventory Service

```bash
cd inventory-service
cargo run
```

### Running the User Service

```bash
cd user-service
python app.py
```

### Running the Order Service

```bash
cd order-service
python app.py
```

### Running the Payment Service

```bash
cd payment-service
mix deps.get
iex -S mix
```

## Usage

1. Start the Inventory Service.
2. Start the User Service.
3. Start the Order Service.
4. Start the Payment Service.
