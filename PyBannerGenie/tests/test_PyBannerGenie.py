#test_PyBannerGenie

#imports
import unittest
import os
import sys
from unittest.mock import patch
from io import StringIO
from PyBannerGenie import * 
from PyBannerGenie import(
    display_square_basic_banner,
    display_square_fancy_banner,
    display_square_colored_banner,
    save_banner_to_file,
    save_banner_as_image,
    COLORS,
    FONTS,
    OUTPUT_DIR,
    parse_arguments,
    get_user_choice,
    get_user_text,
    main
)

class TestPyBannerGenie(unittest.TestCase):
    """Comprehensive unit tests for PyBannerGenie functionalities."""

    def setUp(self):
        """Set up test environment."""
        self.test_text = "Test Banner"
        self.test_color = COLORS["blue"]
        self.test_font = "standard"
        self.test_filename = "test_banner"
        self.output_dir = OUTPUT_DIR

        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        """Clean up after tests."""
        # Remove test files created during testing
        txt_file = os.path.join(self.output_dir, f"{self.test_filename}.txt")
        png_file = os.path.join(self.output_dir, f"{self.test_filename}.png")
        
        if os.path.exists(txt_file):
            os.remove(txt_file)
        
        if os.path.exists(png_file):
            os.remove(png_file)

    def test_display_square_basic_banner(self):
        """Test basic square banner generation."""
        banner_text = display_square_basic_banner(self.test_text, self.test_color)
        self.assertTrue(banner_text.startswith(self.test_color), "Banner color not applied correctly.")
        self.assertIn(self.test_text, banner_text, "Banner text not displayed correctly.")

    def test_display_square_fancy_banner(self):
        """Test fancy ASCII-art banner generation."""
        banner_text = display_square_fancy_banner(self.test_text, self.test_color, font=self.test_font)
        self.assertIsNotNone(banner_text, "Fancy banner generation failed.")
        self.assertIn(self.test_text, banner_text, "Banner text not displayed correctly.")

    def test_display_square_colored_banner(self):
        """Test colorful square framed banner generation."""
        banner_text = display_square_colored_banner(self.test_text, self.test_color)
        self.assertTrue(banner_text.startswith(self.test_color), "Banner color not applied correctly.")
        self.assertIn(self.test_text, banner_text, "Banner text not displayed correctly.")

    def test_save_banner_to_file(self):
        """Test saving banner to a text file."""
        banner_text = display_square_basic_banner(self.test_text, self.test_color)
        save_banner_to_file(banner_text)
        
        txt_file_path = os.path.join(self.output_dir, f"{self.test_filename}.txt")
        
        self.assertTrue(os.path.exists(txt_file_path), "Text file was not created.")
        
        with open(txt_file_path, "r", encoding="utf-8") as file:
            saved_content = file.read()
        
        self.assertEqual(saved_content.strip(), banner_text.strip(), "Saved content does not match the generated banner.")

    def test_save_banner_as_image(self):
        """Test saving banner as an image file."""
        banner_text = display_square_basic_banner(self.test_text, self.test_color)
        save_banner_as_image(banner_text)
        
        png_file_path = os.path.join(self.output_dir, f"{self.test_filename}.png")
        
        self.assertTrue(os.path.exists(png_file_path), "Image file was not created.")

    def test_invalid_color_choice(self):
        """Test handling invalid color choices."""
        with self.assertRaises(KeyError):
            _ = COLORS["invalid_color"]

    def test_invalid_font_choice(self):
        """Test handling invalid font choices."""
        with self.assertRaises(Exception):
            _ = display_square_fancy_banner(self.test_text, self.test_color, font="invalid_font")

    def test_output_directory_creation(self):
        """Test that output directory is created if it doesn't exist."""
        if os.path.exists(OUTPUT_DIR):
            os.rmdir(OUTPUT_DIR)  # Remove directory to simulate non-existence
        
        # Trigger a save operation to recreate the directory
        save_banner_to_file("Sample Banner")
        
        # Check if directory exists again
        self.assertTrue(os.path.exists(OUTPUT_DIR), "Output directory was not recreated.")

    def test_parse_arguments(self):
        """Test command-line argument parsing."""
        with patch('sys.argv', ['PyBannerGenie.py', '--text', 'Hello', '--color', 'blue', '--type', '1', '--output', 'hello']):
            args = parse_arguments()
            self.assertEqual(args.text, 'Hello')
            self.assertEqual(args.color, 'blue')
            self.assertEqual(args.type, 1)
            self.assertEqual(args.output, 'hello')

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice(self, mock_input):
        """Test getting user choice from menu."""
        choice = get_user_choice()
        self.assertEqual(choice, '1')

    @patch('builtins.input', side_effect=['Test Text'])
    def test_get_user_text(self, mock_input):
        """Test getting user text input."""
        text = get_user_text()
        self.assertEqual(text, 'Test Text')

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4', 'y'])
    def test_main_interactive_exit(self, mock_input, mock_stdout):
        """Test exiting interactive mode."""
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Test Banner', 'blue', 'test_banner', 'n', 'n'])

    def test_main_interactive_mode(self, mock_input, mock_stdout):
        """Test main function in interactive mode."""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Test Banner", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_command_line_mode(self, mock_stdout):
        """Test main function in command-line mode."""
        with patch('sys.argv', ['PyBannerGenie.py', '--text', 'Hello', '--color', 'blue', '--type', '1']):
            main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Hello", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_invalid_color(self, mock_stdout):
        """Test main function with invalid color in command-line mode."""
        with patch('sys.argv', ['PyBannerGenie.py', '--text', 'Hello', '--color', 'invalid_color', '--type', '1']):
            with self.assertRaises(SystemExit) as context:
                main()
            self.assertEqual(context.exception.code, 1)
        output = mock_stdout.getvalue().strip()
        self.assertIn("Error: Invalid color", output)

if __name__ == "__main__":
    unittest.main()
    