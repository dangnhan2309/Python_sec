import sys
import os
from PIL import Image

def encode_image(image_path, message):
    """Mã hóa một thông điệp vào ảnh bằng phương pháp LSB (Least Significant Bit)."""

    img = Image.open(image_path)
    width, height = img.size

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Thêm chuỗi kết thúc để đánh dấu hết tin nhắn (EOF Marker)
    binary_message += '1111111111111110'  

    data_index = 0  # Chỉ số bit của thông điệp

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # Lấy giá trị pixel (R, G, B)

            for color_channel in range(3):  # Lặp qua các kênh màu
                if data_index < len(binary_message):
                    # Chỉnh sửa bit cuối của màu
                    pixel[color_channel] = (pixel[color_channel] & ~1) | int(binary_message[data_index])
                    data_index += 1
            
            img.putpixel((col, row), tuple(pixel))  # Cập nhật pixel

            if data_index >= len(binary_message):  # Nếu đã mã hóa xong, dừng lại
                break
        if data_index >= len(binary_message):
            break

    # Lưu ảnh với tên mới (tránh mất ảnh gốc)
    encode_image_path = os.path.splitext(image_path)[0] + '_encoded.png'
    img.save(encode_image_path)
    print(f"✅ Encoded image saved as: {encode_image_path}")

def main():
    # Nhận tham số từ dòng lệnh hoặc nhập thủ công
    if len(sys.argv) == 3:
        image_path = sys.argv[1]
        message = sys.argv[2]
    else:
        image_path = input("Enter image path: ").strip()
        message = input("Enter message: ").strip()

    if not os.path.exists(image_path):
        print("❌ Error: Image path does not exist!")
        sys.exit(1)

    encode_image(image_path, message)

if __name__ == "__main__":
    main()
