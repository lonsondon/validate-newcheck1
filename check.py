"""Find and replace repeated words in a text file."""

from collections import Counter
from pathlib import Path
import re
from typing import Mapping


WORD_PATTERN = re.compile(r"\b[\w']+\b", re.IGNORECASE)


def read_file(file_path: str | Path) -> str:
	"""Read and return the contents of a text file."""
	return Path(file_path).read_text(encoding="utf-8")


def find_repeated_words(text: str) -> dict[str, int]:
	"""Return repeated words and their counts, ignoring letter case."""
	words = [word.lower() for word in WORD_PATTERN.findall(text)]
	counts = Counter(words)
	return {word: count for word, count in counts.items() if count > 1}


def find_repeated_words_in_file(file_path: str | Path) -> dict[str, int]:
	"""Read a file and return its repeated words and counts."""
	return find_repeated_words(read_file(file_path))


def print_word_counts(word_counts: Mapping[str, int]) -> None:
	"""Print repeated words and their counts in alphabetical order."""
	if not word_counts:
		print("No repeated words found.")
		return

	for word, count in sorted(word_counts.items()):
		print(f"{word}: {count}")


def replace_repeated_words(
	text: str, replacements: Mapping[str, str]
) -> str:
	"""Replace matching words using a case-insensitive replacement mapping."""
	replacement_lookup = {word.lower(): replacement for word, replacement in replacements.items()}

	def replace_match(match: re.Match[str]) -> str:
		word = match.group(0)
		return replacement_lookup.get(word.lower(), word)

	return WORD_PATTERN.sub(replace_match, text)


def replace_words_in_file(
	file_path: str | Path,
	replacements: Mapping[str, str],
	output_path: str | Path | None = None,
) -> Path:
	"""Replace words in a file and write the result to an output file."""
	source_path = Path(file_path)
	destination_path = source_path if output_path is None else Path(output_path)
	updated_text = replace_repeated_words(read_file(source_path), replacements)
	destination_path.write_text(updated_text, encoding="utf-8")
	return destination_path


def main() -> None:
	"""Print repeated words from the file supplied on the command line."""
	import argparse

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("file", type=Path, help="text file to inspect")
	args = parser.parse_args()
	print_word_counts(find_repeated_words_in_file(args.file))


if __name__ == "__main__":
	main()
