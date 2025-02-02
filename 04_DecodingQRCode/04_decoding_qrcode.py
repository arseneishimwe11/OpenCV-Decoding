import cv2
from pyzbar.pyzbar import decode

def decode_qr_code_with_pyzbar(image_path):
    try:
        # Loading the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to read")

        # Decoding QR code
        decoded_objects = decode(image)
        
        if decoded_objects:
            decoded_data = [obj.data.decode('utf-8') for obj in decoded_objects]
            print(f"Decoded Data: {decoded_data}")
            return decoded_data
        else:
            print("No QR codes detected")
            return []

    except Exception as e:
        print(f"Error: {str(e)}")
        return []

if __name__ == "__main__":
    image_path = 'IMG_2027.jpg'
    decode_qr_code_with_pyzbar(image_path)
