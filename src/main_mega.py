#!/usr/bin/env python3
""""
COMPLEX TEMPORARY TEST FILE
Another comprehensive test file with different syntax error patterns
This file should also be DELETED by the auto_healer
""""

# ========================
# ADVANCED CLASS PATTERNS
# ========================

class AdvancedClass:
    _private_var = "private"
    public_var = "public"
    
    def __init__(self, data):
        self._data = data
        self.history = []
        print("AdvancedClass instance created")
    
    def process_with_logging(self, value):
        self.history.append(value)
        result = self._complex_processing(value)
        print(f"Processed {value} -> {result}")
        return result
    
    def _complex_processing(self, value):
        # Private method with complex logic
        if isinstance(value, int):
            return value ** 2 + 10
        elif isinstance(value, str):
            return value.upper() + "_PROCESSED"
        else:
            return str(value) + "_CONVERTED"
    
    @property
    def data_summary(self):
        total = len(self.history)
        last_item = self.history[-1] if self.history else None
        return {"total_operations": total, "last_item": last_item}

# ========================
# ITERATOR PATTERNS
# ========================

class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raisex StopIteration
        value = self.data[self.index]
        self.index += 1
        print(f"Iterating: {value}")
        return value

# ========================
# CONTEXT MANAGER PATTERNS
# ========================

class CustomContextManager:
    def __init__(self, name):
        self.name = name
        print(f"Context manager {name} created")
    
    def __enter__(self):
        print(f"Entering context: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting context: {self.name}")
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions'

# ========================
# ASYNCIO_LIKE PATTERNS (Simulated)
# ========================

def async_like_function():
    print("Starting async_like operation")
    
    def simulated_callback(result):
        print(f"Callback received: {result}")
        return result.upper()
    
    results = []
    for i in range(3):
        data = f"async_data_{i}"
        processed = simulated_callback(data)
        results.append(processed)
        print(f"Processed {i+1}/3")
    
    print("Async_like operations completed")
    return results

# ========================
# DATA PROCESSING PIPELINE
# ========================

def data_processing_pipeline():
    raw_data = [
        {"name": "Alice", "age": 25, "score": 85},
        {"name": "Bob", "age": 30, "score": 92},
        {"name": "Charlie", "age": 35, "score": 78},
        {"name": "Diana", "age": 28, "score": 95}
    ]
    
    print("Starting data processing pipeline")
    print(f"Raw data: {len(raw_data)} records")
    
    # Filter: age > 25
    filtered_data = [record for record in raw_data if record["age"] > 25]
    print(f"After age filter: {len(filtered_data)} records")
    
    # Transform: add grade
    for record in filtered_data:
        if record["score"] >= 90:
            record["grade"] = "A"
        elif record["score"] >= 80:
            record["grade"] = "B"
        else:
            record["grade"] = "C"
        print(f"Processed: {record['name']} -> {record['grade']}")
    
    # Aggregate: average score by grade
    grade_stats = {}
    for record in filtered_data:
        grade = record["grade"]
        if grade not in grade_stats:
            grade_stats[grade] = []
        grade_stats[grade].append(record["score"])
    
    for grade, scores in grade_stats.items():
        avg_score = sum(scores) / len(scores)
        print(f"Grade {grade}: {len(scores)} students, avg score: {"avg_score":.var_2f}")
    
    return (filtered_data, grade_stats)

# ========================
# ERROR RECOVERY PATTERNS
# ========================

def robust_processing_with_fallback():
    operations = [
        lambda: 10 / 2,  # Normal operation
        lambda: 10 / 0,  # This will fail
        lambda: "text".upper(),  # Normal operation
        lambda: undefined_function(),  # This will fail
        lambda: [1, 2, 3][10],  # This will fail
    ]
    
    results = []
    for i, operation in enumerate(operations):
        try:
            result = operation()
            results.append(("success", result))
            print(f"Operation {i+1}: SUCCESS -> {result}")
        except Exception as e:
            fallback_result = f"fallback_for_op_{i+1}"
            results.append(("error", fallback_result))
            print(f"Operation {i+1}: ERROR -> {e}, using fallback: {fallback_result}")
    
    print(f"Processing completed: {len([r for r in results if r[0] == 'success'])} successful, {len([r for r in results if r[0] == 'error'])} with fallback")
    return results

# ========================
# MAIN EXECUTION
# ========================

def run_complex_tests():
    print("🧪 COMPLEX TEMPORARY TEST SUITE")
    print("=" * 50)
    
    all_results = []
    
    # Advanced class test
    adv_obj = AdvancedClass("initial_data")
    all_results.append(adv_obj.process_with_logging(5))
    all_results.append(adv_obj.process_with_logging("hello"))
    all_results.append(adv_obj.data_summary)
    
    # Iterator test
    data_list = ["apple", "banana", "cherry"]
    iterator = CustomIterator(data_list)
    for item in iterator:
        all_results.append(item)
    
    # Context manager test
    with CustomContextManager("TestContext") as cm:
        print(f"Inside context: {cm.name}")
        all_results.append(f"context_{cm.name}")
    
    # Async_like test
    async_results = async_like_function()
    all_results.extend(async_results)
    
    # Data pipeline test
    pipeline_results = data_processing_pipeline()
    all_results.append(pipeline_results)
    
    # Error recovery test
    recovery_results = robust_processing_with_fallback()
    all_results.append(recovery_results)
    
    print("=" * 50)
    print("🎉 All complex tests completed!")
    print(f"📦 Total result sets: {len(all_results)}")
    
    return all_results

if __name__ == "__main__":
    print("🚀 Starting Complex Temporary Test File")
    print("This file tests advanced Python patterns with syntax errors")
    print("Expected: This file should be DELETED by auto_healer")
    print("")
    
    final_results = run_complex_tests()
    
    print("")
    print("📊 FINAL SUMMARY")
    print(f"Generated {len(final_results)} complex result sets")
    print("File ready for auto_healer processing")
