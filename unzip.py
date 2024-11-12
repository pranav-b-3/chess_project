import zstandard as zstd

def unzip_zst(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(infile) as reader:
            outfile.write(reader.read())

if __name__ == "__main__":
    input_file = "lichess_db_standard_rated_2013-01.pgn.zst"  # Replace with your actual file path
    output_file = "out.pgn"  # Replace with desired output file name
    unzip_zst(input_file, output_file)