# Parsing patient data

A simple example showing how to use AI to structure unstructured patient data and process it with Python.

These are the requirements:
1. **Sample_patient_report.pdf** - medical report with unstructured data.
2. **Prompt.txt** - prompt we provide to an LLM.
3. **Python** - valid instalation with a plotting library.

In case you want a plottig library we can install matplotlib:
```bash
pip install matplotlib
```

## Step 1
- Load the file inside your favourite AI chatbot. Ex: ChatGPT
- Paste the contents of Prompt.txt
- Run the prompt and check the output.

## Step 2
- AI chatbot will reply with the JSON that structures the data nicely.
- Copy that json to the place where you want to write your python script.
- In case you run into problems or you want to skip step 1 & 2, you have (**patientdata.json**)

## Step 3
- Write python to load the data.
- Create 2 lists that get the dates and scores from the tracking information.
- Use matplotlib or any other equivalent to chart it.
- In case you want to skip step 3, or run into problems you have (**plot_patient_info.py**)

## Step 4
- Run script & preview plot.
- Draw conclusions or play around with the data.
- In case you run into problems you have the saved plot as image (**Figure_1.png**)

## Conclusions
- We can use AI to extract data from unstructured documents.
- That data can easily be loaded and processed with automations.
- Providing private data to public AI models poses privacy, ethical, and legal risks.
- You can either use an internal hospital approved AI tool for this or anonymize the patient report for the public domain.
- This example uses a synthetic patient report to demonstrate each step.