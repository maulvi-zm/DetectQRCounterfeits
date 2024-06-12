import time
import cv2, qrdecoder, string_matching, textextract


start = time.time()

file = "tes11.png"

image = cv2.imread(file)

qrtext = qrdecoder.extract_text_from_image(file)
text = textextract.extract_text_from_image(file)

# Convert to lowercase 
qrtext = str(qrtext).lower()
text = [x.lower() for x in text]

print("QR Code: ", qrtext)
print("Text: ", text)

real = True

for word in text:
    real = real and string_matching.boyer_moore(qrtext, word) != -1

if real:
    print("Real")
else:
    print("Fake")

# print time in ms
print("Time: ", (time.time() - start) * 1000, "ms")