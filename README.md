
# Ragalahari-Downloader 🖼️

**Ragalahari-Downloader** is a Python-based program to scrape and download images from a series of pages on a ragalahari website. It specifically targets image URLs that match a specific pattern and downloads them into a local folder. The program supports multithreading for efficient downloading and provides a user-friendly interface with progress tracking. it is build in 'Python 3.12.5' still It can be run in python 3.7 or Higher.

---

## Features 🚀
- **Multi-Page Scraping**: Download images from multiple pages in one run.  
- **Custom Directory Names**: Save downloaded images in directories with custom names, prefixed by their source directory number.
- **Efficient Downloading**: Uses multithreading for faster image downloads.  
-- **User-Friendly Interface**: Progress bars and feedback are displayed using the `rich` library. 
- **Error Handling**: Handles timeouts and HTTP errors gracefully, providing clear messages.  

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
   cd Ragalahari-Downloader-2024
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python Ragalahari_Downloader_v4.4.py
   ```

3. Follow the prompts:
   - Enter the **base URL** of the page you want to Download from `Ragalahari.com`.
   - Enter the **number of pages** to scrape for images.
   - Custom folder name for saving the images.(e.g.: Richa)

4. The program will:
   - Display the number of images to download.
   - Show a progress bar as images are being downloaded.
   - Save all images into the specified folder.

---

## Example Input & Output 📥📤

### Example Input:
- **Base URL**: `https://m.ragalahari.com/actress/3811/leader-heroine-richa-gangopadhyay-photo-session-by-ragalaharicom.aspx`
- **Number of Pages**: `3` (or above minimum `1`)
- 
- **Custom folder name**: `Richa`
### Output:
```
|-- Ragalahari Downloads/
    |-- 3811-Richa/
        |-- image1.jpg
        |-- image2.jpg
        ...
```

---

## File Structure 📂

When running the script, the following folder structure is created:

```
Ragalahari Downloader/
│
├── Ragalahari Downloads/
│   ├── 123-Tamannah/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── ...
├── ragalahari_downloader.py
├── README.md
└── requirements.txt
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
- **Name**: Devendra Sonawane
- **Email**: [Mail me](mailto:dpsonawane789@gmail.com)
- **GitHub**: [Devson](https://github.com/Dev9078)

