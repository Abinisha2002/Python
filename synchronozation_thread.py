import threading

# Shared resource
counter = 0

# Function to increment the counter without synchronization
def increment_without_lock():
    global counter
    for _ in range(100000):
        counter += 1

# Function to increment the counter with synchronization using a lock
def increment_with_lock(lock):
    global counter
    for _ in range(100000):
        # Acquire the lock before accessing the shared resource
        lock.acquire()
        counter += 1
        # Release the lock after modifying the shared resource
        lock.release()

def main():
    # Creating a lock
    lock = threading.Lock()

    # Creating threads without synchronization
    threads_without_lock = []
    for _ in range(5):
        t = threading.Thread(target=increment_without_lock)
        threads_without_lock.append(t)
        t.start()

    # Waiting for threads without synchronization to complete
    for t in threads_without_lock:
        t.join()

    print(f"Counter value without lock: {counter}")

    # Reset counter for synchronized increment
    counter = 0

    # Creating threads with synchronization
    threads_with_lock = []
    for _ in range(5):
        t = threading.Thread(target=increment_with_lock, args=(lock,))
        threads_with_lock.append(t)
        t.start()

    # Waiting for threads with synchronization to complete
    for t in threads_with_lock:
        t.join()

    print(f"Counter value with lock: {counter}")

if __name__ == "__main__":
    main()
