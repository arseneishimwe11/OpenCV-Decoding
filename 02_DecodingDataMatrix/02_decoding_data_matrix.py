import cv2
from pylibdmtx import pylibdmtx

def decode_datamatrix(image_path):
    try:
        # Loading the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to read")

        # Converting to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Decoding the DataMatrix barcode
        decoded_objects = pylibdmtx.decode(gray)

        # Checking if any DataMatrix barcodes were found
        if decoded_objects:
            for obj in decoded_objects:
                print("Decoded Data: ", obj.data.decode('utf-8'))
        else:
            print("No DataMatrix codes found")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    decode_datamatrix('IMG_2019.jpg')
