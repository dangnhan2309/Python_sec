import sys
from PIL import Image

def decode_image(encoded_image_path):
    """Giải mã thông điệp ẩn trong hình ảnh nhanh hơn bằng cách dừng sớm khi gặp EOF Marker."""
    
    img = Image.open(encoded_image_path)
    width, height = img.size

    binary_message = []
    eof_marker = "1111111111111110"
    eof_marker_length = len(eof_marker)

    # Quét từng pixel, tìm EOF Marker để dừng sớm
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            for color_channel in range(3):
                binary_message.append(format(pixel[color_channel], '08b')[-1])

                # Kiểm tra nếu đã tìm thấy EOF Marker
                if len(binary_message) >= eof_marker_length and "".join(binary_message[-eof_marker_length:]) == eof_marker:
                    binary_message = binary_message[:-eof_marker_length]  # Cắt bỏ EOF
                    return decode_binary_message(binary_message)

    return decode_binary_message(binary_message)  # Trường hợp không tìm thấy EOF

def decode_binary_message(binary_message):
    """Chuyển chuỗi nhị phân thành văn bản."""
    message_bytes = bytearray()
    for i in range(0, len(binary_message), 8):
        message_bytes.append(int("".join(binary_message[i:i+8]), 2))
    
    return message_bytes.decode(errors="ignore")  # Bỏ qua lỗi ký tự đặc biệt

def main():
    encoded_image_path = input("Enter encoded image path: ").strip()

    try:
        decoded_message = decode_image(encoded_image_path)
        print(f"✅ Decoded message: {decoded_message}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
