from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route("/api/version")
def version():
    return jsonify({
        "version": "main-stable",
        "commit": "z9y8x7w",
        "status": "healthy",
        "deployed_at": "2025-08-21T09:00:00Z"
    }), 200

@app.route("/api/checkout", methods=["POST"])
def checkout():
    """Simulate successful checkout process"""
    data = request.get_json()
    promo = data.get("promo_code", None)
    total = 100
    if promo == "SAVE10":
        total *= 0.9

    return jsonify({
        "success": True,
        "message": "Checkout completed successfully.",
        "promo_applied": promo if promo else "None",
        "final_amount": total,
        "transaction_id": f"TXN-{int(time.time())}"
    }), 200

@app.route("/health")
def health():
    return jsonify({
        "service": "checkout-service",
        "status": "UP",
        "latency": "120ms",
        "errorRate": "0.5%",
        "version": "main-stable"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
