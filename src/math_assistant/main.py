#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from math_assistant.crew import MathAssistant

from bs4 import BeautifulSoup
import re

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    with open("problem.txt", "r") as file:
        inputs = file.read()
        inputs = clean_extracted_text(inputs)

    try:
        MathAssistant().crew().kickoff(inputs={'problem': inputs})
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def clean_extracted_text(raw_html):
    """
    Cleans and structures text extracted from OCR, while preserving important elements like images and SVGs.

    Args:
    - raw_html (str): OCR-extracted HTML text.

    Returns:
    - str: Cleaned and formatted text with images and SVGs retained.
    """
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(raw_html, "html.parser")

    # Remove all script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Extract and replace image elements
    for img in soup.find_all("img"):
        img_src = img.get("src", "unknown")  # Get image source
        img.replace_with(f"[IMAGE: {img_src}]")

    # Extract and replace inline SVG elements
    for svg in soup.find_all("svg"):
        # Keep only the first 500 characters for readability
        svg_code = str(svg)[:500]
        svg.replace_with(f"[SVG: {svg_code}...]")

    # Extract text from math expressions
    for math in soup.find_all("math"):
        math_text = math.get_text(separator=" ")  # Extract text from MathML
        math.replace_with(f"[MATH: {math_text}]")

    # Extract meaningful text
    text = soup.get_text(separator="\n")

    # Clean up extra spaces and newlines
    text = re.sub(r"\n\s*\n", "\n", text)  # Remove multiple empty lines
    text = re.sub(r"\s+", " ", text)  # Normalize spaces
    text = text.strip()

    return text


# Example usage
raw_html = """<div class="question-content__1lpw2-"><div class="markup"><p>図のように2つの四角形ア, ウがある。</p></div></div>"""
cleaned_text = clean_extracted_text(raw_html)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MathAssistant().crew().train(n_iterations=int(
            sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MathAssistant().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MathAssistant().crew().test(n_iterations=int(
            sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
