
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": prompt,
    #         }
    #     ],
    #     model="openai/gpt-oss-120b",
    #     temperature=0.5,
    #     max_tokens=256,
    # )



import os
from groq import Groq
import base64
from dotenv import load_dotenv


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_response(base64_image, prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.5,
        max_tokens=256,
    )

    return chat_completion.choices[0].message.content


prompt = "What is in the image? Can you tell me facts about it?"
image_path = "Rose.jpg"

# Call the function to encode the image and store the result
base64_image = encode_image(image_path)

system_prompt = "Instructios : \nYou are a helpful assistant that recommends things to do, watch, read, etc. based on the user's prompt.,be crisp and to the point.\n"
print(f"prompt: {prompt}")
print(f"Response:{get_response(base64_image, system_prompt+prompt)}")
print("-" * 100)