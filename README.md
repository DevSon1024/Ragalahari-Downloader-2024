
# Ragalahari-Downloader 🖼️

**Ragalahari-Downloader** is a Python-based program to scrape and download images from a series of pages on a ragalahari website. It specifically targets image URLs that match a specific pattern and downloads them into a local folder. The program supports multithreading for efficient downloading and provides a user-friendly interface with progress tracking. it is build in 'Python 3.12.5' still I can be run python 3.7 or Higher.

---

## Features 🚀
- **Scrapes Images**: Automatically fetches image URLs from multiple pages based on user input.
- **Targeted Download**: Only downloads images with specific URL patterns.
- **Progress Tracking**: Displays a progress bar with file counts and elapsed time.
- **Multithreaded Downloads**: Uses multiple threads for faster downloading.
- **Custom Folder**: Allows saving files in a user-specified folder.

---

## Prerequisites 🛠️
Make sure you have the following installed:
- **Python 3.7 or higher**
- Required Python libraries:
  - `requests`
  - `bs4` (BeautifulSoup)
  - `concurrent.futures`
  - `rich`

You can install the required libraries using:
```bash
pip install requests beautifulsoup4 rich
```

---

## Usage 👩‍💻

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Dev9078/Ragalahari-Downloader-2024.git
   ```

2. Run the script:
   ```bash
   python Downloader v4.3.py
   ```

3. Follow the prompts:
   - Enter the **base URL** of the page you want to Download from `Ragalahari.com`.
   - Enter the **number of pages** to scrape for images.
   - Specify a folder name (or leave blank for default `downloaded_images`).

4. The program will:
   - Display the number of images to download.
   - Show a progress bar as images are being downloaded.
   - Save all images into the specified folder.

---

## Example Input & Output 📥📤

### Example Input:
- **Base URL**: `https://m.ragalahari.com/actress/3811/leader-heroine-richa-gangopadhyay-photo-session-by-ragalaharicom.aspx`
- **Number of Pages**: `3`

### Output:
- Total images to download: `10`
- Folder: `downloaded_images/`

**Downloaded Images**:
- `https://starzone.ragalahari.com/image1.jpg`
- `https://starzone.ragalahari.com/image2.jpg`
- ...

---

## File Structure 📂

```
ImgDownloader/
├── img_downloader.py    # Main Python script
├── README.md            # Documentation
├── requrements.txt      # for installing required version
```

---

## Features to Add (Optional) 📋
- Support for other file types (e.g., `.png`, `.webp`).
- Retry logic for failed downloads.
- GUI support for non-technical users.

---

## License 📜
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

## Contributing 🙌
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

---

## Contact 📧
For any queries, feel free to reach out:
- **Email**: [Mail me](mailto:dpsonawane789@gmail.com)
- **GitHub**: [Devson](https://github.com/Dev9078)

