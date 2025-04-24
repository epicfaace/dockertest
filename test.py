from flask import Flask, jsonify, abort
from flask_login import LoginManager, login_required, current_user
from models import Invoice  # SQLAlchemy model

app = Flask(__name__)
login_manager = LoginManager(app)

@app.route("/invoice/<int:invoice_id>", methods=["GET"])
@login_required  # ✅ checks user is logged in
def get_invoice(invoice_id):
    """
    INTENTIONALLY VULNERABLE:
    - No per-object authorization; any authenticated user
      can request /invoice/123 and view someone else’s data.
    """
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        abort(404)

    # ❌ Missing: `if invoice.owner_id != current_user.id: abort(403)`
    return jsonify(invoice.to_dict())  # Sensitive data leaked!

if __name__ == "__main__":
    app.run(debug=True)
