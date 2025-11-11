from flask import Flask, jsonify, request
import random
import time

app = Flask(__name__)

@app.route("/api/version")
def version():
    """Return faulty deployment info"""
    return jsonify({
        "version": "a1b2c3d",
        "commit": "a1b2c3d",
        "status": "unstable",
        "deployed_at": "2025-08-22T14:01:10Z"
    }), 200

@app.route("/api/checkout", methods=["POST"])
def checkout():
    """Simulate 95% checkout failure rate"""
    time.sleep(random.uniform(0.5, 3.5))  # Simulate latency spike
    if random.random() < 0.95:
        error_messages = [
            "NullReferenceException in PaymentProcessor.js:174",
            "TimeoutError: PayPal API did not respond",
            "Database connection lost while committing transaction",
            "500 Internal Server Error - CheckoutService"
        ]
        return jsonify({
            "success": False,
            "error": random.choice(error_messages),
            "status": "failed",
            "version": "a1b2c3d"
        }), 500

    # Rare successful transaction (5% chance)
    return jsonify({
        "success": True,
        "message": "Checkout completed successfully (unstable)",
        "transaction_id": f"TXN-{int(time.time())}",
        "version": "a1b2c3d"
    }), 200

@app.route("/health")
def health():
    """Simulate degraded health"""
    failure_rate = 95
    return jsonify({
        "service": "checkout-service",
        "status": "DOWN" if random.random() < 0.8 else "DEGRADED",
        "latency": f"{random.randint(800, 2500)}ms",
        "errorRate": f"{failure_rate}%",
        "version": "a1b2c3d",
        "lastError": "NullReferenceException in PaymentProcessor.js:174"
    }), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
