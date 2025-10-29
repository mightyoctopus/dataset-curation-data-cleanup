
def find_data_structure(category):
    """
    Return a list of dataset file(s) corresponding to the given category argument.

    num_files_map:
        - first attr: number of file(s)
        - second attr: the last part of the file digits (e.g. full-00000-of-"00001".parquet)
    """

    dataset_base_path = f"https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023/resolve/main/raw_meta_{category}/"
    mapped_file_formats = {
        "All_Beauty": [1, "00001"],
        "Arts_Crafts_and_Sewing": [4, "00004"],
        "Cell_Phones_and_Accessories": [7, "00007"],
        "Electronics": [10, "00010"],
        "Gift_Cards": [1, "00001"],
        "Handmade_Products": [1, "00001"],
        "Industrial_and_Scientific": [2, "00002"],
        "Musical_Instruments": [2, "00002"],
        "Toys_and_Games": [5, "00005"]
    }

    files = mapped_file_formats[category]

    return [f"{dataset_base_path}full-0000{i}-of-{files[1]}.parquet" for i in range(files[0])]



# print(find_data_structure("Arts_Crafts_and_Sewing"))
