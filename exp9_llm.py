import ollama
import time
import psutil
import os

# List of models to compare
models = ["phi3", "llama3.2:1b", "qwen2.5:0.5b"]

# List of prompts for evaluation
prompts = [
    "Explain the difference between BFS and DFS in simple terms.",
    "Write a Python function to check whether a number is prime.",
    "If a car travels at 60 km/h, how long will it take to cover 150 km? Explain step by step."
]

def get_memory_usage():
    """Returns current memory usage of the process in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)


print("Starting SLM / µLM Comparison Experiment...\n")

for model in models:
    print(f"\n{'='*60}")
    print(f"Model: {model}")
    print(f"{'='*60}")

    for i, prompt in enumerate(prompts, 1):
        print(f"\n Prompt {i} ")
        print(f"Prompt: {prompt}")

        start_time = time.time()
        start_mem = get_memory_usage()

        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.3}
        )

        end_time = time.time()
        end_mem = get_memory_usage()

        answer = response['message']['content']
        duration = end_time - start_time

        print(f"\nResponse:\n{answer}")
        print(f"\nTime taken: {duration:.2f} seconds")
        print(f"Memory change: {end_mem - start_mem:.2f} MB")

    print("-" * 40)