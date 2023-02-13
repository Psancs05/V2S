import cohere
import config


def connect_cohere():
    """Connect to the Cohere API"""
    global co
    api_key = config.api_key
    co = cohere.Client(api_key)


def generate_prompt(file):
    """Generates the prompt for the text summarization"""
    with(open(file, 'r')) as f:
        text = f.read()
    return text + "\n In summary,"


def make_prediction(prompt):
    """Makes the prediction using the Cohere API"""
    return co.generate(
        model='xlarge',
        prompt=prompt,
        return_likelihoods='GENERATION',
        stop_sequences=['--'],
        max_tokens=150,
        temperature=0.7,
        num_generations=1,
        k=0,
        p=0.75,
    )


def process_prediction(prediction):
    """Processes the prediction"""
    # Print the prediction cutting the text after the last period
    prediction = prediction[0][:prediction[0].rfind('.')+1]
    # Remove the first character if it is a space
    prediction = prediction[1:] if prediction[0] == ' ' else prediction
    # Print the fisrt character in uppercase
    prediction = prediction[0].upper() + prediction[1:]
    return "TEXT SUMMARIZATION:\n" + prediction

# --------------------- Main function ---------------------


def summarization(file):
    """Summarizes the text"""
    print("Summarizing text...")
    connect_cohere()
    prompt = generate_prompt(file)
    prediction = make_prediction(prompt)
    summ = process_prediction(prediction)
    print("Summarization complete")
    print(summ)
