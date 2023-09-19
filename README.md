# Paper to Audiopaper 📝🔊

Welcome to the Paper to Audiopaper project! This project aims to convert scientific PDF papers into audio format using a combination of PDF extraction, LaTeX formula translation, and text-to-speech technologies. 

:warning: **Please note that this is a work in progress and may not work perfectly for all papers.** 

The primary script used for this process is `paper_to_audiopaper_colab.ipynb`, which provides a series of functions to handle the paper conversion process.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/engelberger/p2s/blob/main/paper_to_audiopaper_colab.ipynb)

## Features

- PDF Extraction: Converts a PDF file or an arXiv paper into a markdown file. 📄
- LaTeX Translation: Translates LaTeX formulas into plain English. 📝➡️🗣️
- Text-to-Speech: Converts the processed text into speech in WAV format. 🗣️➡️🔊

## Future Work (TODO)

- [ ] Support for local inference with [ctransformers](https://github.com/marella/ctransformers) Llama2.
- [ ] Add support to other TTS options like [Coqui TTS](https://github.com/coqui-ai/TTS).
- [ ] Improve the user experience in the Colab notebook (better markdown interface).
- [ ] Save to google drive

## Functions
Here is a brief explanation of the main functions used in the script:

### `pdf_to_markdown()`

This function converts a PDF file or an arXiv paper to a markdown file. The resulting markdown file is saved in a specified output directory.

```python
pdf_to_markdown(input: Union[str, bool], output_dir: str = "outputs", is_arxiv_id: bool = False, nougat_path: str = "/home/iwe30/anaconda3/envs/nougat/bin")
```

### `translate()`

This function uses the OpenAI API to translate a given LaTeX formula into plain English. It employs a backoff strategy to manage API request retries.

```python
translate(latex_formula)
```

### `latex_to_english()`

This function takes a list of LaTeX formulas and translates them to plain English using the OpenAI API. It leverages multithreading for efficient processing.

```python
latex_to_english(latex_formulas, debug=False)
```

### `process_markdown_file()`

This function processes a markdown file, translating LaTeX formulas to plain English. The processed file is saved with a `_processed` tag appended to the original filename.

```python
process_markdown_file(file_path, dry_run=False, debug=False, tag="_processed")
```

### `markdown_to_wav()`

This function converts a processed markdown file into speech in WAV format. The resulting audio file is saved to a specified output path.

```python
markdown_to_wav(file_path, output_path='output.wav')
```

### `pdf_to_speech()`

This is the main function that orchestrates the conversion process from PDF (or an ArXiv ID) to speech. It calls the other functions in the necessary order to perform the conversion.

```python
pdf_to_speech(pdf_input, output_dir="outputs", is_arxiv_id=False, dry_run=False, debug=False, wav_output_path='output.wav')
```

## Usage

To use the script, simply call the `pdf_to_speech()` function with your desired PDF file or ArXiv ID.

```python
pdf_to_speech("2309.07124", is_arxiv_id=True)
```

This will download the paper from arXiv, convert it to markdown, translate the LaTeX formulas, and finally convert the text to speech.

We hope you find this script useful for your research and study needs. Enjoy listening to your papers! 🎧📚
