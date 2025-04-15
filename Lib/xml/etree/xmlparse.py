import xml.etree.ElementTree as ET
import sys

def main():
    # Get the command-line arguments
    filename = sys.argv[1]
    plant_name = sys.argv[2]
    percent_change = float(sys.argv[3])

    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Find the plant element and modify its price
    for plant in root.findall('PLANT'):
        if plant.find('COMMON').text == plant_name:
            current_price = float(plant.find('PRICE').text)
            new_price = current_price + (current_price * percent_change / 100)
            plant.find('PRICE').text = str(round(new_price, 2))

    # Write the modified XML tree to a new file
    output_filename = f"updated_{filename}"
    tree.write(output_filename)

if __name__ == "__main__":
    main()
