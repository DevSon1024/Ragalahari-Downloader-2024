import os
import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from urllib.parse import quote


def fetch_image_urls(base_url, num_pages):
    image_urls = []

    # Extract the base number (e.g., 3811) using regex
    match = re.search(r"(\d+)/", base_url)
    if not match:
        print("No number found in the URL structure to increment!")
        return []
    base_number = match.group(1)  # Extract the number (e.g., 3811)

    for i in range(num_pages):
        # Handle the URL structure
        if i == 0:
            page_url = base_url  # First page URL (no increment)
        else:
            # Replace the base number with "base_number/{i}/"
            page_url = re.sub(rf"{base_number}/", f"{base_number}/{i}/", base_url)
        
        print(f"Fetching: {page_url}")
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract image URLs from <img> tags with src starting with "https://starzone.ragalahari.com/"
            for img_tag in soup.find_all("img"):
                img_src = img_tag.get("src")
                if img_src and img_src.startswith("https://starzone.ragalahari.com/"):
                    img_src = re.sub(r't(?=\.jpg)', '', img_src)  # Clean URL (optional)
                    image_urls.append(img_src)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {page_url}: {e}")
            continue

    return image_urls


def download_image(url, folder):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        encoded_url = quote(url, safe=':/')
        response = requests.get(encoded_url, headers=headers, timeout=15)
        response.raise_for_status()
        filename = os.path.join(folder, url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        return f"Downloaded: {filename}"
    except requests.exceptions.Timeout:
        return f"Timeout error: {url}"
    except requests.exceptions.HTTPError as e:
        return f"HTTP error {e.response.status_code}: {url}"
    except requests.exceptions.RequestException as e:
        return f"Error downloading {url}: {str(e)}"


def main():
    # Input for the base URL and number of pages
    base_url = input("Enter the base URL for the first page: ")
    num_pages = int(input("Enter the number of pages to scrape: "))
    
    # Fetch image URLs
    all_image_urls = fetch_image_urls(base_url, num_pages)
    if not all_image_urls:
        print("No matching images found. Exiting.")
        return

    print(f"Found {len(all_image_urls)} images from starzone.ragalahari.com across {num_pages} pages.")

    # Create download folder
    folder_choice = input("Enter the folder name to save images or press Enter to create a new folder: ")
    if not folder_choice:
        folder_choice = 'downloaded_images'
    folder_path = os.path.join(os.getcwd(), folder_choice)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created new folder: {folder_path}")

    # Download images
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_image, url, folder_path) for url in all_image_urls]
        
        with tqdm(total=len(all_image_urls), desc="Downloading", unit="image") as pbar:
            for future in as_completed(futures):
                result = future.result()
                if "Downloaded:" in result:
                    pbar.update(1)
                else:
                    pbar.write(result)

    print(f"\nDownload complete. Images saved in {folder_path}")


if __name__ == "__main__":
    main()