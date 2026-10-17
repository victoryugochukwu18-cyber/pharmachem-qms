import os
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(file))

app = Flask(
name,
template_folder=os.path.join(BASE_DIR, "templates"),
static_folder=os.path.join(BASE_DIR, "static")
)

modules = [
"Document Control",
"Deviation Management",
"CAPA",
"Change Control",
"Training Management",
"Audit Management",
"Risk Management",
"Complaints Management",
"Supplier Management",
"Quality Records"
]

records = []

@app.route("/")
def home():
return render_template(
"index.html",
total=len(records),
modules=modules
)

@app.route("/api/records", methods=["GET", "POST"])
def manage_records():
if request.method == "POST":
data = request.get_json(silent=True) or {}

    record = {
        "id": len(records) + 1,
        "module": data.get("module", "General"),
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "status": data.get("status", "Open")
    }

    records.append(record)

    return jsonify({
        "success": True,
        "record": record,
        "total": len(records)
    }), 201

module = request.args.get("module")

if module:
    filtered = [
        record for record in records
        if record["module"] == module
    ]
    return jsonify(filtered)

return jsonify(records)

if name == "main":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))