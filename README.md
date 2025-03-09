# 🚀 Fine-Tuning Qwen 2.5 3B Model for AI Research QA

Welcome to the **Qwen 2.5 3B Model Fine-Tuning Project**! This project demonstrates the fine-tuning of a powerful language model to create a specialized system capable of answering complex AI research questions.


---

## 🎯 Project Objectives
- Fine-tune the **Qwen 2.5 3B Base model** for domain-specific AI research question answering.
- Implement **Retrieval-Augmented Generation (RAG)** to improve response accuracy.
- Quantize the model for optimized deployment.
- Document the entire process with a **technical report** and **evaluation results**.

---

## 🛠️ Setup and Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/AmandaHanz/Intellihack_CypherZ_Task03.git
cd Intellihack_CypherZ_Task03
```

2. **Create a Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```


3. **Install Additional Libraries:**
```bash
pip install transformers torch datasets bitsandbytes accelerate wandb
```

---

## 🚦 How to Run

### 1. **Training the Model:**
```bash
python scripts/training_script.py
```

### 2. **Running Inference:**
```bash
python scripts/inference_script.py
```
---



## 💡 Key Features
- **Fine-Tuning:** Customized for answering AI research questions.
- **Quantization:** Model reduced to 4-bit precision for speed and efficiency.
- **RAG Integration:** Uses BM25 Retriever for context-aware answers.
- **FastAPI Interface:** Provides an easy-to-use API for real-time inference.

---

## 🛡️ Best Practices Followed
- ✅ Model Versioning with Git
- ✅ Experiment Tracking with Weights & Biases
- ✅ Mixed Precision Training (`fp16`)
- ✅ Early Stopping to prevent overfitting

---

## 🧠 Future Enhancements
- **Reinforcement Learning:** Explore GRPO for improved reasoning.
- **Advanced Retrieval Techniques:** Implement more sophisticated RAG models.
- **Deployment:** Dockerize the application and integrate with Kubernetes for scalability.

---


Happy Fine-Tuning! 😊

