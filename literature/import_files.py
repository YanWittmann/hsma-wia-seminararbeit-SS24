import os
import shutil
import subprocess

invalid_file_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '\'']

def get_valid_filename(name):
    for char in invalid_file_chars:
        name = name.replace(char, "")
    return name

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def get_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

def copy_and_rename_pdfs(input_directory, target_directory, known_names):
    ensure_directory_exists(target_directory)
    clear_directory(target_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(".pdf"):
            input_filepath = os.path.join(input_directory, filename)
            print(f"Processing {filename}...")
            try:
                if filename in known_names and known_names[filename] != "":
                    new_title = get_valid_filename(known_names[filename]) + (".pdf" if known_names[filename].endswith(".pdf") else "")
                else:
                    result = subprocess.run(["pdftitle", "-p", input_filepath], capture_output=True, text=True)
                    if result.returncode == 0:
                        new_title = filename.replace(".pdf", "") + " " + get_valid_filename(result.stdout.strip())
                    else:
                        new_title = filename.replace(".pdf", "")
                new_filename = new_title + ".pdf"
                new_filename = get_unique_filename(target_directory, new_filename)
                target_filepath = os.path.join(target_directory, new_filename)
                shutil.copy(input_filepath, target_filepath)
                print(f"  --> {new_filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

input_directory = "C:\\Users\\yan20\\AppData\\Local\\Swiss Academic Software\\Citavi 6\\ProjectCache\\o4dlpde2nswsn35ugnd4pj86kw5dp5ruh3i2iwzz74qotpy\\Citavi Attachments"
target_directory = "original"
known_names = {
    "1ef45ee8-e571-4135-af84-73551d50565f.pdf": "Proposed Design and Modeling of Smart Energy Dashboard System by Implementing IoT (Internet of Things) Based on Mobile Devices",
    "4debfdd5-bab2-4f49-a7ec-9e0695aa9ad1.pdf": "A Mobile Dashboard for Analytics-based Information Provisioning on the Shop Floor",
    "4ef608c8-b6b5-454b-a72d-cb8628323f90.pdf": "Responsive Web Design Mode and Application",
    "5f4163f1-ec89-499b-a3fb-6556e064cbe8.pdf": "Preserving Privacy For Location Based Services With Continuous Queries",
    "7a9f31da-58a9-49b8-9fbf-bceab411e302.pdf": "State of the Art: Coordinated & Multiple Views in Exploratory Visualization",
    "7b486e1c-d2ff-49d0-9448-445052feedd0.pdf": "A Flexible Dashboard Panel for a Small Electric Vehicle",
    "8bcf871e-aca4-4bfc-8012-d3a9140cb0bf.pdf": "Interactive Dynamics for visual analysis",
    "46eb8b37-3c21-4afd-a98d-b211a97ad11e.pdf": "Design Patterns and Trade-Offs in Responsive Visualization for Communication",
    "61e51663-0d3c-4f2a-9493-9a28411d0443.pdf": "A Design Space of Visualization Tasks",
    "65ff4045-2419-4cf3-ad17-44dc17dd8dfe.pdf": "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations",
    "73d422b6-6a16-4490-9075-da41fd9aa16b.pdf": "Mobile Web & Responsive Webdesign",
    "378d8ff2-db1f-41d1-9915-3bd206f8424f.pdf": "What Do We Talk About When We Talk About Dashboards",
    "945c439e-4396-48b4-819c-3e9abb2a27bf.pdf": "Riding the Technology Wave Effective Dashboard Data Visualization",
    "03277bd4-0a95-4cf0-a683-a17c30b549a3.pdf": "Dashboard Design Patterns",
    "46229c94-8511-49c2-9e74-e00cf3e19821.pdf": "Towards User Interface Components for Dashboard Applications on Smartphones",
    "78755c40-b39d-4f7c-8853-4d0e8f3eeb5f.pdf": "D3: Data-Driven Documents",
    "690947c8-ba3b-4363-b64b-72eac3d3cfa5.pdf": "Edward Tufte: Beautiful Evidence",
    "a203860a-a22e-4f28-ae08-7e5326ed95ae.pdf": "Tutorial: Mobile BI",
    "add8ddff-10c5-47b6-8d0f-7f38a238e703.pdf": "Creating Support Content for Responsive Websites at Microsoft Mobile",
    "ae6032a6-74b4-4834-a1c5-528d5c971483.pdf": "A handheld classroom dashboard: Teachers perspectives on the use of real-time collaborative learning analytics",
    "aee8aa3f-54cb-4687-9fc6-1b3031893638.pdf": "Web Application for Information Dashboard Design",
    "b7bef40c-c21f-46f8-a312-05e47dcf74c7.pdf": "The Structure of the Information Visualization Design Space",
    "be3072d4-8882-4e98-8034-7d2e7b724b0e.pdf": "Design Patterns Elements of Reusable Object-Oriented Software",
    "be648595-4541-4a05-90a1-989ee0cb1b68.pdf": "Wie kann mit Hilfe von Responsive Webdesign (RWD) die Usability von Websites verbessert werden",
    "c7788501-8662-4bc0-b6e6-4bc0f6fee210.pdf": "Web Engineering: 19th International Conference, ICWE 2019",
    "d7f6d5fe-3749-476c-9628-3573a0082854.pdf": "Connecting domain-specific features to source code: towards the automatization of dashboard generation",
    "d643f754-2ed5-4de7-9bce-6efc3146989c.pdf": "Geolocation in the Browser",
    "d934e73a-1b90-4be1-b193-302a324c3fcd.pdf": "Exploration Views: Understanding Dashboard Creation and Customization for Visualization Novices",
    "da19eb0b-f9b5-4b92-9451-097503b89dfb.pdf": "Ch.6 Mobile Application Designing Dashboards for mobile applications",
    "f6de2a69-2f73-412d-bfcf-d0852940ed2f.pdf": "A review of dashboards in performance management: Implications for design and research",
    "5f5f2de2-2311-4dbd-b786-598fe1c7b766.pdf": "Implementing Responsive Design in Industrial Dashboard Editor",
    "b28f7427-cddc-46b6-ba86-829814365fc0.pdf": "Adaptive Web Design: Crafting rich experiences with Progressive Enhancement",
    "f1a528a5-6e5c-4bb5-bfdb-e0e286cede70.pdf": "Responsible Responsive Design - Planning For Performance",
}
copy_and_rename_pdfs(input_directory, target_directory, known_names)
