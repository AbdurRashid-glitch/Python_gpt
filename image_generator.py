#api_key= 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

import os
import openai
openai.api_key = "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"

answer=openai.Image.create(
    prompt="beautiful retro countyside image",
    n=2,
    size="1024x1024"
)
print(answer)