import os
import shutil


def copy_and_rename_files(source_folder, destination_folder, target_countries):
    # Iterate over each country folder in the source directory
    for country_folder in os.listdir(source_folder):
        country_folder_path = os.path.join(source_folder, country_folder)

        # Check if it's a directory and if the country is in the target list
        if os.path.isdir(country_folder_path) and country_folder in target_countries:
            # Iterate over each file in the country folder
            for file_name in os.listdir(country_folder_path):
                file_path = os.path.join(country_folder_path, file_name)

                # Check if it's a PNG file
                if file_name.endswith(".png"):
                    # Generate the new file name with the specified suffix
                    new_file_name = f"{country_folder}=={file_name}"

                    # Build the destination path in the all-countries folder
                    destination_path = os.path.join(destination_folder, new_file_name)

                    # Copy the file to the destination with the new name
                    shutil.copy2(file_path, destination_path)


# Specify the paths to your source and destination folders
source_folder = r"C:\Users\heroi\OneDrive\Desktop\desktop4\projects\github\tv-logos\tv-logos\countries"
destination_folder = r"C:\Users\heroi\OneDrive\Desktop\desktop4\projects\github\tv-logos\tv-logos\countries\all-countries"

# Specify the list of target countries
target_countries = [
    "argentina",
    "australia",
    "brazil",
    "bulgaria",
    "canada",
    "croatia",
    "denmark",
    "france",
    "germany",
    "greece",
    "indonesia",
    "israel",
    "italy",
    "mexico",
    "netherlands",
    "new-zealand",
    "norway",
    "philippines",
    "poland",
    "portugal",
    "romania",
    "russia",
    "serbia",
    "south-africa",
    "spain",
    "turkey",
    "united-arab-emirates",
    "united-kingdom",
    "united-states",
    "world-middle-east",
]

# Call the function to copy and rename files
copy_and_rename_files(source_folder, destination_folder, target_countries)
