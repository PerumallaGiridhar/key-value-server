import uuid
import random
import string

def generate_random_string(length):
    """Generate a random string of given length."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_data(num_records):
    """Generate 1 million UUIDs with random strings."""
    data = []
    for _ in range(num_records):
        uuid_str = str(uuid.uuid4())
        random_str = generate_random_string(random.randint(1, 20))
        data.append(f"{uuid_str} {random_str}")
    return data

# Example: Generate 1 million records
one_million_records = generate_data(1000000)
with open('example.input.large.data', 'w') as f:
    for line in one_million_records:
        f.write(line)
        f.write('\n')

# Print the first few records
for record in one_million_records[:5]:
    print(record)
