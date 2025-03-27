
import moondream as md
from PIL import Image

model = md.vl(model='./moondream-2b-int8.mf.gz')
# model = md.vl(model='./moondream-0_5b-int8.mf.gz')

picture = './img10.png'
image = Image.open(picture)
encoded_image = model.encode_image(image)

query = 'give me make, model, color and license plate number of car. In CSV, with keys text, make text, model text,color text,number text'
answer = model.query(encoded_image, query)["answer"]
print(query)
print("\nAnswer:", answer)
#print(answer['make'])
