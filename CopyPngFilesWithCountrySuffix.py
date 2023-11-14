import os
import shutil


def process_country_folder(country_folder, destination_folder):
    country_name = os.path.basename(country_folder)
    destination_folder = os.path.join(destination_folder, "logos-with-country-suffix")

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate over PNG files in the country folder
    for file_name in os.listdir(country_folder):
        if file_name.lower().endswith(".png"):
            source_path = os.path.join(country_folder, file_name)
            destination_name = f"{os.path.splitext(file_name)[0]}=={country_name}.png"
            destination_path = os.path.join(destination_folder, destination_name)

            # Copy the file to the new destination
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {source_path} to {destination_path}")


def main():
    base_folder = "tv-logos"
    countries_list = [
        "argentina",
        "australia",
        "brazil",
        "bulgaria",
        "canada",
        "croatia",
        "nordic/denmark",
        "france",
        "germany",
        "greece",
        "indonesia",
        "israel",
        "italy",
        "mexico",
        "netherlands",
        "new-zealand",
        "nordic/norway/",
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

    for country in countries_list:
        country_folder = os.path.join(base_folder, "countries", country)
        if os.path.exists(country_folder):
            process_country_folder(country_folder, base_folder)
        else:
            print(f"Folder not found: {country_folder}")


if __name__ == "__main__":
    main()
