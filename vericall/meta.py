import exiftool

def extract_metadata(file_path):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(file_path)
    return metadata

# Example usage:
file_path = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\10-86.mp3"  # Replace this with the path to your audio file
metadata = extract_metadata(file_path)
print(metadata)
