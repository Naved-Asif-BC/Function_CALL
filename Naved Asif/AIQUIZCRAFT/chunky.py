import pandas as pd

json_data={
    "questions": [
      {
        "question": "What is the main focus of Accelerate People?",
        "options": [
          "Providing digital IT EPAs",
          "Delivering successful digital transformations",
          "Offering work-readiness programs",
          "Providing investment management services"
        ],
        "correct_option": "Providing digital IT EPAs"
      },
      {
        "question": "Who has the final say on whether an apprentice is ready for their EPA?",
        "options": [
          "The training provider",
          "The employer",
          "The apprentice",
          "The EPA organisation"
        ],
        "correct_option": "The employer"
      },
      {
        "question": "Which level of apprenticeship does Agilisys offer in Artificial Intelligence (AI) Data Specialist?",
        "options": [
          "Level 7",
          "Level 4",
          "Level 3",
          "Level 5"
        ],
        "correct_option": "Level 7"
      },
      {
        "question": "What is the focus of Agilisys' digital transformation services?",
        "options": [
          "Enhancing public services",
          "Providing high-quality customer services",
          "Offering cloud solutions",
          "Delivering successful outcomes"
        ],
        "correct_option": "Enhancing public services"
      },
      {
        "question": "What does Avado Learning specialize in?",
        "options": [
          "Digital transformations",
          "Investment management",
          "Work-readiness programs",
          "English language tests"
        ],
        "correct_option": "Work-readiness programs"
      },
      {
        "question": "Which academy does Avado offer for data-driven culture?",
        "options": [
          "Data Academy",
          "FastFutures Programme",
          "CIPD HR Courses",
          "Marketing Academy"
        ],
        "correct_option": "Data Academy"
      },
      {
        "question": "What type of courses does Avado offer for HR and L&D professionals?",
        "options": [
          "Data science courses",
          "English communication courses",
          "HR courses",
          "Marketing courses"
        ],
        "correct_option": "HR courses"
      },
      {
        "question": "What services does BCI Capital Limited provide?",
        "options": [
          "Digital transformations",
          "Work-readiness programs",
          "Investment management"
        ],
        "correct_option": "Investment management"
      },
      {
        "question": "What is the main focus of Accelerate People?",
        "options": [
          "Providing digital IT EPAs",
          "Delivering successful digital transformations",
          "Offering work-readiness programs",
          "Providing investment management services"
        ],
        "correct_option": "Providing digital IT EPAs"
      },
      {
        "question": "Which apprenticeship standards does Accelerate People create End-point Assessments for?",
        "options": [
          "Level 7 Artificial Intelligence (AI) Data Specialist Apprenticeship",
          "Level 4 Business Analyst Apprenticeship",
          "Level 4 Cyber Security Technologist Apprenticeship",
          "Level 3 Digital Marketer Apprenticeship"
        ],
        "correct_option": "Level 7 Artificial Intelligence (AI) Data Specialist Apprenticeship"
      },
      {
        "question": "Which organization commends Agilisys for their dedication and expertise?",
        "options": [
          "NHSBSA",
          "Universitas Surabaya",
          "BCI Capital Limited",
          "ClearScore"
        ],
        "correct_option": "NHSBSA"
      },
      {
        "question": "What does Avado Learning specialize in?",
        "options": [
          "Cloud, IT, and digital transformation services",
          "Mobile English tests and certificates",
          "Investment management and advisory services",
          "Work-readiness programs and professional qualifications"
        ],
        "correct_option": "Work-readiness programs and professional qualifications"
      },
      {
        "question": "What does BCI Capital Limited provide?",
        "options": [
          "Digital IT EPAs",
          "Cloud, IT, and digital transformation services",
          "Work-readiness programs and professional qualifications",
          "Investment management and advisory services"
        ],
        "correct_option": "Investment management and advisory services"
      },
      {
        "question": "What does ClearScore offer for free?",
        "options": [
          "Access to credit score and report",
          "Work-readiness programs and professional qualifications",
          "Digital IT EPAs",
          "Cloud, IT, and digital transformation services"
        ],
        "correct_option": "Access to credit score and report"
      },
      {
        "question": "What can you identify by regularly checking your credit report?",
        "options": [
          "Signs of fraud",
          "Discounts on financial products",
          "Tips for improving your credit score",
          "Steps to increase your savings"
        ],
        "correct_option": "Signs of fraud"
      },
      {
        "question": "Which category on the ClearScore Support website addresses login issues?",
        "options": [
          "Sign-up problems",
          "Incorrect credit report sections",
          "Address-related concerns",
          "Login issues"
        ],
        "correct_option": "Login issues"
      },
      {
        "question": "What does ClearScore provide on their website to help you understand credit scores?",
        "options": [
          "Educational resources",
          "Exclusive pre-approved credit offers",
          "Personalized insights",
          "Monthly checklists"
        ],
        "correct_option": "Educational resources"
      },
      {
        "question": "What does Fospha specialize in fixing within 7 days?",
        "options": [
          "Credit scores",
          "Sales attribution",
          "Customer success",
          "Accounting errors"
        ],
        "correct_option": "Sales attribution"
      },
      {
        "question": "What is the main focus of Hive Learning's platform?",
        "options": [
          "Peer learning",
          "Financial management",
          "Marketing attribution",
          "Accounting automation"
        ],
        "correct_option": "Peer learning"
      },
      {
        "question": "What does Kloo offer as part of their platform for businesses?",
        "options": [
          "Accounts payable automation",
          "Credit score monitoring",
          "Sales attribution analysis",
          "Peer learning opportunities"
        ],
        "correct_option": "Accounts payable automation"
      },
       {
        "question": "What is the main focus of Koodoo?",
        "options": [
          "Providing personalized marketing solutions",
          "Offering embedded business finance solutions",
          "Transforming lending for the better",
          "Maximizing the mortgage vertical"
        ],
        "correct_option": "Maximizing the mortgage vertical"
      },
      {
        "question": "How does Liberis utilize Open Banking?",
        "options": [
          "To streamline the mortgage application process",
          "To expand access to funding for small businesses",
          "To detect and prevent financial fraud",
          "To provide personalized lending solutions"
        ],
        "correct_option": "To expand access to funding for small businesses"
      },
      {
        "question": "What is the product called that Liberis provides?",
        "options": [
          "Business Cash Advance",
          "Embedded Business Management",
          "Open Banking",
          "Mortgage Monitoring Tools"
        ],
        "correct_option": "Business Cash Advance"
      },
      {
        "question": "What is the role of AI in detecting and preventing financial fraud?",
        "options": [
          "To provide personalized lending solutions",
          "To maximize the mortgage vertical",
          "To enhance customer targeting",
          "To offer scalable and accurate fraud protection"
        ],
        "correct_option": "To offer scalable and accurate fraud protection"
      },
      {
        "question": "What is the main focus of Oakbrook?",
        "options": [
          "Providing personalized marketing solutions",
          "Offering embedded business finance solutions",
          "Transforming lending for the better",
          "Maximizing the mortgage vertical"
        ],
        "correct_option": "Transforming lending for the better"
      },
      {
        "question": "What is the aim of Modulr?",
        "options": [
          "To maximize the mortgage vertical",
          "To provide personalized lending solutions",
          "To automate payments in software",
          "To move money efficiently through businesses"
        ],
        "correct_option": "To move money efficiently through businesses"
      },
      {
        "question": "What is the main focus of Accelerate People?",
        "options": [
          "Providing digital IT EPAs",
          "Delivering successful digital transformations",
          "Offering work-readiness programs",
          "Providing investment management services"
        ],
        "correct_option": "Providing digital IT EPAs"
      },
      {
        "question": "Who has the final say on whether an apprentice is ready for their EPA?",
        "options": [
          "The training provider",
          "The employer",
          "The apprentice",
          "The EPA organisation"
        ],
        "correct_option": "The employer"
      },
      {
        "question": "Which level of apprenticeship does Agilisys offer in Artificial Intelligence (AI) Data Specialist?",
        "options": [
          "Level 7",
          "Level 4",
          "Level 3",
          "Level 5"
        ],
        "correct_option": "Level 7"
      },
      {
        "question": "What is the focus of Agilisys' digital transformation services?",
        "options": [
          "Enhancing public services",
          "Providing high-quality customer services",
          "Offering cloud solutions",
          "Delivering successful outcomes"
        ],
        "correct_option": "Enhancing public services"
      },
      {
        "question": "What does Avado Learning specialize in?",
        "options": [
          "Digital transformations",
          "Investment management",
          "Work-readiness programs",
          "English language tests"
        ],
        "correct_option": "Work-readiness programs"
      },
      {
        "question": "Which academy does Avado offer for data-driven culture?",
        "options": [
          "Data Academy",
          "FastFutures Programme",
          "CIPD HR Courses",
          "Marketing Academy"
        ],
        "correct_option": "Data Academy"
      },
      {
        "question": "What type of courses does Avado offer for HR and L&D professionals?",
        "options": [
          "Data science courses",
          "English communication courses",
          "HR courses",
          "Marketing courses"
        ],
        "correct_option": "HR courses"
      },
      {
        "question": "What services does BCI Capital Limited provide?",
        "options": [
          "Digital transformations",
          "Work-readiness programs",
          "Investment management"
        ],
        "correct_option": "Investment management"
      },
      {
        "question": "What can you identify by regularly checking your credit report?",
        "options": [
          "Signs of fraud",
          "Discounts on purchases",
          "New job opportunities",
          "Health insurance plans"
        ],
        "correct_option": "Signs of fraud"
      },
      {
        "question": "Which website can you visit for assistance with ClearScore?",
        "options": [
          "ClearScore Support",
          "ClearScore Education",
          "ClearScore Credit",
          "ClearScore Savings"
        ],
        "correct_option": "ClearScore Support"
      },
      {
        "question": "What can you learn about on ClearScore's website?",
        "options": [
          "Credit scores and reports",
          "Cooking recipes",
          "Gardening tips",
          "Fashion trends"
        ],
        "correct_option": "Credit scores and reports"
      },
      {
        "question": "What services does ClearScore provide for free?",
        "options": [
          "Access to credit score and report",
          "Personalized insights and tips",
          "Exclusive pre-approved credit offers",
          "All of the above"
        ],
        "correct_option": "All of the above"
      },
      {
        "question": "What does Contentive specialize in?",
        "options": [
          "Reinventing B2B media and events",
          "Creating mobile apps",
          "Designing websites",
          "Managing social media accounts"
        ],
        "correct_option": "Reinventing B2B media and events"
      },
      {
        "question": "How many senior executives does Contentive engage annually?",
        "options": [
          "1 million",
          "5 million",
          "10 million",
          "12 million"
        ],
        "correct_option": "12 million"
      },
      {
        "question": "What does Fospha specialize in fixing within 7 days?",
        "options": [
          "Credit scores",
          "Sales attribution",
          "Marketing strategies",
          "Customer acquisition"
        ],
        "correct_option": "Sales attribution"
      },
      {
        "question": "What is the key feature of Fospha's platform?",
        "options": [
          "Flawless marketing data",
          "Real-time insights",
          "Customer support",
          "Social media management"
        ],
        "correct_option": "Flawless marketing data"
      },
      {
        "question": "What is Hive Learning's main focus?",
        "options": [
          "Reinventing B2B media and events",
          "Creating mobile apps",
          "Designing websites",
          "Managing social media accounts"
        ],
        "correct_option": "Reinventing B2B media and events"
      },
      {
        "question": "What type of customers does Koodoo offer mortgage services to?",
        "options": [
          "a) Buyers",
          "b) Remortgagers",
          "c) Home movers",
          "d) All of the above"
        ],
        "correct_option": "d) All of the above"
      },
      {
        "question": "How does Koodoo collaborate with aggregators to maximize their mortgage vertical?",
        "options": [
          "a) By activating customers",
          "b) By engaging customers",
          "c) By converting customers",
          "d) All of the above"
        ],
        "correct_option": "d) All of the above"
      },
      {
        "question": "What does Koodoo's unique sourcing system combined with lender eligibility rules do?",
        "options": [
          "a) Streamlines the mortgage application process",
          "b) Increases conversion rates",
          "c) Provides direct access to tailored products",
          "d) All of the above"
        ],
        "correct_option": "d) All of the above"
      },
      {
        "question": "What do Koodoo's mortgage monitoring tools improve?",
        "options": [
          "a) Customer targeting",
          "b) Personalized marketing",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      },
      {
        "question": "What does Open Banking empower customers to do?",
        "options": [
          "a) Share their transaction data with third parties",
          "b) Have greater control over their account information",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      },
      {
        "question": "How does Liberis utilize Open Banking?",
        "options": [
          "a) To expand access to funding for small businesses",
          "b) To access real-time transaction data",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      },
      {
        "question": "What does embedded business management provide for small businesses?",
        "options": [
          "a) Support for operations management",
          "b) Seamless integration of financial services",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      },
      {
        "question": "What is Liberis' product called that is a form of receivables finance?",
        "options": [
          "a) Business Cash Advance",
          "b) Business Loan",
          "c) Business Credit",
          "d) Business Investment"
        ],
        "correct_option": "a) Business Cash Advance"
      },
      {
        "question": "What is the minimum monthly repayment expected by Liberis for their Business Cash Advance?",
        "options": [
          "a) Up to 1% of the total owed",
          "b) Up to 2% of the total owed",
          "c) Up to 3% of the total owed",
          "d) Up to 4% of the total owed"
        ],
        "correct_option": "c) Up to 3% of the total owed"
      },
      {
        "question": "What is the role of AI in detecting and preventing financial fraud in embedded finance?",
        "options": [
          "a) Real-time analysis to detect fraudulent transactions",
          "b) Proactive fraud management",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      },
      {
        "question": "What does Oakbrook aim to do in the lending industry?",
        "options": [
          "a) Transform lending for the better",
          "b) Provide personalized lending solutions",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      },
      {
        "question": "What does Rajasthan Royals aim to do through cricket?",
        "options": [
          "a) Transform society",
          "b) Transform cricket",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      },
      {
        "question": "What does Modulr aim to do with their digital payment service?",
        "options": [
          "a) Make money flow more efficiently through businesses",
          "b) Make money flow more efficiently through the economy",
          "c) Both a) and b)",
          "d) None of the above"
        ],
        "correct_option": "c) Both a) and b)"
      }  
    ]
  }
  

df = pd.DataFrame(json_data["questions"])

df[["Option1", "Option2", "Option3", "Option4"]] = pd.DataFrame(df["options"].tolist(), index=df.index)

df.drop(columns=["options"], inplace=True)

output_file = "questions_and_options.xlsx"
df.to_excel(output_file, index=False)

print(f"Data saved to '{output_file}'.")