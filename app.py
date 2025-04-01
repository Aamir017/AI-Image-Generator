import os
import uuid
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for, flash
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Verify API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found. Please check your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Simple in-memory storage for users and their generated images
users = {}
user_images = {}

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        if not user_id:
            flash('Please enter a user ID')
            return redirect(url_for('login'))
        
        # Create user if not exists
        if user_id not in users:
            users[user_id] = {
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'last_login': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            user_images[user_id] = []
        else:
            users[user_id]['last_login'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        session['user_id'] = user_id
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    user_data = users.get(user_id, {})
    images = user_images.get(user_id, [])
    
    return render_template('dashboard.html', user_id=user_id, user_data=user_data, images=images)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Get the text prompt from the form
        prompt = request.form['prompt']
        
        try:
            # Generate image using OpenAI API
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            # Get the image URL from the response
            image_url = response.data[0].url
            
            # Save image data to user's history
            image_data = {
                'id': str(uuid.uuid4()),
                'prompt': prompt,
                'url': image_url,
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            user_id = session['user_id']
            if user_id not in user_images:
                user_images[user_id] = []
            
            user_images[user_id].append(image_data)
            
            # Return the result template with the image URL and original prompt
            return render_template('result.html', image=image_data, user_id=user_id)
        
        except Exception as e:
            error_message = str(e)
            return render_template('generate.html', error=error_message)
    
    # If it's a GET request, just render the form
    return render_template('generate.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)