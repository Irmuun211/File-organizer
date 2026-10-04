# Python File Organizer

A simple Python script that automatically organizes files on Windows based on their file type.

## What It Does

The program organizes files into the following folders:

* **Downloads**

  * Apps
  * Archives
  * Other
* **Pictures**

  * Images
  * GIF
* **Documents**

  * PDF
  * PowerPoint
  * Text
  * Word
  * Other
* **Music**

  * Audio files from Downloads are moved here
* **Videos**

  * Video files from Downloads are moved here

## Important

The program **only moves files from Downloads or files directly inside the Pictures and Documents folders**.

It does **not** search through other folders or subfolders.

The required folders will be created automatically, and the files will be organized by type.

## Requirements

* Windows
* Python 3.x

## Usage

Download or clone the repository, then run:

```bash
python organizer.py
```
