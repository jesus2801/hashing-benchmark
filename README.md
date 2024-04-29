# Hashing Benchmark

This project is a basic script that benchmarks two hashing libraries: Bcrypt and Hashlib.
Bcrypt is known by its delayed algorithm that ensure you have a more secure hashing algorithm, in the other hand
hashlib (the built-in hashing library from Python) is easier to use but its algorithm is pretty fast (which is not good).

## Installation:
**Step 1: Clone the repository**
```
git clone https://github.com/jesus2801/hashing-benchmark.git
```
**Step 2 (Optional): Create a virtual enviroment**
```
python -m venv env
source env/bin/activate
```

**Step 3: Install libraries**
```
pip install -r requirements.txt
```

**Step 4: Run the script**
```
python app/main.py
```