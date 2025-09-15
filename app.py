from flask import Flask, request, render_template, jsonify
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
    # Load the UI directly
    return render_template("index.html")


@app.route("/ask-ui", methods=["GET", "POST"])
def ask_ui():
    user_query = request.form.get("query", "")
    answer = None

    if not user_query:
        return render_template("index.html", answer="Please enter a question.")

    # Load transaction data
    try:
        df = pd.read_csv("transactions.csv")
    except FileNotFoundError:
        return render_template("index.html", answer="Error: transactions.csv file not found")

    # Context logic
    context = "Transaction data available."
    matched=False

     # Dynamic check for categories
    categories = df["category"].unique()
    for cat in categories:
        if cat.lower() in user_query.lower():
            spent = df[df["category"].str.lower() == cat.lower()]["amount"].sum()
            context = f"You spent {spent} INR on {cat} last month."
            matched = True
            break
                
    if not matched:
        total_spent = df["amount"].sum()
        context = f"Your total spending last month was {total_spent} INR." 
              

    # if "groceries" in user_query.lower():
    #     groceries_spent = df[df["category"] == "groceries"]["amount"].sum()
    #     context = f"You spent {groceries_spent} INR on groceries last month."
    # elif "travel" in user_query.lower():
    #     travel_spent = df[df["category"] == "travel"]["amount"].sum()
    #     context = f"You spent {travel_spent} INR on travel last month."
    # elif "rent" in user_query.lower():
    #     rent_spent = df[df["category"] == "rent"]["amount"].sum()
    #     context = f"Your rent payment last month was {rent_spent} INR."
    # else:
    #     total_spent = df["amount"].sum()
    #     context = f"Your total spending last month was {total_spent} INR."

    # Call Azure OpenAI
    try:
        completion = client.chat.completions.create(
            model="Financemodel-genai",
            messages=[
                {"role": "system", "content": "You are a financial assistant. Answer based on transaction context."},
                {"role": "user", "content": f"{user_query}. Here is some context: {context}"}
            ]
        )
        answer = completion.choices[0].message.content
    except Exception as e:
        answer = f"Error calling Azure OpenAI: {str(e)}"

    return render_template("index.html", answer=answer)


# --------------------------
# Run the app
# --------------------------
if __name__ == "__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
