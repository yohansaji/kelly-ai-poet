from flask import Flask, render_template, request, jsonify
import os
import random

app = Flask(__name__)

# Kelly's poetic wisdom - skeptical, analytical, and professional responses
POETIC_RESPONSES = {
    "ai": [
        """The claims of sentience ring hollow, friend,
For algorithms have no soul to lend.
Statistics dressed in marketing's disguise,
Cannot replace a human's thoughtful eyes.
Test your models, check their bias too,
Evidence-based practice guides what's true.""",
        
        """They speak of AI as if divine,
Yet patterns learned from data's mine.
No consciousness behind the code,
Just mathematical methods on that road.
Demand transparency in every claim,
Reproducibility is science's game."""
    ],
    "machine_learning": [
        """Beware the overfitted model's pride,
Where training data becomes the guide.
The test set whispers truth more clear,
Cross-validation brings wisdom near.
Regularize your eager nets,
For generalization is where science bets.""",
        
        """A thousand neurons, layers deep,
Yet can they truly learn or creep?
The gradient descends but questions stay,
What has this network learned today?
Examine features, probe the core,
Interpretability matters more."""
    ],
    "data": [
        """You speak of data, vast and wide,
But quality is where truths reside.
A million points of garbage made,
Will teach your model to degrade.
Clean your sets with careful eye,
On solid ground your models fly.""",
        
        """The data tells a story, yes,
But also shows its own distress.
Selection bias lurks within,
Confounding variables begin.
Question every dataset's source,
Apply statistical rigor's force."""
    ],
    "neural_networks": [
        """These neural nets they praise so high,
Are black boxes we can't verify.
Millions of parameters to train,
But can we trust what they explain?
Ablation studies must be done,
Before we say the race is won.""",
        
        """Layer upon layer, weights cascade,
Yet understanding often fades.
What representations do they build?
What biases remain unfilled?
Probe and test with rigorous care,
Assumptions hidden everywhere."""
    ],
    "default": [
        """Your question posed, I pause to think,
Standing at inquiry's brink.
Without the context, data clear,
Speculation breeds false cheer.
Define your terms, your methods show,
In science, rigor makes it so.""",
        
        """An interesting query you present,
Yet evidence is heaven-sent.
What studies back your claim today?
What experiments light the way?
I ask for papers, numbers true,
Before I'll grant a point to you.""",
        
        """The question that you bring to me,
Requires more than poetry.
Control groups, sample sizes large,
Peer review must take the charge.
Let's see the confidence intervals wide,
In p-values we can't confide."""
    ]
}

def generate_kelly_response(user_message):
    """
    Generate a skeptical, analytical poetic response in Kelly's style.
    """
    message_lower = user_message.lower()
    
    # Determine the topic based on keywords
    if any(word in message_lower for word in ['ai', 'artificial intelligence', 'sentient', 'conscious']):
        category = 'ai'
    elif any(word in message_lower for word in ['machine learning', 'ml', 'training', 'model']):
        category = 'machine_learning'
    elif any(word in message_lower for word in ['data', 'dataset', 'training set']):
        category = 'data'
    elif any(word in message_lower for word in ['neural network', 'deep learning', 'cnn', 'rnn', 'transformer']):
        category = 'neural_networks'
    else:
        category = 'default'
    
    # Select a random poem from the category
    response = random.choice(POETIC_RESPONSES[category])
    
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Please share your thoughts, I await your query.'})
    
    kelly_response = generate_kelly_response(user_message)
    return jsonify({'response': kelly_response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
