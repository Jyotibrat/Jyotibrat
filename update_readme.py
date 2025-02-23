import random
import time

# Different layouts for the Skills & Technologies section
layouts = [
    "### **Programming Languages**\n![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)\n![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white)\n### **Web Development**\n![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)\n![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)",
    
    "### **Web Development**\n![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)\n![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)\n### **Programming Languages**\n![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)\n![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)",

    "### **AI & ML**\n![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)\n![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)\n### **Databases**\n![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)\n![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)"
]

# Read the existing README file
with open("README.md", "r", encoding="utf-8") as file:
    content = file.readlines()

# Locate the Skills & Technologies section
start_index = next(i for i, line in enumerate(content) if "## 🛠️ Skills & Technologies" in line)

# Replace with a new random layout
new_content = content[:start_index + 1] + ["\n" + random.choice(layouts) + "\n"]

# Write updated README
with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(new_content)

print("README updated successfully!")
