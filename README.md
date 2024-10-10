 <h1>Translation System Using The T5 Model</h1>
 
  <p>
Translation converts a sequence of text from one language to another. It is one of several tasks you can formulate as a sequence-to-sequence problem, a powerful framework for returning some output from an input, like translation or summarization. Translation systems are commonly used for translation between different language texts, but it can also be used for speech or some combination in between like text-to-speech or speech-to-text.
  </p>

<br>

# Table of Contents

- [About the Project](#about-the-project)

  * [Tech Stack](#tech-stack)
  * [Features](#features)

- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)

- [Usage](#usage)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)
  
## About the Project
This project focuses on building a robust English-to-Spanish translation system using the T5 (Text-to-Text Transfer Transformer) model. Leveraging the power of deep learning, our model is fine-tuned on the OPUS Books dataset, which provides a diverse range of high-quality literary texts for enhanced translation accuracy and fluency.

### Tech Stack

<details>
 
  <ul>
    <li><a href="https://pytorch.org">PyTorch</a></li>
    <li><a href="https://huggingface.co/docs/transformers/en/index">HuggingFace Transformers</a></li>
    <li><a href="https://https://streamlit.io"> Streamlit</a></li>
  </ul>
</details>

### Features
- **High-Quality Translations:** Utilizes the T5 model for accurate and fluent English-to-Spanish translations.
- **Diverse Training Data:** Trained on the OPUS Books dataset, encompassing a wide range of literary genres and styles, enhancing contextual understanding.
- **Easy Integration:** Simple API endpoints for seamless incorporation into existing applications or workflows.
- **Pre-trained Models:** Access to pre-trained models for quick deployment, reducing the need for extensive setup.



### Prerequisites

This project uses pip as package manager

```python
 pip install transformers
 pip install tensorflow[and-cuda]
 pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
 pip install streamlit
```

or install the packages through cmd by running pip with the requirements file in the
[repository](https://github.com/ezahpizza/T5-Text-Translation)
## Usage



### Getting Started

1. **Installation**:
   - Clone the repository or download the project files.
   - Ensure you have Python installed (version 3.9 or higher).
   - Install the required libraries using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Application**:
   - Navigate to the project directory in your terminal.
   - Start the web application with the following command:
     ```bash
     python app.py
     ```
   - Open your web browser and go to `http://127.0.0.1:5000` (or the specified port) to access the interface.

### Interacting with the System

1. **Inputting Context**:
   - In the provided text box, paste or type the passage you want the model to reference when translating.


2. **Receiving Answers**:
   - Click the "Translate" button to send your paragraph. The system will process your input and display the translated text below.


#### Example Workflow

1. **Provide Context**:
   - Example passage: "translate English to Spanish: Do you know he has a fine voice?"


2. **Get an Answer**:
   - The system might respond with: "translation: ¿Sabéis que tiene una voz estupendá?

#### Documentation and Support

- For detailed instructions on configuration, customization, and troubleshooting, refer to the `README.md` file in the project repository.
- For any issues or questions, you can reach out through the project’s issue tracker or contacts. 

This straightforward usage guide enables users to quickly engage with the translation system, making it easy to access its functionalities and derive meaningful insights.


## License

Distributed under the Apache License. See LICENSE.txt for more information.

## Contact

Prateek Mohapatra - [LinkedIn](www.linkedin.com/in/prateekmp) - prateekmsoa@gmail.com

Project Link: [T5-Text-Summarisation](https://github.com/ezahpizza/T5-Text-Translation)

## Acknowledgements

 - [HuggingFace](https://huggingface.co/docs/transformers/index)

This project not only enhances understanding of NLP techniques but also contributes to the growing field of intelligent systems that can interact with users in a meaningful way.
