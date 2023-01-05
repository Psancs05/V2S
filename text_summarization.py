import cohere
import config

api_key = config.api_key

# Connect to Cohere API using your API key
co = cohere.Client(api_key)
    
# Get the text to summarize from transcript.txt
with(open('transcript.txt', 'r')) as f:
    text = f.read()
    
# Build the prompt adding to the text the words "In summary, "
prompt = text + "\n In summary, "

# Make the prediction
prediction = co.generate(
    model='xlarge',
    prompt=prompt,
    return_likelihoods = 'GENERATION',
    stop_sequences=['--'],
    max_tokens=150,
    temperature=0.7,
    num_generations=1,
    k=0,
    p=0.75,
)

def process_prediction(prediction):
    # Print the prediction cutting the text after the last period
    prediction = prediction[0][:prediction[0].rfind('.')+1]
    
    # Remove the first character if it is a space
    prediction = prediction[1:] if prediction[0] == ' ' else prediction
    
    # Print the fisrt character in uppercase
    prediction = prediction[0].upper() + prediction[1:]
    
    return "TEXT SUMMARIZATION:\n" + prediction

print(process_prediction(prediction))
