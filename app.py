from flask import Flask, request, render_template, jsonify
from openai import AzureOpenAI
import pandas as pd
import os
import re

app = Flask(__name__)

#AZURE OPENAI CONFIGURATION-------------------------
AZURE_API_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = "https://fiancemngmnt.openai.azure.com/"  
AZURE_API_VERSION = "2024-05-01-preview"
DEPLOYMENT_NAME = "Financemodel-genai" 

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask-ui", methods=["GET", "POST"])
def ask_ui():
    if request.method == "GET":
        return render_template("index.html")  

    user_query = request.form.get("query", "")
    if not user_query:
        return render_template("index.html", answer="Please enter a question.")

    csv_path=os.path.join(os.path.dirname(__file__),'transactions.csv')
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        return render_template("index.html", answer="Error: transactions.csv file not found")

    # Clean data: handle missing amounts
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    context = "Transaction data available."
    user_text = user_query.lower()
    matched = False

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

       
        months = {
            "january": 1, "february": 2, "march": 3, "april": 4,
            "may": 5, "june": 6, "july": 7, "august": 8,
            "september": 9, "october": 10, "november": 11, "december": 12
        }
        month_num = None
        for m, num in months.items():
            if m in user_text:
                month_num = num
                break
        year_match = re.search(r"\b(20\d{2})\b", user_text)
        year = int(year_match.group(1)) if year_match else None
        if month_num or year:
            filtered = df.copy()
            if month_num:
                filtered = filtered[filtered["date"].dt.month == month_num]
            if year:
                filtered = filtered[filtered["date"].dt.year == year]

            if filtered.empty:
                context = f"No spending records found for {month_num if month_num else ''} {year if year else ''}."
            else:
                df = filtered  

    
    for cat in df["category"].dropna().unique():
        pat = rf"\b{re.escape(cat.lower())}\b"
        if re.search(pat, user_text):
            spent = df[df["category"].str.lower() == cat.lower()]["amount"].sum()
            context = f"You spent {spent} INR on {cat}."
            matched = True
            break

    if not matched:
        total_spent = df["amount"].sum()
        context = f"Your total spending was {total_spent} INR."

    
    try:
        completion = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are a financial assistant. Answer based only on context provided."},
                {"role": "user", "content": f"Question: {user_query}\nContext: {context}"}
            ],
            temperature=0
        )
        answer = completion.choices[0].message.content
    except Exception as e:
        answer = f"Error calling Azure OpenAI: {str(e)}"

    return render_template("index.html", answer=answer)





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

