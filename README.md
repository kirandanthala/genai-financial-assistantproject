GENAI POWERED FINANCIAL ASSISTANT 

    **OBJECTIVE**  
A GenAI-powered assistant that provides personalized financial insights based on user queries and transaction data.  
. Accepts natural language queries (e.g., *“How much did I spend on groceries last month?”*)  
. Analyzes structured transaction data ('transactions.csv)  
. Uses  to generate financial summaries  
. Provides actionable insights (spending trends, saving tips)  
. Accessible via a simple *web interface* ('/ask-ui')  


   *PROJECT STRUCTURE**
genai-financial-assistantproject/
│-- app.py # Flask application
│-- requirements.txt # Dependencies
│-- transactions.csv # Sample transaction dataset
│-- templates/
└── index.html # Web interface
│-- README.md # Documentation



--- SETUP INSTRUCTIONS

1.Clone the Repository  
git clone https://github.com/kirandanthala/genai-financial-assistantproject
cd genai-financial-assistantproject

2.Create Virtual Environment & Install Requirements
python -m venv venv
venv\Scripts\activate.bat  # Windows
pip install -r requirements.txt

3.Run Locally
python app.py
Open in browser: http://127.0.0.1:5000

*AZURE DEPLOYEMENT*

Deployed using Azure App Service (Linux, Python runtime)
Environment Variables (Configuration → Application Settings):
AZURE_OPENAI_KEY → AZURE_API_KEY
AZURE_ENDPOINT →  https://fiancemngmnt.openai.azure.com/
AZURE_DEPLOYMENT → Financemodel-genai

Public URL:
https://genaiassistant-e7h3hkf7fagdawa2.canadacentral-01.azurewebsites.net/ask-ui

==>USAGE
Web Interface: / or /ask-ui
Accessible in any browser:

https://genaiassistant-e7h3hkf7fagdawa2.canadacentral-01.azurewebsites.net/ask-ui

Shows a text box to enter queries
Displays AI response directly below

**USER STORIES* 
==>>User Story 1 – Category Spending (e.g., groceries, shopping, medicine)

TC1.1 – Query groceries spending
Preconditions: transactions.csv has category = groceries.
Steps:
Open Web UI.
1.Enter: “How much did I spend on groceries last month?”
2.Submit.
Expected Result: System returns grocery total from CSV.
Actual Result: (Filled in table)

TC1.2 – Query shopping spending
Preconditions: transactions.csv has category = shopping.
Steps:
Open Web UI.
1.Enter: “How much on shopping last month?”
2.Submit.
Expected Result: System returns shopping total.
Actual Result: (Filled in Table)

TC1.3 – Query haircut spending
Preconditions: transactions.csv has category = haircut.
Steps:
Open Web UI.
1.Enter: “What about Haircut expenses?”
2.Submit.
Expected Result: System returns medicine total.
Actual Result: (Filled in Table)

TC1.4 – (Negative) Unknown category
Preconditions: transactions.csv does NOT have category = movies.
Steps:
Open Web UI.
1.Enter: “How much did I spend on movies last month?”
2.Submit.
Expected Result: System returns total spending (fallback).
Actual Result: (Filled in Table)

===>>User Story 2 – Rent Spending

TC2.1 – Query rent
Preconditions: transactions.csv has category = rent.
Steps:
Open Web UI.
1.Enter: “What was my rent last month?”
2.Submit.
Expected Result: System returns rent amount.
Actual Result: (Filled in Table)

TC2.2 – Rent alternative wording
Preconditions: Same CSV.
Steps:
1.Enter: “Tell me my house rent last month”.
2.Submit.
Expected Result: System returns rent amount.
Actual Result: (Filled in Table)

TC2.3 – Rent case-insensitive
Preconditions: Same CSV.
Steps:
1.Enter: “rent” (lowercase).
2.Submit.
Expected Result: System returns rent amount.
Actual Result: (Filled in Table)

TC2.4 – (Negative) Rent missing
Preconditions: transactions.csv does NOT have category = rent.
Steps:
1.Enter: “What was my rent last month?”
2.Submit.
Expected Result: System falls back → total spending.
Actual Result: (Filled in Table)

==>>User Story 3 – Analyst Spending Trends

TC3.1 – Query travel
Preconditions: transactions.csv has category = travel.
Steps:
1.Enter: “How much did I spend on travel last month?”
2.Submit.
Expected Result: System returns travel amount.
Actual Result: (Filled in Table)

TC3.2 – Query groceries (trend)
Preconditions: Same CSV.
Steps:
1.Enter: “Groceries expense last month?”
2.Submit.
Expected Result: System returns groceries total.
Actual Result: (Filled in Table)

TC3.3 – Query shopping (trend)
Preconditions: Same CSV.
Steps:
1.Enter: “Shopping spending last month?”
2.Submit.
Expected Result: System returns shopping total.

Actual Result: (Filled in Table)

TC3.4 – (Negative) Empty CSV
Preconditions: transactions.csv is empty.
Steps:
1.Enter: “How much did I spend on travel last month?”
2.Submit.
Expected Result: System returns error “transactions.csv file not found or empty”.
Actual Result: (Filled in Table)

==>>User Story 4 – Edge Cases / Developer Testing

TC4.1 – Empty query
Preconditions: Web UI loaded.
Steps:
1.Leave query field blank.
2.Submit.
Expected Result: System shows “Please enter a question.”
Actual Result: (Filled in Table)

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

==>>User Story 5 – Total Spending

TC5.1 – Query total
Preconditions: transactions.csv has multiple categories.
Steps:
1.Enter: “What is my total spending last month?”
2.Submit.
Expected Result: System returns total spending.
Actual Result: (Filled in Table)

TC5.2 – Alternative wording
Preconditions: Same CSV.
Steps:
1.Enter: “Show all my expenses last month”
2.Submit.
Expected Result: System returns total spending.
Actual Result: (Filled in Table)

TC5.3 – Lowercase query
Preconditions: Same CSV.
Steps:
1.Enter: “total spending”
2.Submit.
Expected Result: System returns total spending.
Actual Result: (Filled in Table)

TC5.4 – (Negative) Malformed query
Preconditions: Same CSV.
Steps:
1.Enter: “Tell me blah blah”
2.Submit.
Expected Result: System falls back → total spending.
Actual Result: (Filled in Table)


TESTCASES 
Test ID	User Story	Description	Preconditions	Test Steps	Expected Result	Actual Result
TC1.1	Story 1 – Category Query groceries spending	transactions.csv has groceries	Enter “How much did I spend on groceries last month?” in Web UI	Returns grocery total	(You spent 1700 INR on groceries last month.)
TC1.2	Story 1 – Category	Query shopping spending	CSV has shopping	Enter “How much on shopping last month?”	Returns shopping total	(You spent 2000 INR on shopping last month)
TC1.3	Story 1 – Category	Query haircut spending	CSV has haircut	Enter “What about haircut expenses?”	Returns medicine total	(The haircut expenses of 300 INR can be recorded as a personal expense under the category of personal care or grooming in your financial records for last month.)
TC1.4	Story 1 – Category (Negative)	Query unknown category	CSV does NOT have movies	Enter “How much did I spend on movies last month?”	Returns total spending (fallback)	(You spent 11600 INR last month, but without further details, I cannot provide the specific amount you spent on movies. If you have a breakdown of your expenses or can provide more information, I can help you determine the exact amount spent on movies.)
TC2.1	Story 2 – Rent	Query rent	CSV has rent	Enter “What was my rent last month?”	Returns rent amount	(Your rent last month was 5000 INR.)
TC2.2	Story 2 – Rent	Rent alternative wording	CSV has rent	Enter “Tell me my house rent last month”	Returns rent amount	(Your house rent last month was 5000 INR.)
TC2.3	Story 2 – Rent	Rent case-insensitive	CSV has rent	Enter “RENT”	Returns rent amount	(Thank you for providing the context. I have recorded the rent expense of 5000 INR for last month. If you need any further assistance or have any other transactions to report, please let me know.)
TC2.4	Story 2 – Rent (Negative)	Rent missing in CSV	CSV has no rent	Enter “What was my rent last month?”	Returns total spending (fallback)	(Your medicine bill amount was not explicitly provided in the context given. However, if your total spending last month was 11600 INR and you want to know the medicine bill amount, you would need to provide more specific information related to your expenses for me to accurately determine the exact amount spent on medicines.)
TC3.1	Story 3 – Analyst Trends	Query travel	CSV has travel	Enter “How much did I spend on travel last month?”	Returns travel total	(You spent 600 INR on travel last month.)
TC3.2	Story 3 – Analyst Trends	Query groceries	CSV has groceries	Enter “Groceries expense last month?”	Returns groceries total	(You spent 1700 INR on groceries last month.)
TC3.3	Story 3 – Analyst Trends	Query shopping	CSV has shopping	Enter “Shopping spending last month?”	Returns shopping total	(You spent 2000 INR on shopping last month.)
TC3.4	Story 3 – Analyst Trends (Negative)	Empty CSV	transactions.csv is empty	Enter “How much did I spend on travel last month?”	Returns error (file not found / empty)	(fill)
TC4.1	Story 4 – Edge Case	Empty query	Web UI loaded	Leave field blank → Submit	Returns “Please enter a question.”	(We can see when not entering anything means in UI)
TC4.2	Story 4 – Edge Case	Invalid query	CSV present	Enter “asdfghjkl???”	Returns total spending (fallback)	(It seems like you might be inquiring about your spending from last month. Your total spending was 11600 INR. Let me know if you need any further assistance or clarification regarding your finances.)
TC4.3	Story 4 – Edge Case	Query with symbols	CSV has travel	Enter “!!! Travel ???”	Returns travel total	(Thank you for providing that information. It appears that you spent 600 INR on travel last month. If you need any assistance with managing your travel expenses or budgeting for future trips, feel free to let me know.)
TC4.4	Story 4 – Edge Case (Negative)	Symbols only	Web UI loaded	Enter “@@@###”	Returns total spending (fallback)	(fill)
TC5.1	Story 5 – Total	Query total spending	CSV has multiple categories	Enter “What is my total spending last month?”	Returns total spending	(Your total spending last month was 11600 INR.)
TC5.2	Story 5 – Total	Alternative wording	Same CSV	Enter “Show all my expenses last month”	Returns total spending	(Certainly! Here are your expenses breakdown for last month: 1. Rent: 6000 INR 2. Groceries: 2000 INR 3. Utilities: 1200 INR 4. Dining out: 1400 INR 5. Transportation: 1000 INR Total Expenses: 11600 INR Please let me know if you need further details or assistance.)
TC5.3	Story 5 – Total	Lowercase query	Same CSV	Enter “total spending”	Returns total spending	(Your total spending last month was 11600 INR.)
TC5.4	Story 5 – Total (Negative)	Malformed query	Same CSV	Enter “Tell me blah blah”	Returns total spending (fallback)	(Based on the context provided, your total spending last month was 11600 INR. If you need further details or specific information, feel free to ask.)



              **Architecture*
flowchart 
    A[User Query in Web UI] --> B[Flask App]
    B --> C[Load transactions.csv using pandas]
    C --> D[Dynamic Category Detection]
    D --> E[Azure OpenAI Deployment]
    E --> F[AI Response Generated]
    F --> G[Answer Displayed in Browser]

===> LEARNINGS AND CHALLENGES

-Learned how to integrate Flask with Azure OpenAI.
-Understood environment variable handling to protect secrets.
-Faced issues with deployment (Application Error, 405 Method Not Allowed) and fixed them.
-Implemented dynamic category detection → now app works with any category in transactions.csv.
-Learned Agile practices → writing User Stories (3C) and Test Cases (with actual results).


Web Interface:

https://genaiassistant-e7h3hkf7fagdawa2.canadacentral-01.azurewebsites.net/ask-ui