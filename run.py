import os
import subprocess

def main():

    os.chdir("backend")
    subprocess.run(["python", "scraper.py"])
    flask_process = subprocess.Popen(["python", "app.py"])
    os.chdir("..")
    os.chdir("frontend")
    print("Press Ctrl+C to stop all servers")
    try:
        subprocess.run(["npm", "run", "serve"])
    except KeyboardInterrupt:
        pass
    finally:
        print("Shutting down Flask server...")
        flask_process.terminate()
        flask_process.wait()

if __name__ == "__main__":
    main()