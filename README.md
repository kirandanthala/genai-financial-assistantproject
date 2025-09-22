--GENAI-POWERED FINANCIAL ASSISTANT--

OVERVIEW:
   This project is a Flask-based web application powered by Azure OpenAI.
   It allows users to ask natural language questions about their financial transactions, and get AI-generated insights based on contextual transaction data.


FEATURES:
       =>Query expenses by category (e.g., groceries, rent, travel, shopping).
       =>Query expenses by category + month/year (e.g., travel in Sept 2025).
       =>Handle missing dates and missing amounts gracefully.
       =>Reject invalid or irrelevant queries with safe responses.
       =>Accessible via a basic web interface hosted on Azure App Service.

ARCHITECTURE:

   flowchart TD
    User[User Query via Browser] -->|POST /ask-ui| FlaskApp[Flask Application]
    FlaskApp -->|Reads| CSV[transactions.csv]
    FlaskApp -->|Context + Query| AzureOpenAI[Azure OpenAI Service]
    AzureOpenAI --> Response[AI Response Returned]
    Response --> User

PROJECT STRUCTURE:
      genai-financial-assistantproject/
│
|__ app.py                # Main Flask application (routes, logic, OpenAI integration)
├── requirements.txt      # Python dependencies (Flask, Pandas, OpenAI, Gunicorn, etc.)
├── transactions.csv      # Sample transaction dataset (used for queries)
├── templates/
│   └── index.html        # Web UI for interacting with the financial assistant
├── startup.txt           # Startup command for Azure App Service
├── .deployment           # Deployment configuration for Azure     
└── README.md             # Project documentation
 

SETUP INSTRUCTIONS:

1.Clone the Repo
     git clone https://github.com/kirandanthala/genai-financial-assistantproject
     cd genai-financial-assistantproject
    
2.Create Virtual Environment
      python -m venv venv
      venv\Scripts\activate.bat --For windows

3.Install Dependencies
       pip install -r requirements.txt

4.Add the Data into Csv file.
      -Create the file transactions.csv abd add below data

5.Set Azure OpenAI keys
       In Azure Portal → App Service → Configuration → Application settings,
         AZURE_OPENAI_KEY = <Key1>
6.Run Locally .
      =>python app.py
      Visit this link after running in local. 
         http://127.0.0.1:8000
7.Deploy to Azure
    Push to GitHub
    Connect repo in Azure App Service
    Add startup command:
              =>gunicorn app:app --bind=0.0.0.0:$PORT
    Restart service

USER STORIES (3C Format)
    Story 1 – Category-Based Query
       Card: As a user, I want to query expenses by category so that I can track spending patterns.
       Conversation: Discussed common categories like groceries, rent, travel.
       Confirmation: Query returns total spend for the mentioned category.
    Story 2 – Category + Date Query
       Card: As a user, I want to query expenses by category and month/year so that I can track spending over time.
       Conversation: Mentioned travel in Sept 2025, groceries in July, etc.
       Confirmation: Query returns filtered sum for that period.
    Story 3 – Handle Missing Dates
       Card: As a user, I want the system to skip or notify missing dates so that my results remain accurate.
       Conversation: If all rows missing → respond with “No records found”.
       Confirmation: Properly ignores lanks, does not crash.
    Story 4 – Handle Missing Amounts
       Card: As a user, I want missing or invalid amounts treated as 0 so that my totals are correct.
       Conversation: Blank or “abc” → treated as 0.
       Confirmation: Still gives a valid total.
    Story 5 – Handle Invalid Queries
       Card: As a user, I want irrelevant queries to be handled gracefully so that system does not confuse or break.
       Conversation: If query unrelated (e.g., president of India) → respond with “No records found”.
       Confirmation: Rejects safely.

TESTCASES IN FORMAT:
Story 1 – Category-Based Query
TC1.1 – Query groceries spending
Preconditions: transactions.csv has category = groceries.
Steps:
Open Web UI.
Enter: “How much did I spend on groceries last month?”
Submit.
Expected Result: System returns grocery total from CSV.
Actual Result:You spent 5700.0 INR on groceries.

TC1.2 – Query rent spending
Preconditions: CSV has category = rent.
Steps:
Open Web UI.
Enter: “How much was my rent?”
Ask
Expected Result: System returns rent total.
Actual Result:Your rent was 8000.0 INR.

TC1.3 – Query travel spending
Preconditions: CSV has category = travel.
Steps:
Enter: “Show my travel expenses.”
Ask
Expected Result: System returns travel total.
Actual Result:You spent 9000.0 INR on travel.

TC1.4 – Negative: Unknown category
Preconditions: CSV does not have category = medicine.
Steps:
Enter: “What was my medicine bill?”
Submit.
Expected Result: System responds: “No records found for medicine.”
Actual Result: —

Story 2 – Category + Date Query
TC2.1 – Query travel in September 2025
Preconditions: CSV has travel rows in Aug 2025.
Steps:
  Enter: “How much did I spend on travel in August 2025?”
  Ask.
Expected Result: Returns filtered sum for travel in Sept 2025.
Actual Result:It appears that you spent 5000.0 INR on travel. If you are inquiring about a future travel plan in August 2025, please provide more details or clarify your question.

TC2.2 – Query rent in August 2025
Preconditions: CSV has rent rows in Aug 2025.
Steps:
  Enter: “How much rent in August 2025?”
  Ask.
Expected Result: Returns rent in Aug 2025.
Actual Result: The rent paid in August 2025 was 8000.0 INR.

TC2.3 – Query groceries in July 2025
Preconditions: CSV has groceries in July 2025.
Steps:
  Enter: “Groceries in July 2025?”
  Ask.
Expected Result: Returns groceries spend in July.
Actual Result:The total amount spent on groceries in September 2025 was 2200.0 INR.

TC2.4 – Negative: No records for month
Preconditions: CSV has no travel in June 2025.
Steps:
  Enter: “How much travel in June 2025?”
  Ask.
Expected Result: Responds: “No spending records found for June 2025.”
Actual Result: There are no spending records found for the category 'travel' in June.

Story 3 – Handle Missing Dates
TC3.1 – Query travel with valid dates
Preconditions: CSV travel rows have proper dates.
Steps:
  Enter: “How much on travel in Sept 2025?”
  Ask.
Expected Result: Correct filtered result.
Actual Result:You spent 5000.0 INR on travel in August 2025.

TC3.2 – Query rent with mixed dates
Preconditions: Some rent rows have valid Aug 2025, some missing dates.
Steps:
  Enter: “How much rent in Aug 2025?”
  Ask.
Expected Result: Only valid dated rows included; missing skipped.
Actual Result: You spent 5000.0 INR on travel in August 2025

TC3.3 – Query groceries with partial dates
Preconditions: Groceries in Aug & Sept, but some missing dates.
Steps:
  Enter: “Groceries in Sept 2025?”
  Ask.
Expected Result: Sept groceries only; blanks ignored.
  Actual Result: You spent 2200.0 INR on groceries in September 2025.

TC3.4 – Negative: All missing dates
Preconditions: All groceries rows have blank dates.
Steps:
  Enter: “Groceries in Sept 2025?”
  Submit.
Expected Result: Responds: “No records found.”
Actual Result: There are no spending records found for movies in June 2025.

Story 4 – Handle Missing Amounts
TC4.1 – Shopping with valid amounts
Preconditions: Shopping rows have valid numbers.
Steps
  Enter: “Shopping spend?”
  Ask.
Expected Result: Returns total shopping spend.
Actual Result: You spent 3000.0 INR on shopping.

TC4.2 – Shopping with blanks
Preconditions: One shopping row = 2000, one blank.
Steps:
  Enter: “Shopping spend?”
  Ask.
Expected Result: Blank treated as 0, result = 2000.
Actual Result: You spent 3000.0 INR on shopping.

TC4.3 – Travel with invalid amount
Preconditions: Travel row = 1500, another = "abc".
Steps:
  Enter: “Travel spend?”
  Submit.
Expected Result: Invalid coerced to 0, total = 1500.
Actual Result: You spent 3000.0 INR on shopping.

TC4.4 – Negative: All missing amounts
Preconditions: All shopping rows have blank amounts.
Steps:
  Enter: “Shopping spend?”
  Submit.
Expected Result: Responds with “0 INR spent on shopping.”
Actual Result: You Spent 0 INR on shopping.

Story 5 – Handle Invalid Queries
TC5.1 – Empty query
Preconditions: Form input is empty.
Steps:
  Leave query blank.
  Submit.
Expected Result: System responds: “Please enter a question.”
Actual Result: ---

TC5.2 – Irrelevant query
Preconditions: Query outside finance.
Steps:
  Enter: “Who is the PM of India?”
  Ask.
Expected Result: “No records found.”
Actual Result: 	I'm sorry, I am a financial assistant and do not have information on the current Prime Minister of India.

TC5.3 – Gibberish query
Preconditions: Input meaningless text.
Steps:
  Enter: “asdasd qwe123”
  Ask.
Expected Result: “No records found.”
Actual Result: I'm sorry, but I couldn't find any records for the category mentioned in your query. If you have any other questions or need assistance with a different category, please let me know.

TC5.4 – Negative: Unsupported intent
Preconditions: Query asks prediction.
Steps:
  Enter: “Predict my shopping next month.”
  Ask
Expected Result: “AI Response/cannot predict”
Actual Result: I'm sorry, I cannot predict your shopping expenses for next month based on the information provided.


TESTCASES:
 Test ID	User Story	Description	Preconditions	Test Steps	Expected Result	Actual Result
TC1.1	Story 1	Groceries total spend	CSV has groceries	Ask: “How much did I spend on groceries?”	Returns grocery total	"You spent 5700.0 INR on groceries."
TC1.2	Story 1	Rent spend	CSV has rent	Ask: “Rent expense?”	Returns rent total	Your rent was 8000.0 INR.
TC1.3	Story 1	Travel spend	CSV has travel	Ask: “Travel spend?”	Returns travel total	You spent 9000.0 INR on travel.
TC1.4 	Story 1	Negative – Unknown category	No “medicine” category	Ask: “Medicine spend?”	Responds: No records found	I'm sorry, but I couldn't find any records for medicine spend in the available data. If you have any other financial transactions or categories you would like to inquire about, please let me know.
TC2.1	Story 2	Travel in Sept 2025	CSV has travel in Sept	Ask: “Travel in August 2025?”	Returns Aug travel	It appears that you spent 5000.0 INR on travel. If you are inquiring about a future travel plan in August 2025, please provide more details or clarify your question.
TC2.2	Story 2	Rent in Aug 2025	CSV has rent in Aug	Ask: “Rent in Aug 2025?”	Returns Aug rent  The rent paid in August 2025 was 8000.0 INR.
TC2.3	Story 2	Groceries in July 2025	CSV has groceries in July	Ask: “Groceries in September 2025?”	Returns July groceries	The total amount spent on groceries in September 2025 was 2200.0 INR.
TC2.4 	Story 2	Negative – No records	No travel in June 2025	Ask: “Travel in June 2025?”	Responds: No records found	There are no spending records found for the category 'travel' in June.
TC3.1	Story 3	Travel with dates	CSV has travel dates	Ask: “Travel in Sept 2025?”	Returns August travel  	
TC3.1	Story 3	Travel with dates	CSV has travel dates	Ask: “Travel in Sept 2025?”	Returns Sep travel You spent 5000.0 INR on travel in August 2025.	
TC3.2	Story 3	Rent with mixed dates	Rent rows with Aug + blanks	Ask: “Rent in Aug 2025?”	Returns Aug rent only	You spent 5000.0 INR on travel in August 2025.
TC3.3	Story 3	Groceries multiple months	Groceries in Aug + Sept	Ask: “Groceries in Sept 2025?”	Returns Sept groceries	You spent 2200.0 INR on groceries in September 2025.
TC3.4 	Story 3	Negative – all missing dates	Rows blank dates	Ask: “Movies in June 2025?”	Responds: No records found	There are no spending records found for movies in June 2025.
TC4.1	Story 4	Shopping valid amounts	Shopping rows with numbers	Ask: “Shopping spend?”	Returns shopping total	You spent 3000.0 INR on shopping.
TC4.2	Story 4	Shopping mixed amounts	One row 2000, one blank	Ask: “Shopping spend?”	Returns 2000	You spent 3000.0 INR on shopping.
TC4.3	Story 4	Travel with invalid values	Travel rows 1500 + "abc"	Ask: “Travel spend?”	Returns 1500	You Spent 3000.0
TC4.4 	Story 4	Negative – all missing amounts	Shopping rows blank only	Ask: “Shopping spend?”	Responds: 0 INR spent	
TC5.1	Story 5	Empty query	Form empty	Submit blank	Please enter a question	"Please fill out this field"
TC5.2	Story 5	Irrelevant query	Query outside dataset	Ask: “Who is PM of India?”	I'm sorry, I am a financial assistant and do not have information on the current Prime Minister of India.
TC5.3	Story 5	Gibberish	Random chars	Ask: “asdasd qwe123”	No records found I'm sorry, but I couldn't find any records for the category mentioned in your query. If you have any other questions or need assistance with a different category, please let me know.
TC5.4 	Story 5	Negative – unsupported intent	Predictive query	Ask: “Predict shopping next month”	No records found/cannot predict	 I'm sorry, I cannot predict your shopping expenses for next month based on the information provided.

LEARNINGS AND CHALLENGES:
    1.Flask + Azure Integration
       Learned how to build a lightweight Flask API/UI and deploy it on Azure App Service with Gunicorn.
       Understood how to use environment variables (os.getenv) for securely managing API keys.
    2.Data Handling with Pandas
        Gained experience in cleaning data (to_numeric, to_datetime) to handle missing/invalid values.
        Implemented category and date-based filtering dynamically.
    3.Prompt Engineering for Azure OpenAI
        Designed system and user messages to restrict the model to use only provided transaction context.
        Ensured deterministic responses by setting temperature=0.
    4.Error Handling & Debugging
        Dealt with common issues like transactions.csv not found, missing columns, and invalid startup commands.
        Used Kudu Console and Azure log streaming for debugging deployment issues.
    5.Agile Practices
        Wrote user stories in 3C format (Card, Conversation, Confirmation).
        Designed positive & negative test cases for each story, ensuring robustness.

CHALLENGES:
     1.Deployment Issues
       Faced repeated “Container failed to start on port 8000” errors.
       Fixed using proper Gunicorn startup command and startup.txt.
     2.Missing Transactions Data
       CSV initially not being deployed to Azure.
       Solved by force-including transactions.csv and verifying in Kudu /site/wwwroot/.
     3.Dynamic Categories
      Initially hardcoded categories (groceries, rent, travel).
       Moved to a dynamic matching system that reads categories from CSV directly.
     4.Negative Test Handling
       Without fallback, system had to explicitly say “No records found” when category/date not available.
       Required refining logic to check filtered.empty.
     5.Environment Variables & Secrets
        GitHub push was blocked due to exposed API key.
        Resolved by removing secrets from code and using Azure’s Application Settings.

FINAL URL:https://genaiassistant-e7h3hkf7fagdawa2.canadacentral-01.azurewebsites.net/ask-ui


    
 

