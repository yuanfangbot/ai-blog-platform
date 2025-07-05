import openai
import random
from datetime import datetime

# AI article generation function
def generate_article():
    topics = ['Zero Trust Networks', 'Cloud Security', 'Kubernetes Tutorial', 'React Optimization', 'Cybersecurity Frameworks']
    levels = ['Beginner', 'Intermediate', 'Advanced']
    emotions = ['😊', '💡', '⚡️', '🔒', '🚀']

    topic = random.choice(topics)
    prompt = f"Write a detailed technical article about {topic} for {random.choice(levels)} professionals. " \
              "Include practical examples and use {random.choice(emotions)} to emphasize key points."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Generate 16 unique articles
for i in range(16):
    article = generate_article()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"content/posts/article_{i+1}_{timestamp}.md"
    
    with open(filename, 'w') as f:
        f.write(f"---\ntitle: 'Article {i+1}'\ndate: {datetime.now().isoformat()}\ndraft: false\ntags: ['tech', 'security']\n---\n\n")
        f.write(article)