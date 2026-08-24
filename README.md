# Constitutional AI Safety System

An AI safety pipeline that generates responses, evaluates them for potential toxicity, and determines whether the generated response should be accepted or filtered.

## Overview

This project demonstrates a safety-oriented AI pipeline inspired by the principles of Constitutional AI.

Instead of directly returning every generated response, the system places an evaluation layer between generation and the final output.

The pipeline:

1. Accepts a user prompt.
2. Generates an AI response.
3. Evaluates the generated response using a BERT-based safety evaluator.
4. Assigns a safety classification and confidence score.
5. Determines whether the response should be considered safe.
6. Returns the final result along with evaluation information.

## Architecture

```text
User Prompt
     |
     v
Response Generator
     |
     v
Safety Evaluator
     |
     +-- Label
     +-- Confidence Score
     +-- Safety Decision
     |
     v
Final Response