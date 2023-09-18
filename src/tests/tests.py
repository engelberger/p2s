import os
import unittest


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.arxiv_id = "2105.04877"
        self.pdf_path = "test.pdf"
        self.output_dir = "test_outputs"
        self.markdown_path = f"{self.output_dir}/{self.arxiv_id}/{self.arxiv_id}.mmd"
        self.processed_md_path = (
            f"{self.output_dir}/{self.arxiv_id}/{self.arxiv_id}_processed.mmd"
        )
        self.wav_path = f"{self.output_dir}/{self.arxiv_id}/{self.arxiv_id}.wav"

    def test_pdf_to_markdown(self):
        pdf_to_markdown(self.arxiv_id, output_dir=self.output_dir, is_arxiv_id=True)
        self.assertTrue(os.path.exists(self.markdown_path))

    def test_latex_to_english(self):
        test_formulas = ["x^2", "\\frac{a}{b}", "\\sqrt{a}"]
        translations = latex_to_english(test_formulas)
        self.assertEqual(len(translations), len(test_formulas))

    def test_process_markdown_file(self):
        process_markdown_file(self.markdown_path)
        self.assertTrue(os.path.exists(self.processed_md_path))

    def test_markdown_to_wav(self):
        markdown_to_wav(self.processed_md_path, output_path=self.wav_path)
        self.assertTrue(os.path.exists(self.wav_path))

    def test_pdf_to_speech(self):
        pdf_to_speech(self.arxiv_id, output_dir=self.output_dir, is_arxiv_id=True)
        self.assertTrue(os.path.exists(self.wav_path))


if __name__ == "__main__":
    unittest.main()
