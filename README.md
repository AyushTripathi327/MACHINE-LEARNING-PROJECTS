Invoice Audit System using Machine Learning

Hi! This is a simple but smart web app that helps audit teams catch duplicate or fake invoices. Instead of using old Excel formulas, I used Machine Learning so the system can think dynamically and catch fraud patterns intelligently.

 What problem does it solve?
Usually, billing systems check for exact duplicates. If a fraudster changes an invoice from ₹4500 to ₹4501, normal software will miss it. 

But my model learns the "risk zone." Since it knows ₹4500 with 18% GST is a known duplicate, it automatically flags ₹4501 as suspicious too!

 Cool Features
- **Smart Detection:** Catches nearby fraud amounts using Machine Learning.
- **Easy UI:** A clean web dashboard made with Streamlit—anyone can use it.
- **Data Viewer:** A simple checkbox to see the actual history data right on the screen.

## 🛠️ Built With
- Python (Core language)
- Streamlit (For making the web screen)
- Pandas (For handling the data table)
- Scikit-Learn (For the Random Forest ML model)
-How MACHINE LEARNING WORKS
I used the Random Forest Classifier algorithm. Instead of a single decision, it creates 10 small "mental check-posts" (Decision Trees) in the background. It studies the 10 sample invoice logs I provided, finds the hidden connection between the Amount, GST, and Fraud status, and takes a final vote to tell if a new invoice is Original or a Duplicate Pattern.

👤 Author
Ayush
Tech Stack: Python & Machine Learning