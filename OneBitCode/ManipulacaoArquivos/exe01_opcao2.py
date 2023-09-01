def file_read_from_line(file_name, n_lines):
    from itertools import islice
    with open(file_name, encoding='windows 1252') as file:
        for line in islice(file, n_lines):
            print(line.rstrip())

file_read_from_line("ArquivosAulas/exe01_cities.txt", 2)