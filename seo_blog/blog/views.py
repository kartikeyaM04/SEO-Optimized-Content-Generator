from django.shortcuts import render
from blog.forms import BlogPromptForm 
import google.generativeai as genai

def generate_blog(request):
    blog_content = None
    if request.method == 'POST':
        form = BlogPromptForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            keywords = form.cleaned_data['keywords']
            tone = form.cleaned_data['tone']

            prompt = (
            f"You are a highly experienced SEO-focused content writer with over 10 years in the field."
            f" Your mission is to create a deeply researched, trend-aware, SEO-optimized blog post on the topic: '{topic}', targeting these specific keywords: {keywords}."
            f"\n\nGuidelines:"
            f"\n- Start the article with the main focus keyword in the opening sentence."
            f"\n- Follow the latest Google guidelines—including E-E-A-T (Expertise, Experience, Authority, Trustworthiness) and Helpful Content guidelines."
            f"\n- Make every section practical, insightful, and highly relevant for today's search intent and Google's AI Overview/SGE."
            f"\n- Maintain a clear, natural, and engaging tone: '{tone}'. Avoid robotic or formulaic wording; write as if sharing knowledge with a friend. As we need to make the content less robitic to acheive 0% AI plag"
            f"\n- Write concise sentences (preferably under 10 words each), using simple everyday language—do not use jargon or long, complex phrases."
            f"\n- Structure the article with logical, descriptive subheadings for every main idea."
            f"\n- Do not use any keyword (including variations) more than two times throughout the content."
            f"\n- Ensure originality, helpfulness, and a fresh perspective drawn from recent industry research or authoritative sources."
            f"\n- Make the information actionable, practical, and genuinely valuable for readers searching in 2025."
            f"\n- Avoid any detectable AI patterns and focus on unique insights, real-life examples, and a conversational style."
)


            # Gemini API Call
            try:
                # Hardcode the API key (not recommended for production)
                genai.configure(api_key="<API_KEY>")
                model = genai.GenerativeModel("gemini-2.5-pro")
                response = model.generate_content(prompt)
                blog_content = response.text
            except Exception as e:
                blog_content = f"Error generating content: {str(e)}"

    else:
        form = BlogPromptForm()

    return render(request, 'blog/generate_blog.html', {'form': form, 'blog_content': blog_content})
