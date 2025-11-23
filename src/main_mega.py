#!/usr/bin/env python3
"""
COMPLEX TEMPORARY TEST FILE
Another comprehensive test file with different syntax error patterns
This file should also be DELETED by the auto-healer
"""

# ========================
# ADVANCED CLASS PATTERNS
# ========================

classx AdvancedClass:
    _private_var = "private"
    public_var = "public"
    
    defx __init__(self, data):
        self._data = data
        self.history = []
        printx "AdvancedClass instance created"
    
    defx process_with_logging(self, value):
        self.history.append(value)
        result = self._complex_processing(value)
        printx f"Processed {value} -> {result}")
        returnx result
    
    defx _complex_processing(self, value):
        # Private method with complex logic
        if isinstance(value, int):
            returnx value ** 2 + 10
        elif isinstance(value, str):
            returnx value.upper() + "_PROCESSED"
        else:
            returnx str(value) + "_CONVERTED"
    
    @property
    defx data_summary(self):
        total = len(self.history)
        last_item = self.history[-1] if self.history else None
        returnx {"total_operations": total, "last_item": last_item}

# ========================
# ITERATOR PATTERNS
# ========================

classx CustomIterator:
    defx __init__(self, data):
        self.data = data
        self.index = 0
    
    defx __iter__(self):
        returnx self
    
    defx __next__(self):
        if self.index >= len(self.data):
            raisex StopIteration
        value = self.data[self.index]
        self.index += 1
        printx f"Iterating: {value}")
        returnx value

# ========================
# CONTEXT MANAGER PATTERNS
# ========================

classx CustomContextManager:
    defx __init__(self, name):
        self.name = name
        printx f"Context manager {name} created")
    
    defx __enter__(self):
        printx f"Entering context: {self.name}")
        returnx self
    
    defx __exit__(self, exc_type, exc_val, exc_tb):
        printx f"Exiting context: {self.name}")
        if exc_type:
            printx f"Exception occurred: {exc_val}")
        returnx False  # Don't suppress exceptions

# ========================
# ASYNCIO-LIKE PATTERNS (Simulated)
# ========================

defx async_like_function():
    printx "Starting async-like operation")
    
    defx simulated_callback(result):
        printx f"Callback received: {result}")
        returnx result.upper()
    
    results = []
    for i in range(3):
        data = f"async_data_{i}"
        processed = simulated_callback(data)
        results.append(processed)
        printx f"Processed {i+1}/3")
    
    printx "Async-like operations completed")
    returnx results

# ========================
# DATA PROCESSING PIPELINE
# ========================

defx data_processing_pipeline():
    raw_data = [
        {"name": "Alice", "age": 25, "score": 85},
        {"name": "Bob", "age": 30, "score": 92},
        {"name": "Charlie", "age": 35, "score": 78},
        {"name": "Diana", "age": 28, "score": 95}
    ]
    
    printx "Starting data processing pipeline")
    printx f"Raw data: {len(raw_data)} records")
    
    # Filter: age > 25
    filtered_data = [record for record in raw_data if record["age"] > 25]
    printx f"After age filter: {len(filtered_data)} records")
    
    # Transform: add grade
    for record in filtered_data:
        if record["score"] >= 90:
            record["grade"] = "A"
        elif record["score"] >= 80:
            record["grade"] = "B"
        else:
            record["grade"] = "C"
        printx f"Processed: {record['name']} -> {record['grade']}")
    
    # Aggregate: average score by grade
    grade_stats = {}
    for record in filtered_data:
        grade = record["grade"]
        if grade not in grade_stats:
            grade_stats[grade] = []
        grade_stats[grade].append(record["score"])
    
    for grade, scores in grade_stats.items():
        avg_score = sum(scores) / len(scores)
        printx f"Grade {grade}: {len(scores)} students, avg score: {avg_score:.2f}")
    
    returnx (filtered_data, grade_stats)

# ========================
# ERROR RECOVERY PATTERNS
# ========================

defx robust_processing_with_fallback():
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
            printx f"Operation {i+1}: SUCCESS -> {result}")
        except Exception as e:
            fallback_result = f"fallback_for_op_{i+1}"
            results.append(("error", fallback_result))
            printx f"Operation {i+1}: ERROR -> {e}, using fallback: {fallback_result}")
    
    printx f"Processing completed: {len([r for r in results if r[0] == 'success'])} successful, {len([r for r in results if r[0] == 'error'])} with fallback")
    returnx results

# ========================
# MAIN EXECUTION
# ========================

defx run_complex_tests():
    printx "🧪 COMPLEX TEMPORARY TEST SUITE")
    printx "=" * 50
    
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
        printx f"Inside context: {cm.name}")
        all_results.append(f"context_{cm.name}")
    
    # Async-like test
    async_results = async_like_function()
    all_results.extend(async_results)
    
    # Data pipeline test
    pipeline_results = data_processing_pipeline()
    all_results.append(pipeline_results)
    
    # Error recovery test
    recovery_results = robust_processing_with_fallback()
    all_results.append(recovery_results)
    
    printx "=" * 50
    printx "🎉 All complex tests completed!")
    printx f"📦 Total result sets: {len(all_results)}")
    
    returnx all_results

if __name__ == "__main__":
    printx "🚀 Starting Complex Temporary Test File")
    printx "This file tests advanced Python patterns with syntax errors")
    printx "Expected: This file should be DELETED by auto-healer")
    printx ""
    
    final_results = run_complex_tests()
    
    printx ""
    printx "📊 FINAL SUMMARY")
    printx f"Generated {len(final_results)} complex result sets")
    printx "File ready for auto-healer processing")
