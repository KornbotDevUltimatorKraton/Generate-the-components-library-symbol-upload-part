import requests

# Define the endpoint URL
url = "http://192.168.50.4:8900/uploadfile/"

# Specify the file to upload
file_path = "/home/kornbotdev/AA51880.PDF" #package_pdf/TB6612FNG.pdf"  # Replace with the actual file path

# Open the file in binary mode and prepare the file dictionary
with open(file_path, "rb") as f:
    files = {"file": (file_path.split("/")[-1], f)}

    # Send the POST request with the file
    response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)
