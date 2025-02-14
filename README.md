# TaskHarbour

A Django-based web application that provides multiple AI-powered generation services including image generation, music generation, README creation, and error solving capabilities.

## Features

- **Image Generation**: Creates images using the 3DRedmond-V1 model from Hugging Face
- **Music Generation**: Generates music using Facebook's MusicGen Small model
- **README Generator**: Creates project documentation using Gemini 1.5 Pro
- **Error Solver**: Helps debug code issues using AI assistance
- **Image Upscaling**: Allows users to upscale uploaded images

## Technologies Used

- Django
- Python
- Hugging Face API
- Google Gemini AI
- PIL (Python Imaging Library)
- BytesIO for file handling

## Setup

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd TaskHarbour
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Hugging Face API key
   - Google Gemini API key

4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```

## API Keys Required

- Hugging Face API token
- Google Gemini API key

## Usage

1. **Image Generation**
   - Navigate to the image generation page
   - Enter your prompt
   - Click generate to create an image

2. **Music Generation**
   - Visit the music generation page
   - Enter your music description
   - Generate and play the created audio

3. **README Generation**
   - Access the README generator
   - Input your project details
   - Get an auto-generated README file

4. **Error Solving**
   - Use the error solver page
   - Paste your code and error message
   - Receive AI-powered solutions

## Project Structure

(Provide a directory structure overview here)

## Security Notes

- API keys should be stored as environment variables
- The project includes safety settings for AI content generation
- Cache is cleared after image generation

## Contributing

Feel free to submit issues and enhancement requests!


