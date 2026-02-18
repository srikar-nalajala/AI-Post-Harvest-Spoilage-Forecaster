import subprocess
import sys
import time
import os

# Force UTF-8 encoding for stdout/stderr to handle emojis on Windows
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def run_test(script_name):
    print(f"\n{'='*20} Running {script_name} {'='*20}")
    start_time = time.time()
    try:
        # Run with utf-8 encoding environment variable
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        
        result = subprocess.run(
            [sys.executable, script_name], 
            capture_output=True, 
            text=True, 
            check=True,
            encoding='utf-8',
            env=env
        )
        print(result.stdout)
        print(f"✅ {script_name} PASSED ({time.time() - start_time:.2f}s)")
        return True
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        print(f"❌ {script_name} FAILED")
        return False
    except Exception as e:
        print(f"❌ Error running {script_name}: {e}")
        return False

def main():
    scripts = [
        "check_models.py", 
        "test_backend.py", 
        "test_translations.py", 
        "test_vision.py"
    ]
    
    passed = 0
    total = len(scripts)
    
    print("🚀 Starting Complete Test Suite for AgriThon...")
    
    for script in scripts:
        if run_test(script):
            passed += 1
            
    print("\n" + "="*50)
    print(f"Test Summary: {passed}/{total} Passed")
    print("="*50)
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! System is ready.")
        sys.exit(0)
    else:
        print("⚠️ SOME TESTS FAILED. Check output above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
