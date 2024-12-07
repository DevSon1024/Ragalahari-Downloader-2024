#Added support for 
#https://media.ragalahari.com/: Updated fetch_image_urls to include URLs starting with https://media.ragalahari.com/ in addition to https://starzone.ragalahari.com/.

import os
import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn, TextColumn
from urllib.parse import quote
from time import perf_counter

console = Console()

class RagaDownloader:
    def __init__(self):
        self.base_url = ""
        self.num_pages = 0
        self.folder_path = ""
        self.download_root = os.path.join(os.getcwd(), "Ragalahari Downloads")

        # Ensure the root folder exists
        if not os.path.exists(self.download_root):
            os.makedirs(self.download_root)
            console.print(f"[bold green]Created root folder:[/bold green] {self.download_root}")

    def get_user_input(self):
        console.print("[bold yellow]Enter the base URL for the first page:[/bold yellow]")
        self.base_url = input("> ").strip()

        # Extract the directory number from the base URL
        match = re.search(r"/(\d+)/", self.base_url)
        if not match:
            console.print("[bold red]Invalid URL! Could not extract directory number.[/bold red]")
            exit()
        self.directory_number = match.group(1)

        console.print("[bold yellow]Enter the number of pages to scrape:[/bold yellow]")
        try:
            self.num_pages = int(input("> "))
        except ValueError:
            console.print("[bold red]Invalid input. Please enter a valid number of pages![/bold red]")
            exit()

    def fetch_image_urls(self):
        image_urls = []

        console.print("\n[bold cyan]Processing...[/bold cyan]\n", style="bold cyan")
        base_number = self.directory_number

        with Progress(SpinnerColumn(), "[progress.description]{task.description}", TimeElapsedColumn()) as progress:
            task = progress.add_task("[cyan]Fetching image URLs...", total=self.num_pages)
            for i in range(self.num_pages):
                if i == 0:
                    page_url = self.base_url
                else:
                    page_url = re.sub(rf"{base_number}/", f"{base_number}/{i}/", self.base_url)

                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                    }
                    response = requests.get(page_url, headers=headers)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, "html.parser")

                    for img_tag in soup.find_all("img"):
                        img_src = img_tag.get("src")
                        if img_src:
                            # Check if the image URL matches the required patterns
                            if img_src.startswith("https://starzone.ragalahari.com/") or img_src.startswith("https://media.ragalahari.com/"):
                                img_src = re.sub(r't(?=\.jpg)', '', img_src)
                                image_urls.append(img_src)

                except requests.exceptions.RequestException as e:
                    console.print(f"[bold red]Failed to fetch {page_url}: {e}[/bold red]")
                finally:
                    progress.update(task, advance=1)

        return image_urls

    def download_images(self, image_urls):
        console.print("\n[bold green]Starting download process...[/bold green]")
        if not self.folder_path:
            console.print("[bold yellow]Enter a folder name (e.g., Rashmika):[/bold yellow]")
            folder_name = input("> ").strip()

            # Combine directory number with the folder name and place it under the root folder
            self.folder_path = os.path.join(self.download_root, f"{self.directory_number}-{folder_name}")

            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
                console.print(f"[bold green]Created folder:[/bold green] {self.folder_path}")

        total_files = len(image_urls)
        console.print(f"[bold blue]Total images to download: {total_files}[/bold blue]")

        with Progress(
            SpinnerColumn(), 
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("{task.completed}/{task.total}"),
            TimeElapsedColumn()
        ) as progress:
            task = progress.add_task("[cyan]Downloading images...", total=total_files)

            with ThreadPoolExecutor(max_workers=5) as executor:
                start_time = perf_counter()
                futures = {executor.submit(self.download_image, url): url for url in image_urls}
                
                for future in as_completed(futures):
                    result = future.result()
                    if "Downloaded:" in result:
                        progress.update(task, advance=1)
                    else:
                        console.print(result, style="bold red")

                end_time = perf_counter()
                total_time = end_time - start_time
                console.print(f"\n[bold green]Download complete in {total_time:.2f} seconds![/bold green]")

    def download_image(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            encoded_url = quote(url, safe=':/')
            response = requests.get(encoded_url, headers=headers, timeout=15)
            response.raise_for_status()
            filename = os.path.join(self.folder_path, url.split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(response.content)
            return f"Downloaded: {filename}"
        except requests.exceptions.Timeout:
            return f"Timeout error: {url}"
        except requests.exceptions.HTTPError as e:
            return f"HTTP error {e.response.status_code}: {url}"
        except requests.exceptions.RequestException as e:
            return f"Error downloading {url}: {str(e)}"

    def run(self):
        self.get_user_input()
        image_urls = self.fetch_image_urls()
        if not image_urls:
            console.print("[bold red]No matching images found. Exiting.[/bold red]")
            return

        console.print(f"[bold green]Found {len(image_urls)} images from Ragalahari across {self.num_pages} pages.[/bold green]")
        self.download_images(image_urls)
        console.print(f"\n[bold green]All images saved in: {self.folder_path}[/bold green]")

if __name__ == "__main__":
    downloader = RagaDownloader()
    downloader.run()