import time
# Compatibility fix: time.clock was removed in Python 3.8+
if not hasattr(time, 'clock'):
    time.clock = time.perf_counter

from app import app

if __name__ == "__main__":
    app.run()

