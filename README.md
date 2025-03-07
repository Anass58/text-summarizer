# 📄 Text Summarizer

A Python-based text summarization tool using OpenAI's GPT API. This project extracts concise summaries from long-form text to save time and enhance content understanding.

## 📂 Project Structure
```
text-summarizer/
├── main.py              # Main application file
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```

## 🚀 Features
- Summarize long-form text into key insights.
- Customize summary length for flexibility.
- Simple and easy-to-use interface.

## 🛠️ Installation
1. Clone the repository:

```bash
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 📊 Usage
1. Ensure you have an OpenAI API key:

   Sign up at [OpenAI](https://platform.openai.com/signup) and get your API key.

2. Set your API key:

```bash
export OPENAI_API_KEY='your-api-key-here'  # Linux/macOS
set OPENAI_API_KEY='your-api-key-here'    # Windows
```

3. Run the summarizer:

```bash
python main.py
```

4. Input the text you want to summarize and receive a concise summary.

## 📌 Example Output
```
Enter text to summarize: This is a long document...
Summary: This document discusses...
```

## 📈 Customization
You can adjust:
- **Summary length**: Control how detailed the summary is.
- **Model parameters**: Fine-tune OpenAI API parameters.

## 🤝 Contributing
Contributions are welcome! Feel free to fork, open an issue, or submit a pull request.

## 📜 License
This project is licensed under the MIT License.

## 📧 Contact
For any inquiries, contact [a55.44.as47@gmail.com].

