from openai import OpenAI
from keys import OPENAI_API_KEY
  
client = OpenAI(
  api_key = OPENAI_API_KEY
)

def translate( texto: str ) -> str:
  if ( texto ):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "Translate from english to spanish. Preserve html tags and information. DO NOT TRANSLATE LINKS, WRITE THEM THE SAME WAY. And respect the beggining and endings of phrases: If it beggins in lowercase, the ending punctuation (. , ! etc). The following text is all to be translated>>"},
            {"role":"user","content": texto}
        ]
    )
    return completion.choices[0].message.content
  else:
    raise ValueError( "Texto no puede ser vacío" )