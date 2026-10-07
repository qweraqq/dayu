import argparse

from contextlib import redirect_stdout
import logging

from pandasm.reader import PandasmReader
from pandasm.file import PandasmFile
from pandasm.pa_class import PandasmClass

logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-pa', type=str, help='specify the input text-form Panda Assembly file')
    parser.add_argument('-o', '--output-file', type=str, help='write printed output to the specified file instead of stdout')
    args = parser.parse_args()
    return args


def dump_classes_and_methods(pafile: PandasmFile):
    for clz in pafile.iter_classes():
        clz: PandasmClass = clz
        print("# " + clz.name)
        print("## " + "Fields")
        for field in clz.fields:
            print("- " + str(field))
        print("## " + "Methods")
        for method in clz.methods:
            print("- " + str(method))

    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    args = parse_args()
    if not args.pa or not args.output_file:
        logger.error('Please specify pa file and output file')
        exit(-1)

    pafile = PandasmReader.from_file(args.pa)
    
    with open(args.output_file, 'w', encoding='utf-8') as output_stream:
        with redirect_stdout(output_stream):
            dump_classes_and_methods(pafile)
