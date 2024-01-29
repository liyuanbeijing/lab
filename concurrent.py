import concurrent.futures

def job(task):
    # Do some work here
    print(f"Task {task} is completed")

# Create a list of tasks
tasks = [1, 2, 3, 4, 5]

# Create a ThreadPoolExecutor with maximum 5 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit each task to the executor
    futures = [executor.submit(job, task) for task in tasks]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)
