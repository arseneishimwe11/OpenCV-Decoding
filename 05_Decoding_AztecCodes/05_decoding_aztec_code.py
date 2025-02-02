import cv2
import numpy as np
import zxing

def decode_aztec(image_path):
    try:
        # Initializing ZXing reader
        reader = zxing.BarCodeReader()
        
        # Load and validate image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to read")

        # Decoding aztec code
        decoded = reader.decode(image_path)
        
        if decoded:
            print(f"Decoded Data: {decoded.parsed}")
            print(f"Barcode Format: {decoded.format}")
            
            # Drawing detection boundary
            if hasattr(decoded, "points") and decoded.points:
                points = np.array(decoded.points, dtype=np.int32).reshape((-1, 1, 2))
                cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)
                
                # Adding decoded text
                x, y = points[0][0]
                cv2.putText(image, decoded.parsed, (x, y - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
                # Save and display results
                cv2.imwrite("decoded_aztec.png", image)
                cv2.imshow("Decoded Aztec Code", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
            return decoded.parsed
            
        print("No Aztec code detected")
        return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    decode_aztec("aztec-code.jpg")
