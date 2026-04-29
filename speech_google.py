from google.cloud import texttospeech


def sintetizar_mp3(texto: str) -> bytes:
    cliente = texttospeech.TextToSpeechClient()
    entrada = texttospeech.SynthesisInput(text=texto)
    voz = texttospeech.VoiceSelectionParams(
        language_code="pt-BR",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        name="pt-BR-Wavenet-D",
    )
    configuração_áudio = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=0.0,
        speaking_rate=1.0,
    )
    resposta = cliente.synthesize_speech(
        input=entrada,
        voice=voz,
        audio_config=configuração_áudio,
    )
    return resposta.audio_content
