# Gen AI Playground and Site

This Dash application showcases interactive AI models for code completion and image generation, leveraging state-of-the-art models for natural language processing and image synthesis.

## Features

- **Code Completion**: Utilizes a language model to generate code based on user input.
- **Image Generation**: Generates images from textual descriptions using the Stable Diffusion model.
![IMG_5346](https://github.com/srlausten/generative-ai-site/assets/65357089/f0b21290-0eb1-43ae-addf-894249d8ed8a)

## Getting Started with Poetry

[Poetry](https://python-poetry.org/) is used for dependency management and packaging in this project. It simplifies package management and deployment.

### Prerequisites

- Python 3.8+
- Poetry

If you haven't installed Poetry yet, you can do so by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/srlausten/generative-ai-site.git
   cd generative_ai_site
   ```

2. **Install Dependencies with Poetry**:
   Poetry creates a virtual environment and installs all the required packages.
   ```bash
   poetry install
   ```

### Running the Application

Activate the virtual environment managed by Poetry and start the Dash application:

```bash
poetry shell
python app.py
```

Open `http://127.0.0.1:8050` in a web browser to interact with the application.

## Usage

Navigate through the application's tabs to access the different functionalities:

- **Code Completion**: Enter a code snippet or prompt, and press "Complete Code" to see the AI-generated completion.
- **Image Generation**: Type a descriptive prompt and click "Generate Image" to produce a visual representation.

## Contributing

We welcome contributions! Please feel free to fork the repository, make changes, and submit pull requests.

## Authors

- Sam Lausten - Initial Development

## Acknowledgments

- Thanks to the creators of the AI models and the Dash framework that made this application possible.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

