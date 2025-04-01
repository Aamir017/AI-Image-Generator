# AI Image Generator

A web application that generates images from text descriptions using OpenAI's DALL-E model.

## Features

- User account system with personalized dashboards
- Text-to-image generation using OpenAI's DALL-E 3
- Image history and gallery view
- Responsive design for all devices

## Requirements

- Python 3.7+
- Flask
- OpenAI API key
- Internet connection

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages:

pip install flask openai python-dotenv

3. Create a `.env` file in the project root directory and add your OpenAI API key: 

OPENAI_API_KEY=your_openai_api_key_here

4. Run the application:

python app.py

5. Open your web browser and navigate to:

http://127.0.0.1:5000/


## Usage

1. On the homepage, click "Get Started" to begin.

2. Enter a user ID to log in or create a new account.

3. From your dashboard, click "Create New Image" to generate an image.

4. Enter a detailed description of the image you want to create.

5. Click "Generate Image" and wait for the AI to create your image.

6. View, download, or create more images from the result page.

7. All your generated images will appear in your dashboard gallery.

## Tips for Better Results

- Be specific and detailed in your descriptions
- Include information about style, colors, lighting, and mood
- Mention the perspective or angle you want
- Experiment with different phrasings if you don't get the desired result

## Project Structure

- `app.py`: Main application file with Flask routes and OpenAI integration
- `templates/`: HTML templates for the web interface
- `static/css/`: CSS stylesheets for the application
- `.env`: Environment variables file (contains API key)

## Limitations

- Image generation is limited by the capabilities of the DALL-E 3 model
- API usage may incur costs depending on your OpenAI account plan
- Internet connection is required for image generation

## Troubleshooting

- If images fail to generate, check your OpenAI API key and internet connection
- If the application fails to start, ensure all required packages are installed
- For any other issues, check the console output for error messages

## License

This project is for educational purposes only.

## Credits

- OpenAI for the DALL-E API
- Flask web framework
- Poppins font from Google Fonts

## Author

Created by: [Your Name]
Contact: [Your Email]
GitHub: [Your GitHub Profile]

## Acknowledgements

Special thanks to the OpenAI team for providing the powerful DALL-E API that makes this application possible.