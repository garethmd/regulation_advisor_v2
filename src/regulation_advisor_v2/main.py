#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from .crew import RegulationAdvisorV2

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run(question: str):
    """
    Run the crew.
    """
    # question = input("what is your question?")
    inputs = {"topic": "AI Legislation", "question": question}

    try:
        RegulationAdvisorV2().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
