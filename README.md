# GenAI-Powered Financial Insights Assistant

## 📌 Project Overview
This project is a **GenAI-powered assistant** that provides personalized financial insights using natural language queries and structured transaction data.  
It is built with **Flask**, **Azure OpenAI**, and **pandas**.  

The assistant can:
- Accept natural language queries (e.g., "How much did I spend on groceries last month?")  
- Analyze structured transaction data (CSV file)  
- Provide actionable insights such as spending summaries, top expense categories, and trends  
- Be accessed through a simple REST API  

---

##  How to Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd genai-financial-assistantproject

2. Create virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # Linux/Mac
3. Install requirements
bash
Copy code
pip install -r requirements.txt
4. Run the app
bash
Copy code
python app.py
5. Test API (Example in PowerShell)
powershell
Copy code
Invoke-RestMethod -Uri "http://127.0.0.1:5000/ask" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"query":"How much did I spend on groceries last month?"}'
🧩 User Stories (3C Format)
Story 1 – Grocery Spend
Card: As a customer, I want to know how much I spent on groceries last month.

Conversation: Customer queries “How much did I spend on groceries?” → System calculates from transactions.

Confirmation: Assistant returns total groceries spend.

Story 2 – Category Not Found
Card: As a customer, I want to ask about a category that does not exist.

Conversation: Query = "Electronics spend?" → No data in CSV.

Confirmation: Assistant says "No expenses found for Electronics."

Story 3 – Top 3 Spending Categories
Card: As an analyst, I want to know my top 3 spending categories.

Conversation: Query = "What are my top 3 categories?"

Confirmation: Assistant lists top 3 categories with amounts.

Story 4 – Empty Query
Card: As a tester, I want to see how the system behaves with empty query.

Conversation: Query = "" (empty).

Confirmation: Assistant returns error JSON.

Story 5 – Day of Highest Spend
Card: As a customer, I want to know which day I spent the most.

Conversation: Query = "Which day did I spend the most?"

Confirmation: Assistant returns day + amount.


 Test Cases
TESTID	  Description	Preconditions	Test Steps	Expected Result	Negative/Positive
TC1	Query groceries spend	transactions.csv available	Send query "How much on groceries?"	Returns total groceries spend	Positive
TC2	Query travel spend	transactions.csv available	Send query "Travel expenses?"	Returns total travel spend	Positive
TC3	Query rent spend	transactions.csv available	Send query "Rent last month?"	Returns rent amount	Positive
TC4	Query total spend	transactions.csv available	Send query "Total spend?"	Returns sum of all transactions	Positive
TC5	Top 3 categories	transactions.csv available	Send query "Top 3 categories"	Returns 3 categories ranked	Positive
TC6	Day of highest spend	transactions.csv available	Send query "Which day highest?"	Returns date + amount	Positive
TC7	Non-existing category	transactions.csv available	Send query "Electronics spend?"	Returns "No expenses found"	Negative
TC8	Empty query	transactions.csv available	Send empty query ""	Returns error "No query provided"	Negative
TC9	Gibberish input	transactions.csv available	Send "asdfgh"	Returns fallback total spend or error	Negative
TC10	CSV missing	delete/rename transactions.csv	Send any query	Returns error "transactions.csv file not found"	Negative
TC11	Multiple queries in one	transactions.csv available	Send "Groceries and Travel?"	Returns combined or clarifies	Positive
TC12	Very large query text	transactions.csv available	Send 200 words query	Still responds gracefully	Negative
TC13	Query case sensitivity	transactions.csv available	Send "GROCERIES"	Returns groceries spend	Positive
TC14	Query with typos	transactions.csv available	Send "groceris"	Handles via AI correction	Positive
TC15	Query without month mention	transactions.csv available	Send "Groceries spend?"	Defaults to last month	Positive
TC16	Future date query	transactions.csv available	Send "How much will I spend next month?"	Returns clarification	Negative
TC17	Query in Hindi	transactions.csv available	Send "Maine grocery par kitna kharch kiya?"	AI translates + responds	Positive
TC18	Query in Telugu	transactions.csv available	Send "Nenu groceries meeda entha kharchu chesanu?"	AI responds with context	Positive
TC19	Query for savings suggestion	transactions.csv available	Send "How can I save more?"	AI gives advice (not from CSV)	Positive
TC20	Stress test (rapid requests)	transactions.csv available	Send 10 queries in 5 sec	System handles or rate limits	Negative

 Architecture
pgsql
Copy code
User Query → Flask API (/ask) → pandas reads CSV → Context prepared → Azure OpenAI → AI Response → JSON output

 Learnings and Challenges
       Setting up Flask and Azure OpenAI integration

Handling CSV data with pandas

Writing Agile User Stories in 3C format

Designing positive and negative test cases

Debugging issues with deployment name and endpoint

Understanding cloud deployment and environment setup