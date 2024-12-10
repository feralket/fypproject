import subprocess
import time

def run_tcpdump(output_dir):
    timestamp = int(time.time())
    output_name = "{}/{}.pcap".format(output_dir, timestamp)

    # Run tcpdump command
    command = ["tcpdump", "-i", "wlan0", "dst", "port", "5500", "-c", "150", "-w", output_name]
    subprocess.run(command)

def main():
    output_dir = "/home/pi/Desktop/test/"
    repetitions = 10
    
    for _ in range(repetitions):
        run_tcpdump(output_dir)
        time.sleep(2)  # Wait for 2 seconds before the next iteration

if __name__ == "__main__":
    main()

