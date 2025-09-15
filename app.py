
from flask import Flask, request, jsonify
from openai import AzureOpenAI
import pandas as pd
import os

app = Flask(__name__)

# --------------------------
# Azure OpenAI Configuration
# --------------------------
AZURE_API_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = "https://fiancemngmnt.openai.azure.com/"  
AZURE_API_VERSION = "2024-05-01-preview"
DEPLOYMENT_NAME = "Financemodel-genai" 


client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT
)

# --------------------------
# Routes
# --------------------------

@app.route("/")
def home():
    return " Azure OpenAI Financial Assistant is running!"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_query = data.get("query", "")

    # If no query provided
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    # Load transaction data
    try:
        df = pd.read_csv("transactions.csv")
    except FileNotFoundError:
        return jsonify({"error": "transactions.csv file not found"}), 500

    # Default context
    context = "Transaction data available."

    # Simple logic for different queries
    if "groceries" in user_query.lower():
        groceries_spent = df[df["category"] == "groceries"]["amount"].sum()
        context = f"You spent {groceries_spent} INR on groceries last month."
    elif "travel" in user_query.lower():
        travel_spent = df[df["category"] == "travel"]["amount"].sum()
        context = f"You spent {travel_spent} INR on travel last month."
    elif "rent" in user_query.lower():
        rent_spent = df[df["category"] == "rent"]["amount"].sum()
        context = f"Your rent payment last month was {rent_spent} INR."
    else:
        total_spent = df["amount"].sum()
        context = f"Your total spending last month was {total_spent} INR."

    # Call Azure OpenAI
    try:
        completion = client.chat.completions.create(
            model="Financemodel-genai",
            messages=[
                {"role": "system", "content": "You are a financial assistant. Answer based on transaction context."},
                {"role": "user", "content": f"{user_query}. Here is some context: {context}"}
            ]
        )
        ai_response = completion.choices[0].message.content
        return jsonify({"answer": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --------------------------
# Run the app
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)
