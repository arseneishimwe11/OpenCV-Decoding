import cv2
import numpy as np
import zxing

def decode_maxicode(image_path):
    try:
        # Initializing ZXing reader
        reader = zxing.BarCodeReader()
        
        # Loading and validating image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to read")

        # Decoding MaxiCode
        decoded = reader.decode(image_path, possible_formats=['MAXICODE'])
        
        if decoded and decoded.parsed:
            print(f"Decoded Data: {decoded.parsed}")
            return decoded.parsed
            
        print("No MaxiCode detected")
        return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    decode_maxicode("maxicode.jpg")
