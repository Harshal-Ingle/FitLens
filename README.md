# FitLens
### VisionDiet AI – An Intelligent Image-Based Nutrition & Object Insight Assistant

**Project Overview:**
VisionDiet AI is an interactive image-understanding application built using Streamlit, Groq Vision Models, and Python.
The system allows users to upload an image—such as a food item, flower, animal, product, or any real-world object—and instantly receive meaningful insights.

**Example use cases:**

- Identify unknown foods
- Get nutritional information such as calories, protein, fat, carbs
- Detect animals/plants for educational purposes
- Ask any custom question about the image
- Understand content similar to Google Lens but with AI-enhanced reasoning
- Users can run the app with one simple command:
- python -m streamlit run main.py

**Problem Statement**

In daily life, people frequently encounter objects—especially foods—that they cannot easily identify.
Common challenges include:

- Not knowing what food they are eating
- Having no idea about its calories or protein
- Difficulty identifying fruits, vegetables, flowers, animals, etc.
- Needing to manually search on Google, which is time-consuming
- No personalized space to ask follow-up questions about an image
- There is a need for a tool that can instantly analyze an image and provide accurate, conversational, AI-driven explanations.

**Solution Statement**

VisionDiet AI solves this problem by allowing users to:

- Upload any image (food, animal, flower, object, etc.)
- Convert the image to base64 and feed it to Groq’s multimodal model
- Ask any question related to the image:
– “How many calories does this food have?”
– “What is this flower called?”
– “Tell me facts about this fruit.”
- Get real-time, AI-generated responses with high accuracy.

The application behaves like a custom Google Lens with intelligence, providing not only identification but also context, nutrition insights, and explanations.

**1. User Interface (Frontend)**

Built using Streamlit
Allows:
Image upload
Writing user queries
Viewing model responses
Adjusting parameters (temperature, top-p, max tokens)

**2. Backend Processing**

Image is encoded to base64
Custom prompt + image is sent to Groq Vision Model (LLaMA 4 Scout 17B)
Model processes:

Image recognition
-Object details
Nutritional estimation
Q&A reasoning

**3. AI Model Layer**

**Model used: meta-llama/llama-4-scout-17b-16e-instruct**

Handles:
- Multimodal image + text input
- Vision inference
- Natural-language response generation

**4. Output Layer**

- Groq response is parsed and displayed in Streamlit
- Final output appears cleanly in the user interface
- Essential Tools and Utilities

**1. Streamlit**

- For building the web UI
- File uploader
- Sliders (temperature, tokens, top_p)
- Displaying images and results

**2. Groq API**

- Provides ultra-fast multimodal LLM inference
- Handles all image + text processing
  
**3. Python Libraries**

1. dotenv → Manages API keys safely
2. Pillow (PIL) → Handles image reading
3. base64 → Converts images for Groq API
4. os → Environment variable access
5. time → For UX loading effects
  
**4. Environment Setup**

.env for storing GROQ_API_KEY
Command to run:

***python -m streamlit run main.py***

**Conclusion:**
The VisionDiet AI project demonstrates how multimodal AI can simplify real-world object understanding by combining image analysis with natural-language reasoning. By allowing users to upload any image and instantly receive meaningful insights—such as food identification, nutritional details, or general object information—the system offers a practical and intelligent alternative to manual searching or basic visual tools. Built using Streamlit and Groq’s high-performance vision models, the application delivers fast, accurate, and interactive responses, making it a valuable tool for health enthusiasts, learners, and everyday users alike. This project showcases the powerful potential of AI-driven image assistants and sets the foundation for more advanced, user-focused vision applications in the future.
