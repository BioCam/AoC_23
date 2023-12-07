from nbformat import read, write

def Remove_Output(Book):

	for cell in Book.cells:

		if hasattr(cell, 'outputs'):

			cell.outputs = []

			if hasattr(cell, 'prompt_number'):

				del cell['prompt_number']
			 
if __name__ == "__main__":
	Book= read(open('D05_Seed_fertilizer.ipynb'), 4)
	Remove_Output(Book)
	write(Book, open('D05_Seed_fertilizer2.ipynb', 'w'), 4)