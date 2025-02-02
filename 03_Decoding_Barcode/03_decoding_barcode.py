import cv2
from pyzbar.pyzbar import decode

def decode_barcode(image_path):
    try:
        # Loading the image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found or unable to read")

        # Decoding the barcode
        decoded_objects = decode(img)

        # Printing the decoded data
        if decoded_objects:
            for obj in decoded_objects:
                print(f"Type: {obj.type}")
                print(f"Data: {obj.data.decode('utf-8')}")
        else:
            print("No barcodes detected")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    decode_barcode('IMG_2022.jpg')