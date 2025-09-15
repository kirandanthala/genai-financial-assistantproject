# GenAI-Powered Financial Insights Assistant  

## 🎯 Objective  
A GenAI-powered assistant that provides personalized financial insights based on user queries and transaction data.  
- Accepts natural language queries (e.g., *“How much did I spend on groceries last month?”*)  
- Analyzes structured transaction data (`transactions.csv`)  
- Uses **Azure OpenAI (GPT deployment)** to generate financial summaries  
- Provides actionable insights (spending trends, saving tips)  
- Accessible via a simple **web interface** (`/ask-ui`)  

---

## Project Structure
genai-financial-assistantproject/
│-- app.py # Flask application
│-- requirements.txt # Dependencies
│-- transactions.csv # Sample transaction dataset
│-- templates/
└── index.html # Web interface
│-- README.md # Documentation

yaml
Copy code

---

## ⚙️ Setup Instructions  

### 1. Clone the Repository  

git clone https://github.com/<your-username>/genai-financial-assistantproject.git
cd genai-financial-assistantproject
2. Create Virtual Environment & Install Requirements
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
pip install -r requirements.txt

3. Run Locally
python app.py
Open in browser: http://127.0.0.1:5000

 Azure Deployment
Deployed using Azure App Service (Linux, Python runtime)

Environment Variables (Configuration → Application Settings):

AZURE_OPENAI_KEY → AZURE_API_KEY

AZURE_ENDPOINT →  https://fiancemngmnt.openai.azure.com/

AZURE_DEPLOYMENT → Financemodel-genai

Public URL:

https://<your-app-name>.azurewebsites.net/
🌐 Usage
Web Interface: / or /ask-ui
Accessible in any browser:

https://<your-app-name>.azurewebsites.net/
Shows a text box to enter queries

Displays AI response directly below

User Story 1 – Category Spending (e.g., groceries, shopping, medicine)

TC1.1 – Query groceries spending

Preconditions: transactions.csv has category = groceries.

Steps:

Open Web UI.

1.Enter: “How much did I spend on groceries last month?”

2.Submit.

Expected Result: System returns grocery total from CSV.

Actual Result: (to be filled during testing)

TC1.2 – Query shopping spending

Preconditions: transactions.csv has category = shopping.

Steps:

Open Web UI.

1.Enter: “How much on shopping last month?”

2.Submit.

Expected Result: System returns shopping total.

Actual Result: (to be filled)

TC1.3 – Query medicine spending

Preconditions: transactions.csv has category = medicine.

Steps:

Open Web UI.

1.Enter: “What about medicine expenses?”

2.Submit.

Expected Result: System returns medicine total.

Actual Result: (to be filled)

TC1.4 – (Negative) Unknown category

Preconditions: transactions.csv does NOT have category = movies.

Steps:

Open Web UI.

1.Enter: “How much did I spend on movies last month?”

2.Submit.

Expected Result: System returns total spending (fallback).

Actual Result: (to be filled)

User Story 2 – Rent Spending

TC2.1 – Query rent

Preconditions: transactions.csv has category = rent.

Steps:

Open Web UI.

1.Enter: “What was my rent last month?”

2.Submit.

Expected Result: System returns rent amount.

Actual Result: (to be filled)

TC2.2 – Rent alternative wording

Preconditions: Same CSV.

Steps:

1.Enter: “Tell me my house rent last month”.

2.Submit.

Expected Result: System returns rent amount.

Actual Result: (to be filled)

TC2.3 – Rent case-insensitive

Preconditions: Same CSV.

Steps:

1.Enter: “rent” (lowercase).

2.Submit.

Expected Result: System returns rent amount.

Actual Result: (to be filled)

TC2.4 – (Negative) Rent missing

Preconditions: transactions.csv does NOT have category = rent.

Steps:

1.Enter: “What was my rent last month?”

2.Submit.

Expected Result: System falls back → total spending.

Actual Result: (to be filled)

User Story 3 – Analyst Spending Trends

TC3.1 – Query travel

Preconditions: transactions.csv has category = travel.

Steps:

1.Enter: “How much did I spend on travel last month?”

2.Submit.

Expected Result: System returns travel amount.

Actual Result: (to be filled)

TC3.2 – Query groceries (trend)

Preconditions: Same CSV.

Steps:

1.Enter: “Groceries expense last month?”

2.Submit.

Expected Result: System returns groceries total.

Actual Result: (to be filled)

TC3.3 – Query shopping (trend)

Preconditions: Same CSV.

Steps:

1.Enter: “Shopping spending last month?”

2.Submit.

Expected Result: System returns shopping total.

Actual Result: (to be filled)

TC3.4 – (Negative) Empty CSV

Preconditions: transactions.csv is empty.

Steps:

1.Enter: “How much did I spend on travel last month?”

2.Submit.

Expected Result: System returns error “transactions.csv file not found or empty”.

Actual Result: (to be filled)

User Story 4 – Edge Cases / Developer Testing

TC4.1 – Empty query

Preconditions: Web UI loaded.

Steps:

1.Leave query field blank.

2.Submit.

Expected Result: System shows “Please enter a question.”

Actual Result: (to be filled)

TC4.2 – Invalid query

Preconditions: Same CSV.

Steps:

1.Enter: “asdfghjkl???”

2.Submit.

Expected Result: System falls back → total spending.

Actual Result: (to be filled)

TC4.3 – Query with symbols

Preconditions: CSV has travel.

Steps:

1.Enter: “!!! Travel ???”

2.Submit.

Expected Result: System still detects travel and returns amount.

Actual Result: (to be filled)

TC4.4 – (Negative) Special characters only

Preconditions: Web UI loaded.

Steps:

1.Enter: “@@@###”.

2.Submit.

Expected Result: System falls back → total spending.

Actual Result: (to be filled)

User Story 5 – Total Spending

TC5.1 – Query total

Preconditions: transactions.csv has multiple categories.

Steps:

1.Enter: “What is my total spending last month?”

2.Submit.

Expected Result: System returns total spending.

Actual Result: (to be filled)

TC5.2 – Alternative wording

Preconditions: Same CSV.

Steps:

1.Enter: “Show all my expenses last month”

2.Submit.

Expected Result: System returns total spending.

Actual Result: (to be filled)

TC5.3 – Lowercase query

Preconditions: Same CSV.

Steps:

1.Enter: “total spending”

2.Submit.

Expected Result: System returns total spending.

Actual Result: (to be filled)

TC5.4 – (Negative) Malformed query

Preconditions: Same CSV.

Steps:

1.Enter: “Tell me blah blah”

2.Submit.

Expected Result: System falls back → total spending.

Actual Result: (to be filled)


TESTCASES 
Test ID	User Story	Description	Preconditions	Test Steps	Expected Result	Actual Result
TC1.1	Story 1 – Category Query groceries spending	transactions.csv has groceries	Enter “How much did I spend on groceries last month?” in Web UI	Returns grocery total	(fill after testing)
TC1.2	Story 1 – Category	Query shopping spending	CSV has shopping	Enter “How much on shopping last month?”	Returns shopping total	(fill)
TC1.3	Story 1 – Category	Query medicine spending	CSV has medicine	Enter “What about medicine expenses?”	Returns medicine total	(fill)
TC1.4	Story 1 – Category (Negative)	Query unknown category	CSV does NOT have movies	Enter “How much did I spend on movies last month?”	Returns total spending (fallback)	(fill)
TC2.1	Story 2 – Rent	Query rent	CSV has rent	Enter “What was my rent last month?”	Returns rent amount	(fill)
TC2.2	Story 2 – Rent	Rent alternative wording	CSV has rent	Enter “Tell me my house rent last month”	Returns rent amount	(fill)
TC2.3	Story 2 – Rent	Rent case-insensitive	CSV has rent	Enter “rent”	Returns rent amount	(fill)
TC2.4	Story 2 – Rent (Negative)	Rent missing in CSV	CSV has no rent	Enter “What was my rent last month?”	Returns total spending (fallback)	(fill)
TC3.1	Story 3 – Analyst Trends	Query travel	CSV has travel	Enter “How much did I spend on travel last month?”	Returns travel total	(fill)
TC3.2	Story 3 – Analyst Trends	Query groceries	CSV has groceries	Enter “Groceries expense last month?”	Returns groceries total	(fill)
TC3.3	Story 3 – Analyst Trends	Query shopping	CSV has shopping	Enter “Shopping spending last month?”	Returns shopping total	(fill)
TC3.4	Story 3 – Analyst Trends (Negative)	Empty CSV	transactions.csv is empty	Enter “How much did I spend on travel last month?”	Returns error (file not found / empty)	(fill)
TC4.1	Story 4 – Edge Case	Empty query	Web UI loaded	Leave field blank → Submit	Returns “Please enter a question.”	(fill)
TC4.2	Story 4 – Edge Case	Invalid query	CSV present	Enter “asdfghjkl???”	Returns total spending (fallback)	(fill)
TC4.3	Story 4 – Edge Case	Query with symbols	CSV has travel	Enter “!!! Travel ???”	Returns travel total	(fill)
TC4.4	Story 4 – Edge Case (Negative)	Symbols only	Web UI loaded	Enter “@@@###”	Returns total spending (fallback)	(fill)
TC5.1	Story 5 – Total	Query total spending	CSV has multiple categories	Enter “What is my total spending last month?”	Returns total spending	(fill)
TC5.2	Story 5 – Total	Alternative wording	Same CSV	Enter “Show all my expenses last month”	Returns total spending	(fill)
TC5.3	Story 5 – Total	Lowercase query	Same CSV	Enter “total spending”	Returns total spending	(fill)
TC5.4	Story 5 – Total (Negative)	Malformed query	Same CSV	Enter “Tell me blah blah”	Returns total spending (fallback)	(fill)



 Architecture
flowchart TD
    A[User Query in Web UI] --> B[Flask App]
    B --> C[Load transactions.csv using pandas]
    C --> D[Dynamic Category Detection]
    D --> E[Azure OpenAI Deployment]
    E --> F[AI Response Generated]
    F --> G[Answer Displayed in Browser]

📖 Learnings and Challenges

Learned how to integrate Flask with Azure OpenAI.

Understood environment variable handling to protect secrets.

Faced issues with deployment (Application Error, 405 Method Not Allowed) and fixed them.

Implemented dynamic category detection → now app works with any category in transactions.csv.

Learned Agile practices → writing User Stories (3C) and Test Cases (with actual results).

 Live Demo

Web Interface:

https://<your-app-name>.azurewebsites.net/
