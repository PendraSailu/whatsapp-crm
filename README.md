# 📱 WhatsApp CRM Tool

![Status](https://img.shields.io/badge/status-active-success) ![Python](https://img.shields.io/badge/python-3.10-blue)  

A simple internal tool to broadcast WhatsApp messages to users. This tool now includes a **Predefined Message Generator** feature, allowing users to create messages from a prompt and tweak them before sending.

---

## ✨ Features

- **📢 Broadcast Messages:** Send WhatsApp messages to multiple users at once.  
- **📝 Message Templates:** Use predefined message templates to save time.  
- **🤖 Predefined Message Generator:** Generate custom messages using a prompt.  

**Example:**  
- Prompt: "I want to send a Diwali wish to my customers."  
- Generated Message: "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!"

---

## ⚙️ Installation

1. Clone the repository:  
   `git clone <your-repo-url>`  
2. Create a virtual environment and activate it:  
   `python -m venv .venv`  
   `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`)  
3. Install required dependencies:  
   `pip install -r requirements.txt`

---

## 🔧 Configuration

1. Add your WhatsApp API credentials in a configuration file or environment variables.  
2. Optionally, configure default message templates in `templates.json`.

---

## 🚀 Usage

**Broadcast Messages**  
- Open the tool and follow prompts to select recipients and message templates.  

**Generating Predefined Messages**  
- Input a prompt, e.g., "Send Diwali wishes to my customers".  
- Tool generates a ready-to-use message.  
- Edit or tweak the message if needed.  
- Send the generated message via broadcast.

---

## 🗂 Example Workflow

1. Open the tool.  
2. Select **Generate Predefined Message**.  
3. Input prompt: "Send Diwali wishes to my customers".  
4. Tool outputs: "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!"  
5. Edit message if needed.  
6. Send message to selected users.

---

## 🛠 Tech Stack

- Python  
- WhatsApp Business API / Twilio API  
- JSON for templates and user data  
- Command-line interface (CLI), extendable to web

---

## 🤝 Contributing

- Fork the repository.  
- Create a feature branch.  
- Commit changes and push the branch.  
- Open a pull request.

---

## 📄 License

This project is for **internal use only** and is not publicly licensed.
