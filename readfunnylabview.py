
import sys
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input Labview file')#, nargs='*')
    parser.add_argument('-o', '--output', default='pipes.csv', help='Relative or absolute path of the output csv file, (default: pipes.csv)')
    parser.add_argument('--open', action='store_true', default=False,
                            help='Open  text file after ')
    args = parser.parse_args()
    print(args.input)

    if args.input:
        csv_file = open(args.input, 'r')
        outputFile = open(args.output,'w')
        lines = csv_file.readlines()

        for line in lines:
            text = line.replace(',',';',3)
            text = text.replace('NaN','0,00')
            for i in range(0,10):
                text = text.replace(',','.',1)
                text = text.replace(',',';',1)
        
            text = text.replace(',',';',1)
            text = text[:-2]
            text = text.replace(';',',')
            print(text, file=outputFile)
        outputFile.close()

    if args.open:
        if sys.platform == "win32":
            subprocess.call(["explorer.exe", args.output])
        else:
            subprocess.call(["gedit", args.output])


   
if __name__ == "__main__": 
	# calling the main function 
	main()
